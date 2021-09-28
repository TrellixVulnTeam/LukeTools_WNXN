import nuke
import nukescripts
import subprocess
import os
import sys
import re

def RVThis(selectedNodes):
    args = ''
    args += '-fps "%s" ' %(str(int(nuke.root().knob('fps').value())))

    for n in selectedNodes:
        name = n.knob('file').value()
        name = re.sub(r"%",r"%%",name)
        
        colorspace = n.knob('colorspace').value()

        if 'default (' in colorspace:
            colorspace = colorspace[9:-1]

        if colorspace == 'rec709':
            colorspace = 'Output - rec.709'

        if colorspace == 'sRGB':
            colorspace = 'Output - sRGB'

        args += '%s ' %(name)

    openRV(args, colorspace)

def openRV(args, colorspace):

    env = os.environ.copy()

    env["COLORSPACE"] = colorspace

    call = 'RV.bat %s' %(args)
    print(call)
    print(colorspace)
    subprocess.Popen(call, env=env)
