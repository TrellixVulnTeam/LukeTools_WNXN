#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Set Project Framerange
#
#----------------------------------------------------------------------------------------------------------

node = nuke.selectedNodes()[0]

first = node.knob('first_frame').value()
last = node.knob('last_frame').value()

nuke.Root().knob('first_frame').setValue(first)
nuke.Root().knob('last_frame').setValue(last)