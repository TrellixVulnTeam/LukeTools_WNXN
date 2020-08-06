import nuke
import os
import platform
import subprocess

def openInFileBrowser():

    operatingSystem = platform.system()

    for i in nuke.selectedNodes():

        path =  os.path.dirname(i.knob('file').value())

        if os.path.exists(path):

            if operatingSystem == "Windows":
                os.startfile(path.replace('/','\\'))
            elif operatingSystem == "Darwin":
                subprocess.Popen(["open", path])
            else:
                subprocess.Popen(["xdg-open", path])