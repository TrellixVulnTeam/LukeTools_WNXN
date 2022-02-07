import nuke
import nukescripts
# import pythonlibrary.L_pyseq as L_pyseq


def createReadFromWrite():
    for node in nuke.selectedNodes():

        file = ''
        start = ''
        end = ''

        if node.Class() == 'Write':
            if node["file"].value():
                file = node["file"].value()
                if node.knob('use_limit').getValue():
                    start = int(node.knob('first').getValue())
                    end = int(node.knob('last').getValue())

            else:
                nuke.message(node.name() + ': No valid filepath')

        if node.Class() == 'NoOp' and 'ffmpeg_write' in node.name():
            if node["outPreview"].value():
                file = node["outPreview"].value()

            else:
                nuke.message(node.name() + ': No valid filepath')

        if file:

            # if file[-4:] in ['.mov', '.mp4']:

            #     read = nuke.createNode("Read","file {"+file+"}", inpanel= False)
            #     read.knob('colorspace').setValue('out_srgb')
            #     read.knob('xpos').setValue(node.xpos()+0)
            #     read.knob('ypos').setValue(node.ypos()+100)
            #     read.knob('localizationPolicy').setValue(3)

            # else:
            # seq = L_pyseq.img2pyseq(file)

            # if seq:
            #     read = nuke.nodes.Read(file=file,
            #                                 xpos=node.xpos()+0,
            #                                 ypos=node.ypos()+100,
            #                                 first=seq.start(),
            #                                 last=seq.end(),
            #                                 origfirst = seq.start(),
            #                                 origlast= seq.end())

            #     read.knob('colorspace').setValue(int(node.knob('colorspace').getValue()))
            #     read.knob('localizationPolicy').setValue(3)

            # else:
            read = nuke.nodes.Read(file=file,
                                   xpos=node.xpos()+0,
                                   ypos=node.ypos()+100,
                                   first=start or nuke.root().knob('first_frame').getValue(),
                                   last=end or nuke.root().knob('last_frame').getValue(),
                                   origfirst=nuke.root().knob('first_frame').getValue(),
                                   origlast=nuke.root().knob('last_frame').getValue())

            read.knob('colorspace').setValue(int(node.knob('colorspace').getValue()))
            read.knob('localizationPolicy').setValue(3)
