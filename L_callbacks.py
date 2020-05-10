import nuke
import nukescripts

def updateAllWriteNames():
    if nuke.toNode("L_PROJECT"):
        for n in nuke.allNodes("Write"):
            updateWriteName(n)

def updateWriteName(n = ""):
    if nuke.toNode("L_PROJECT"):
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
            pwrite += n.knob("preLabel").getValue() + '/'
            pwritename += n.knob("preLabel").getValue() + '_'

        versionnumber = '001'

        if n.knob("versionOverride").getValue():
            versionnumber = n.knob("versionOverride").getValue()
        else:
            versionnumber = nukescripts.version_get(nuke.root().name(), 'v')[1]

        pwrite += 'v' + versionnumber + '/'
        pwritename += 'v' + versionnumber + '.######.'

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
