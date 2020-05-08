#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: create Read
# COLOR: #245626
#
#----------------------------------------------------------------------------------------------------------

import LL_pyseq

for node  in nuke.selectedNodes():
    if node["file"].value():
        seq = LL_pyseq.img2pyseq(node["file"].value())
        read = nuke.nodes.Read(file=node["file"].value(), 
                                    xpos=node.xpos()+0,
                                    ypos=node.ypos()+100,
                                    first=seq.start(),
                                    last=seq.end(),
                                    origfirst = seq.start(),
                                    origlast= seq.end())
    

        read.knob('colorspace').setValue(int(node.knob('colorspace').getValue()))
        node.setSelected(False)
    