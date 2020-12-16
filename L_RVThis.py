import nuke
import nukescripts
import subprocess
import os
import sys

def RVThis(selectedNodes):
    args = ''
    args += '-fps "%s" ' %(str(int(nuke.root().knob('fps').value())))


    for n in selectedNodes:
        name = n.knob('file').value()
        # if "%0" in name:
        #     name = nukescripts.replaceHashes(name) % n.knob('first').value()
        
        colorspace = n.knob('colorspace').value()

        if 'default (' in colorspace:
            colorspace = colorspace[9:-1]

        # args += '"%s" -ocio_image "%s" ' %(name, colorspace)
        args += name + " "

    # args += ' -frame "%s"' %(str(nuke.frame()))
    openRV(args, colorspace)

def openRV(args, colorspace):

    env = os.environ.copy()

    env["COLORSPACE"] = colorspace

    call = 'rv.bat %s' %(args)
    print call
    print colorspace
    subprocess.Popen(call, env=env)
