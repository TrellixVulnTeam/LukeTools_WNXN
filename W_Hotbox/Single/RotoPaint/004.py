#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: replace
#
#----------------------------------------------------------------------------------------------------------

for n in nuke.selectedNodes():
    n.knob('replace').setValue(1)
    if 'replace channels' not in n.knob('label').getValue():
        old = n.knob('label').getValue()
        if old:
            n.knob('label').setValue(old+'\nreplace channels')
        else:
            n.knob('label').setValue('replace channels')