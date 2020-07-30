import nuke
import nukescripts
import re
import os

def updateAllWriteNames():
    if nuke.toNode("L_PROJECT"):
        for n in nuke.allNodes("Write"):
            updateWriteName(n)

def updateWriteName(n = ""):
    kname = ''
    if nuke.thisKnob():
        kname = nuke.thisKnob().name()
        
    if nuke.toNode("L_PROJECT") and not kname in ['xpos','ypos']:
        if not n:
            n = nuke.thisNode()

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
        pwritename += 'v' + versionnumber

        if n['file_type'].value() == 'mov':
            metacodec = {
                "apcn" : "prores422", 
                "apch" : "prores422hq", 
                "apcs" : "prores422LT", 
                "apco" : "prores422PR", 
                "ap4h" : "prores444", 
                "ap4x" : "prores444XQ"
                }

            if n['meta_codec'].value() in metacodec:
                pwritename += '_' + metacodec[n['meta_codec'].value()]

            

        else:
            pwritename += '.####'
            
        pwritename += '.'

        pwrite += n.knob('file_type').value() + '/'
        pwritename += n.knob('file_type').value()

        n.knob('file').setValue(pwrite + pwritename)

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
