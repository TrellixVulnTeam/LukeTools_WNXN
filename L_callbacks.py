import nuke
import nukescripts
import re
import os

def updateAllWriteNames():
    if nuke.toNode("L_PROJECT"):
        for n in nuke.allNodes("Write"):
            updateWriteName(n)


def updateWriteNameCallback(n = ""):
    if not n:
        n = nuke.thisNode()
    
    kname = ''
    if nuke.thisKnob():
        kname = nuke.thisKnob().name()

    if kname in ['selected', 'pre', 'preLabel', 'versionOverride']:
        if nuke.toNode("L_PROJECT"):
            updateWriteName(n)


def updateWriteName(n = ""):

    if not n:
        n = nuke.thisNode()

    if 'override_all' in n.knobs():
        if n['override_all'].getValue():
            return
        
    if nuke.toNode("L_PROJECT"):
       

        pn = nuke.toNode("L_PROJECT")

        pwrite = pn.knob('proot').getValue() + pn.knob('pproject').getValue() + '/' + pn.knob('pshot').getValue() + '/out/'
        pwritename = pn.knob('pproject').getValue() + '_' + pn.knob('pshot').getValue() + '_'

        pwrite += pn.knob('ptask').getValue() + '/'
        pwritename += pn.knob('ptask').getValue() + '_'

        if n.knob("pre").getValue():
            pwrite += 'pre/'
            pwritename += 'prerender_'

        if n.knob("preLabel").getValue():
            prelabel = re.sub(r'[\s]', '', n.knob("preLabel").getValue())
            n.knob("preLabel").setValue(prelabel)
            pwrite += prelabel + '/'
            pwritename += prelabel + '_'

        versionnumber = '001'

        if n.knob("versionOverride").getValue():
            versionnumber = re.sub(r'[\D]', '', n.knob("versionOverride").getValue())
            n.knob("versionOverride").setValue(versionnumber)

        elif nuke.root().name():
            versionnumber = re.search("v\d+", os.path.basename(nuke.root().name())).group()[1:]

        pwrite += 'v' + versionnumber + '/'

        if n['file_type'].value() == 'mov':
            if "mov64_codec" in n.knobs():
                if n.knob("mov64_codec").value() == "appr":
                    prorescodec = ["prores444XQ", "prores444", "prores422HQ", "prores422", "prores422LT", "prores422proxy"]
                    pwritename += prorescodec[int(n.knob("mov_prores_codec_profile").getValue())] + '_'

                elif n.knob("mov64_codec").value() == "h264":
                    pwritename += 'h264_'
            pwritename += 'v' + versionnumber

        else:
            pwritename += 'v' + versionnumber
            pwritename += '.####'
            
        pwritename += '.'

        pwrite += n.knob('file_type').value() + '/'
        pwritename += n.knob('file_type').value()

        n.knob('file').setValue(pwrite + pwritename)

    else:
        nuke.message("No L_PROJECT found")

def enableOnRender():
    for n in nuke.allNodes():
        if "enableOnRender" in n.knob('label').getValue():
            n.knob('disable').setValue(False)
        if "disableOnRender" in n.knob('label').getValue():
            n.knob('disable').setValue(True)
        
def writeNodeFields():
    n = nuke.thisNode()

    if not n.knob('Luke'):
        k = nuke.Tab_Knob("Luke","Luke")
        n.addKnob(k)

        k = nuke.Boolean_Knob("pre","Pre Render")
        n.addKnob(k)

        k = nuke.String_Knob("preLabel","Pre Render Label")
        n.addKnob(k)

        k = nuke.String_Knob("versionOverride","Render Version Override")
        n.addKnob(k)

        k = nuke.PyScript_Knob("applyNaming","Apply","L_callbacks.updateWriteName(nuke.thisNode())")
        k.setFlag(nuke.STARTLINE)
        n.addKnob(k)

        k = nuke.Boolean_Knob("override_all","Disable write node naming callback")
        k.setFlag(nuke.STARTLINE)
        n.addKnob(k)