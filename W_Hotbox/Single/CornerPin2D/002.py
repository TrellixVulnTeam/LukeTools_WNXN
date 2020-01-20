#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: MochaName
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    original = i.knob('name').value()
    updated = original.replace('CornerPin2D', 'CP_Mocha')
    i.knob('name').setValue(updated)