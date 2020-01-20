#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Reload all Reads
# COLOR: #2c522c
#
#----------------------------------------------------------------------------------------------------------

for read in nuke.allNodes("Read"):
        read.knob('reload').execute()