#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Limit to Project Range
# COLOR: #52462c
#
#----------------------------------------------------------------------------------------------------------

node = nuke.selectedNode()

first = nuke.Root().knob('first_frame').value()
last = nuke.Root().knob('last_frame').value()

node.knob('first').setValue(int(first))
node.knob('last').setValue(int(last))

