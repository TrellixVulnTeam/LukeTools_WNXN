#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Default
#
#----------------------------------------------------------------------------------------------------------

nodes = nuke.selectedNodes()

for n in nodes:
    n.knob('tile_color').setValue(nuke.defaultNodeColor(n.Class()))
