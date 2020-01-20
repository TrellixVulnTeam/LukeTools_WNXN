#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: SetRefFrame
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    From1Knob = i.knob('from1')
    From2Knob = i.knob('from2')
    From3Knob = i.knob('from3')
    From4Knob = i.knob('from4')

    From1Knob.setExpression('to1.x',0)
    From1Knob.setExpression('to1.y',1)
    From2Knob.setExpression('to2.x',0)
    From2Knob.setExpression('to2.y',1)
    From3Knob.setExpression('to3.x',0)
    From3Knob.setExpression('to3.y',1)
    From4Knob.setExpression('to4.x',0)
    From4Knob.setExpression('to4.y',1)
    
    From1Knob.clearAnimated()
    From2Knob.clearAnimated()
    From3Knob.clearAnimated()
    From4Knob.clearAnimated()
    
    i.knob('shutteroffset').setValue(0)
    
    CurrFrm = (nuke.frame())
    i.knob('label').setValue(str(CurrFrm))