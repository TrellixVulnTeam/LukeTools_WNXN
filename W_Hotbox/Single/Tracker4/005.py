#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: new Roto
# COLOR: #175218
#
#----------------------------------------------------------------------------------------------------------

import nuke, os, re


sel = None

for sel in nuke.selectedNodes():
    
    X = sel.xpos()
    Y = sel.ypos()

    rt = nuke.createNode('Roto')
    rt.setInput(0, None)
    rt.setXYpos(X,Y+150)
    
    rt['label'].setValue(sel['name'].getValue())
        
    rt['translate'].fromScript(sel['translate'].toScript())
    rt['rotate'].fromScript(sel['rotate'].toScript())
    rt['scale'].fromScript(sel['scale'].toScript())
    rt['center'].fromScript(sel['center'].toScript())
    rt['opacity'].setValue(1)
    