#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: set out_rec709
#
#----------------------------------------------------------------------------------------------------------

for n in nuke.selectedNodes():
    n.knob('colorspace').setValue("Output - Rec.709")