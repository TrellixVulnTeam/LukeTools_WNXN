#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Convert Matrix To Translation
#
#----------------------------------------------------------------------------------------------------------

def convert_cam(cam):
    import math
    print "converting " + cam.name()
    
    mResult = nuke.math.Matrix4()   
    
    p = nuke.Panel( "Convert Cam Matrix to Translation" )
    p.addSingleLineInput('Start Frame', '1001')
    p.addSingleLineInput('End Frame', '1100')
    p.addBooleanCheckBox('translate', True)
    p.addBooleanCheckBox('rotate', True)
    p.addBooleanCheckBox('scale', False)
    result = p.show()
    
    if not result:
        return

    start = p.value("Start Frame")
    end = p.value("End Frame")
    dotranslate = p.value("translate")
    dorotate = p.value("rotate")
    doscale = p.value("scale")
    
    if start.isdigit()and end.isdigit():
        start = int(start)
        end = int(end)
        
    else:
        nuke.message("Enter digits only")
        return
        
    ziel = nuke.createNode("Camera2")  
     
    for frame in range(start,end):
        for i in range(0,16):
            mResult[i] = cam.knob('matrix').valueAt(frame)[i]
    
    
        mResult.transpose()
        mTranslate = nuke.math.Matrix4(mResult)
        mTranslate.translationOnly()
        mRotate = nuke.math.Matrix4(mResult)
        mRotate.rotationOnly()
        mScale = nuke.math.Matrix4(mResult)
        mScale.scaleOnly()
        translate = (mTranslate[12], mTranslate[13], mTranslate[14])
        rotateRad = mRotate.rotationsZXY()
        rotate = (math.degrees(rotateRad[0]), math.degrees(rotateRad[1]), math.degrees(rotateRad[2]))
        scale = (mScale.xAxis().x, mScale.yAxis().y, mScale.zAxis().z)
        if dotranslate:
            if not ziel.knob("translate").isAnimated():
                ziel.knob("translate").setAnimated()
            ziel.knob("translate").setValueAt(translate[0], frame, 0)
            ziel.knob("translate").setValueAt(translate[1], frame, 1)
            ziel.knob("translate").setValueAt(translate[2], frame, 2)
        
        if dorotate:
            if not ziel.knob("rotate").isAnimated():
                ziel.knob("rotate").setAnimated()
            ziel.knob("rotate").setAnimated()
            ziel.knob("rotate").setValueAt(rotate[0], frame, 0)
            ziel.knob("rotate").setValueAt(rotate[1], frame, 1)
            ziel.knob("rotate").setValueAt(rotate[2], frame, 2)
        
        if doscale:
            if not ziel.knob("scaling").isAnimated():
                ziel.knob("scaling").setAnimated()
            ziel.knob("scaling").setAnimated()
            ziel.knob("scaling").setValueAt(scale[0], frame, 0)
            ziel.knob("scaling").setValueAt(scale[1], frame, 1)
            ziel.knob("scaling").setValueAt(scale[2], frame, 2)
        
        ziel.knob('focal').setValue(cam.knob('focal').value())
        ziel.knob('haperture').setValue(cam.knob('haperture').value())
        ziel.knob('vaperture').setValue(cam.knob('vaperture').value())
        ziel.knob('near').setValue(cam.knob('near').value())
        ziel.knob('far').setValue(cam.knob('far').value())
        
        ziel.setInput(0,None)
        ziel.setXpos(cam.xpos())
        ziel.setYpos(cam.ypos()+100)


cams = nuke.selectedNodes()

for cam in cams:
    convert_cam(cam)

    