import nuke
import os
import platform
import subprocess

def openPath(path):
    if os.path.exists(path):

        operatingSystem = platform.system()

        if operatingSystem == "Windows":
            os.startfile(path.replace('/','\\'))
        elif operatingSystem == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])

def openInFileBrowser():

    if len(nuke.selectedNodes()) == 0:
        path =  os.path.dirname(nuke.root().name())
        openPath(path)

    for i in nuke.selectedNodes():
        path =  os.path.dirname(i.knob('file').value())
        openPath(path)