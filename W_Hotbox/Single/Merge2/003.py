#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Plus / From (rgb)
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('output').setValue('rgb')
    if i.knob('operation').value() == 'plus':
        i.knob('operation').setValue('from')
    else:
        i.knob('operation').setValue('plus')