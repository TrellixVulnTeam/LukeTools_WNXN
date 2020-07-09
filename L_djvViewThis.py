import nuke
import nukescripts
import subprocess

def djvViewThis(selectedNodes):
    filename = ''
    for n in selectedNodes:
        name = n.knob('file').value()
        if "%0" in name:
            name = nukescripts.replaceHashes(name) % n.knob('first').value()
        
        colorspace = n.knob('colorspace').value()

        filename += '"%s" -ocio_image "%s" ' %(name, colorspace)
    openDjvView(filename)

def openDjvView(filename):

    call = 'C:\\Program Files\\DJV2\\bin\\djv.exe %s' %(filename)
    print call
    subprocess.Popen(call)
