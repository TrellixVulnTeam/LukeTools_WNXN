#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Roto 10% safezone
# COLOR: #195213
#
#----------------------------------------------------------------------------------------------------------

for n in nuke.selectedNodes():
    width_offset = n.width()/10
    height_offset = n.height()/10
    
    n.knob('intersect').setValue(1)
    n.knob('crop').setValue(0)
    
    n.knob('box').setValue(0-width_offset,0)
    n.knob('box').setValue(0-height_offset,1)
    n.knob('box').setValue(n.width()+width_offset,2)
    n.knob('box').setValue(n.height()+height_offset,3)
    