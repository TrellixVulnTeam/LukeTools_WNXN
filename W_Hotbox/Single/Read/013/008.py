#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: toggle RAW
#
#----------------------------------------------------------------------------------------------------------

for n in nuke.selectedNodes():
    n.knob('raw').setValue(not n.knob('raw').getValue())