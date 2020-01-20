#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Mask / Stencil
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('output').setValue('rgba')
    if i.knob('operation').value() == 'mask':
        i.knob('operation').setValue('stencil')
    else:
        i.knob('operation').setValue('mask')