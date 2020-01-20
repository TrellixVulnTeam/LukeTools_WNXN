#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# IGNORE CLASSES: 0
#
#----------------------------------------------------------------------------------------------------------

nodes = nuke.selectedNodes()
if len(nodes) == 1:
    if "OF_SAVER" in nodes[0].name() and "NoOp" in nodes[0].Class():
        ret = True