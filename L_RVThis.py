import nuke
import nukescripts
import subprocess
import os
import sys
import re


def RVThis(selectedNodes):
    args = ''
    args += '-fps "%s" ' % (str(int(nuke.root().knob('fps').value())))

    if len(selectedNodes) == 2:
        args += "-over "

    for n in selectedNodes:
        name = n.knob('file').value()
        name = re.sub(r"%", r"%%", name)

        colorspace = n.knob('colorspace').value()

        if colorspace.startswith("default"):
            colorspace = colorspace[9:-1]

        if colorspace == 'rec709':
            colorspace = 'Output - rec.709'

        if colorspace == 'sRGB':
            colorspace = 'Output - sRGB'

        args += '%s ' % (name)

    viewspace = nuke.activeViewer().node().knob('viewerProcess').value()
    if viewspace.endswith(" (ACES)"):
        viewspace = viewspace[0:-7]

    openRV(args, colorspace, viewspace)


def openRV(args, colorspace, viewspace):

    env = os.environ.copy()

    env["COLORSPACE"] = colorspace
    env["DISPLAY"] = viewspace

    call = 'RV.bat %s' % (args)
    nuke.tprint("### CALL RV ###")
    nuke.tprint('CMD: ' + call)
    nuke.tprint('CLR: ' + colorspace)
    nuke.tprint('VWR: ' + viewspace)
    nuke.tprint("### CALL RV END ###")
    subprocess.Popen(call, env=env)
