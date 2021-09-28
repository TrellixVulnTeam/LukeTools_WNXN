#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Green
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob("mappings").setValue([(0, 'rgba.green', 'rgba.red'), (0, 'rgba.green', 'rgba.green'), (0, 'rgba.green', 'rgba.blue'), (0, 'rgba.green', 'rgba.alpha')])