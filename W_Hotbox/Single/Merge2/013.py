#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: New Mask
# COLOR: #305132
#
#----------------------------------------------------------------------------------------------------------

def emptySelection(selection):
    for i in selection:
        i.knob('selected').setValue(False)

selection = nuke.selectedNodes()

emptySelection(selection)

for i in selection:

    rotoNode = nuke.createNode('Roto')
    blurNode = nuke.createNode('Blur')
    dotNode = nuke.createNode('Dot', inpanel = False)
    postion = [i.xpos()-i.screenWidth()/2,i.ypos()+i.screenHeight()/2]

    dotNode.setXpos(int(postion[0]+200-dotNode.screenWidth()/2))
    dotNode.setYpos(int(postion[1]-dotNode.screenHeight()/2))
    
    blurNode.setXpos(int(postion[0]+200-blurNode.screenWidth()/2))
    blurNode.setYpos(int(postion[1]-70+blurNode.screenHeight()/2))

    rotoNode.setXpos(int(postion[0]+200-rotoNode.screenWidth()/2))
    rotoNode.setYpos(int(postion[1]-110+rotoNode.screenHeight()/2))

    i.setInput(2,dotNode)
    nuke.show(blurNode)
    nuke.show(rotoNode)
    emptySelection(selection)