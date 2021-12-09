#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: set out_srgb
#
#----------------------------------------------------------------------------------------------------------

for n in nuke.selectedNodes():
    n.knob('colorspace').setValue("Output - sRGB")