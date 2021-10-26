#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: create Connector
# COLOR: #54360f
#
#----------------------------------------------------------------------------------------------------------

txt = nuke.getInput('Change label', 'new label')

if txt:
    n = nuke.createNode("Dot", inpanel = False)
    n.setName("Connector")
    n.knob('note_font_size').setValue(22)
    n.knob('label').setValue(txt.upper())
    n.setYpos(n.ypos()+50)
