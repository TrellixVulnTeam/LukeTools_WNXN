#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Plus (rgb)
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('output').setValue('rgba')
    
    i.knob('output').enableChannel(0,1)
    i.knob('output').enableChannel(1,1)
    i.knob('output').enableChannel(2,1)
    i.knob('output').enableChannel(3,0)
    
    i.knob('operation').setValue('plus')