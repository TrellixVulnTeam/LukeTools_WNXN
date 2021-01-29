#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: set lin_srgb
#
#----------------------------------------------------------------------------------------------------------

for n in nuke.selectedNodes():
    n.knob('colorspace').setValue("Utility - Linear - sRGB")