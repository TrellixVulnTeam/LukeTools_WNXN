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
        if n.Class() == "Dot":
            if "Connector" not in n.name():
                ret = True 