#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: DotHigh
# COLOR: #bababa
# TEXTCOLOR: #111111
#
#----------------------------------------------------------------------------------------------------------

nodes = nuke.selectedNodes()


if len(nodes) == 2:

    if nodes[0].ypos() > nodes[1].ypos():
        upper = nodes[1]
        lower = nodes[0]

    else:
        upper = nodes[0]
        lower = nodes[1]
        
    dependent = False
    try:
        if lower == upper.dependent()[0]:
            dependent = True
    except:
        pass
            
    dot = nuke.Node('Dot')

    dot.setXpos(lower.xpos()+lower.screenWidth()/2-dot.screenWidth()/2)
    dot.setYpos(upper.ypos()+upper.screenHeight()/2-dot.screenHeight()/2)
    
    if not dependent:       
        dot.setInput(0,upper)
        lower.setInput(0,dot)
    
else:
    nuke.Node('Dot')