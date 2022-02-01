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

        if colorspace.startswith("default"):
            colorspace = colorspace[9:-1]

        if colorspace == 'rec709':
            colorspace = 'Output - rec.709'

        if colorspace == 'sRGB':
            colorspace = 'Output - sRGB'
        
        viewspace = nuke.root().knob('monitorOutLUT').value()

        viewspace = viewspace.replace(' (ACES)','')

        args += '%s ' %(name)

    openRV(args, colorspace, viewspace)

def openRV(args, colorspace, viewspace):

    env = os.environ.copy()

    env["COLORSPACE"] = colorspace
    env["DISPLAY"] = viewspace

    call = 'RV.bat %s' %(args)
    nuke.tprint("### CALL RV ###")
    nuke.tprint(call)
    nuke.tprint(colorspace)
    nuke.tprint(viewspace)
    nuke.tprint("### CALL RV END ###")
    subprocess.Popen(call, env=env)
