#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# IGNORE CLASSES: 0
#
#----------------------------------------------------------------------------------------------------------

nodes = nuke.selectedNodes()
if len(nodes) == 1:
    for n in nodes:
        if "L_PROJECT" in n.name():
            ret = True 