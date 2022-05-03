import nuke
import DeadlineGlobals


def L_sanityChecks():
    DeadlineGlobals.initMemoryUsage = 25000
    DeadlineGlobals.initBatchMode = True
    DeadlineGlobals.initUseNukeX = True
    DeadlineGlobals.initReloadPlugin = False
    DeadlineGlobals.initSelectedOnly = False
    DeadlineGlobals.initSubmitScene = True
    DeadlineGlobals.initUseGpu = True
    DeadlineGlobals.initConcurrentTasks = 2
    DeadlineGlobals.initContinueOnError = False

    writenames = []
    fileouttest = []
    renderNodes = []

    selectedWrites = nuke.selectedNodes("Write")

    for write in nuke.allNodes('Write'):
        file = write.knob('file').value()
        if file not in fileouttest:
            fileouttest.append(file)
        else:
            nuke.message("Double Write out! \n\n%s\n%s" % (write.name(),file))

    for writeGeo in nuke.allNodes('WriteGeo'):
        writeGeo.knob("disable").setValue(True)

    if selectedWrites:
        for n in selectedWrites:
            writenames.append(n.name())
            n.knob("disable").setValue(False)
            renderNodes.append(n)

        for write in nuke.allNodes("Write"):
            if write not in selectedWrites:
                write.knob("disable").setValue(True)

        # print("selected Nodes are: " + str(writenames))

    else:
        for write in nuke.allNodes("Write"):
            if not write.knob("disable").getValue():
                writenames.append(write.name())
                renderNodes.append(write)


    DeadlineGlobals.initExtraInfo0 = ', '.join(writenames)

    commonStartEndFrame = True

    startframe = renderNodes[0].knob('first').getValue()
    endframe  = renderNodes[0].knob('last').getValue()

    for n in renderNodes:
        if n.knob('first').getValue() != startframe or n.knob('last').getValue() != endframe or n.knob('use_limit').getValue() == False:
            commonStartEndFrame = False
            break
        
    if commonStartEndFrame:
        DeadlineGlobals.initFrameList = str(int(startframe)) + '-' + str(int(endframe))

    return True
