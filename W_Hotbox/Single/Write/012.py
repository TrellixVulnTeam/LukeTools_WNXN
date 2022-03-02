#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Limit to Input Range
# COLOR: #52462c
#
#----------------------------------------------------------------------------------------------------------

for n in nuke.selectedNodes():
    n.knob('use_limit').setValue(True)
    n.knob('first').setValue(n.frameRange().first())
    n.knob('last').setValue(n.frameRange().last())