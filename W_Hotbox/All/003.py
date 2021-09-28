#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: paste to each selected
# COLOR: #434e52
#
#----------------------------------------------------------------------------------------------------------

selection = nuke.selectedNodes()

newNodes = []

for i in selection:
    i.knob('selected').setValue('False')

for i in selection:
    i.knob('selected').setValue('True')
    nuke.nodePaste('%clipboard%')
    newNodes.append(nuke.selectedNode())
    
for i in newNodes:
    i.knob('selected').setValue('True')