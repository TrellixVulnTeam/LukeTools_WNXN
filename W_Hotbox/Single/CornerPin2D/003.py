#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: PaintMatrix
#
#----------------------------------------------------------------------------------------------------------


import nuke
import nukescripts
import nuke.rotopaint as rp
import threading

################

def getCornerPinMatrixAtFrame(node, frame, refFrame):
    
    projectionMatrixTo = nuke.math.Matrix4()
    projectionMatrixFrom = nuke.math.Matrix4()

    toValues = []
    fromValues = []

    for i in range(1,5):
        for j in range(2):
            toVal = node["to{0}".format(i)].valueAt(frame)[j]
            fromVal = node["to{0}".format(i)].valueAt(refFrame)[j] 

            toValues.append(toVal)
            fromValues.append(fromVal)

    projectionMatrixTo.mapUnitSquareToQuad(toValues[0], toValues[1], toValues[2], toValues[3], toValues[4], toValues[5], toValues[6], toValues[7])
    projectionMatrixFrom.mapUnitSquareToQuad(fromValues[0], fromValues[1], fromValues[2], fromValues[3], fromValues[4], fromValues[5], fromValues[6], fromValues[7])

    matrix = projectionMatrixTo*projectionMatrixFrom.inverse()    
    matrix.transpose()

    return matrix



#--------------------------------''' Define Frame Range'''---------------------------------    
    
frames = nuke.getFramesAndViews('get FrameRange', '%s-%s' % (nuke.root().firstFrame(), nuke.root().lastFrame()))
frame_range = nuke.FrameRange( frames[0] )




n = nuke.selectedNode()
n["selected"].setValue(False)

ref = 1001


c = nuke.createNode("RotoPaint")

curve = c['curves']
root = curve.rootLayer
transform = root.getTransform()


for i in frame_range:
    matrix = getCornerPinMatrixAtFrame(n, i, ref)
    for j in range(16):
        extraMatrixKnob = transform.getExtraMatrixAnimCurve(0,j)
        extraMatrixKnob.addKey(i,matrix[j])

tn = str(n['name'].getValue())
tr = str(frame_range)
c["label"].setValue('Matrix -- ' + tn + '\n FrameRange ' + tr)

xpos = n['xpos'].value()
ypos = n['ypos'].value()
            
c_width = c.screenWidth()
c_height = c.screenHeight()
            
c.setXYpos(int(xpos) + int(c_width) + 50 , int(ypos))