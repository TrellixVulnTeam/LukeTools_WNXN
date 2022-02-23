#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Limit to Project Range
# COLOR: #52462c
#
#----------------------------------------------------------------------------------------------------------

for n in nuke.selectedNodes():
    n.knob('use_limit').setValue(True)
    n.knob('first').setValue(nuke.root().knob('first_frame').getValue())
    n.knob('last').setValue(nuke.root().knob('last_frame').getValue())