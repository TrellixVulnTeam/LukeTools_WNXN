import nuke
import nukescripts
import subprocess

def djvViewThis(selectedNodes):
    filename = ""
    for n in selectedNodes:
        name = n.knob('file').value()
        name = nukescripts.replaceHashes(name) % n.knob('first').value()

        filename += name + " "
    openDjvView(filename)

def openDjvView(filename):

    call = 'C:\\Program Files\\DJV2\\bin\\djv.exe %s' %(filename)
    print call
    subprocess.Popen(call)
