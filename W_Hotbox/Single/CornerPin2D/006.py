#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Invert
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    invertKnob = i.knob('invert')
    invertKnob.setValue(1-int(invertKnob.value()))