#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# IGNORE CLASSES: 0
#
#----------------------------------------------------------------------------------------------------------

nodes = nuke.selectedNodes()

for n in nodes:
    if "ffmpeg_write" in n.name():
        ret = True 