#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: create Camera from RS EXR
#
#----------------------------------------------------------------------------------------------------------

# code copied and adapted from https://pastebin.com/4vmAmARU

# Big thanks to Ivan Busquets who helped me put this together!
# (ok, ok, he really helped me a lot)
# Also thanks to Nathan Dunsworth for giving me solid ideas and some code to get me started.

import math


def createExrCamRS( node ):
    '''
    Create a camera node based on VRay metadata.
    This works specifically on VRay data coming from maya.
    '''

    mDat = node.metadata()
    reqFields = ['exr/rs/camera/%s' % i for i in ('DOFFocusDistance', 'FStop', 'transform')]
    if not set( reqFields ).issubset( mDat ):
        nuke.critical( 'No metadata for camera found! Please select a read node with EXR metadata from RS!' )
        return

    first = node.firstFrame()
    last = node.lastFrame()
    ret = nuke.getFramesAndViews( 'Create Camera from Metadata', '%s-%s' %( first, last ) )
    if ret is None:
        return
    fRange = nuke.FrameRange( ret[0] )
    
    cam = nuke.createNode( 'Camera3' )
    cam['useMatrix'].setValue( False )
    
    for k in ( 'focal', 'haperture', 'vaperture', 'translate', 'rotate', 'focal_point'):
        cam[k].setAnimated()
    
    task = nuke.ProgressTask( 'Baking camera from meta data in %s' % node.name() )
    
    for curTask, frame in enumerate( fRange ):
        if task.isCancelled():
            break
        task.setMessage( 'processing frame %s' % frame )
        
        hap = 1.0 # get horizontal aperture
        fov = node.metadata( 'exr/rs/camera/fov', frame ) # get camera FOV
        
        focal = float(hap) / ( 2.0 * math.tan( math.radians(float(fov)) * 0.5 ) ) # convert the fov and aperture into focal length

        width = node.metadata( 'input/width', frame )
        height = node.metadata( 'input/height', frame )
        focalDistance = node.metadata( 'exr/rs/camera/DOFFocusDistance', frame )
        aspect = float(width) / float(height) # calulate aspect ratio from width and height
        vap = float(hap) / aspect # calculate vertical aperture from aspect ratio
        
        cam['focal'].setValueAt( float(focal), frame )
        cam['haperture'].setValueAt( float(hap), frame )
        cam['vaperture'].setValueAt( float(vap), frame )
        cam['focal_point'].setValueAt( float(focalDistance), frame )
        
        matrixCamera = node.metadata( 'exr/rs/camera/transform', frame ) # get camera transform data
        
        # create a matrix to shove the original data into 
        matrixCreated = nuke.math.Matrix4()
        
        for k,v in enumerate( matrixCamera ):
            matrixCreated[k] = v
        
        matrixCreated.rotateY( math.radians(-180) ) # this is needed for VRay, it's a counter clockwise rotation
        translate = matrixCreated.transform( nuke.math.Vector3(0,0,0) )  # get a vector that represents the camera translation   
        rotate = matrixCreated.rotationsZXY() # give us xyz rotations from cam matrix (must be converted to degrees)
    
        cam['translate'].setValueAt( float(translate.x), frame, 0 )
        cam['translate'].setValueAt( float(translate.y), frame, 1 )
        cam['translate'].setValueAt( float(translate.z), frame, 2 )
        cam['rotate'].setValueAt( float( math.degrees( rotate[0] ) ), frame, 0 )
        cam['rotate'].setValueAt( float( math.degrees( rotate[1] ) ), frame, 1 ) 
        cam['rotate'].setValueAt( float( math.degrees( rotate[2] ) ), frame, 2 ) 
    
        task.setProgress( int( float(curTask) / fRange.frames() * 100 ) )

node = None
try:
    node = nuke.selectedNode()
except:
    nuke.critical( 'No node selected! Please select a read node with EXR metadata from VRay!' )

if node is not None:
    createExrCamRS( node )