import nuke
import nukescripts
import subprocess

def djvViewThis(selectedNodes):
    args = ''
    for n in selectedNodes:
        name = n.knob('file').value()
        if "%0" in name:
            name = nukescripts.replaceHashes(name) % n.knob('first').value()
        
        colorspace = n.knob('colorspace').value()

        if 'default (' in colorspace:
            colorspace = colorspace[9:-1]

        args += '"%s" -ocio_image "%s" ' %(name, colorspace)

    args += '-speed "%s"' %(str(int(nuke.root().knob('fps').value())))
    args += ' -frame "%s"' %(str(nuke.frame()))
    openDjvView(args)

def openDjvView(args):

    call = 'djv %s' %(args)
    print(call)
    subprocess.Popen(call)
