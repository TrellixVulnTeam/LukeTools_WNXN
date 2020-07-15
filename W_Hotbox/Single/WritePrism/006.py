#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: create Read
# COLOR: #245626
#
#----------------------------------------------------------------------------------------------------------

import pythonlibrary.L_pyseq as L_pyseq

for node  in nuke.selectedNodes():
    if node["fileName"].value():
        seq = L_pyseq.img2pyseq(node["fileName"].value())
        if seq:
            read = nuke.nodes.Read(file=node["fileName"].value(), 
                                        xpos=node.xpos()+0,
                                        ypos=node.ypos()+100,
                                        first=seq.start(),
                                        last=seq.end(),
                                        origfirst = seq.start(),
                                        origlast= seq.end())
                                        
            read.knob('colorspace').setValue(int(node.knob('colorspace').getValue()))
            node.setSelected(False)
            
        else:
            nuke.message('No files found')    
                  
    else:
        nuke.message('No valid filepath')
    

        
    