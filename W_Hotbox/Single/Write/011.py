#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Disable all other Writes
#
#----------------------------------------------------------------------------------------------------------

tempWrites = []
for n in nuke.selectedNodes():
    tempWrites.append(n)
    n.knob('disable').setValue(False)

for n in nuke.allNodes("Write"):
    if n not in tempWrites:
        n.knob('disable').setValue(True)