#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: alpha
# COLOR: #50523b
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('output').setValue('rgba')
    i.knob('output').enableChannel(0,0)
    i.knob('output').enableChannel(1,0)
    i.knob('output').enableChannel(2,0)
    i.knob('output').enableChannel(3,1)
    