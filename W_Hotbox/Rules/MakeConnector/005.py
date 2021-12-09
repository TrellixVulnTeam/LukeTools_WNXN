#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: make Connector
# COLOR: #54360f
#
#----------------------------------------------------------------------------------------------------------

n = nuke.selectedNode()

txt = nuke.getInput('Change label', 'new label')

if txt:
    n.setName("Connector")
    n.knob('note_font_size').setValue(22)
    n.knob('label').setValue(txt.upper())
