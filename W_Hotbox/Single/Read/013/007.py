#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: set srgb_texture
#
#----------------------------------------------------------------------------------------------------------

for n in nuke.selectedNodes():
    n.knob('colorspace').setValue("Utility - sRGB - Texture")