import nuke
import DeadlineGlobals


def L_sanityChecks():
    DeadlineGlobals.initMemoryUsage = 25000
    DeadlineGlobals.initBatchMode = True
    DeadlineGlobals.initUseNukeX = True
    DeadlineGlobals.initReloadPlugin = False
    DeadlineGlobals.initSelectedOnly = False

    DeadlineGlobals.initConcurrentTasks = 2

    writenames = []

    selectedWrites = nuke.selectedNodes("Write")

    # if selectedWrites:
    #     DeadlineGlobals.initSelectedOnly = True

    for writeGeo in nuke.allNodes('WriteGeo'):
        writeGeo.knob("disable").setValue(True)

    if selectedWrites:
        for n in selectedWrites:
            writenames.append(n.name())
            n.knob("disable").setValue(False)

        for write in nuke.allNodes("Write"):
            if write not in selectedWrites:
                write.knob("disable").setValue(True)

        # print("selected Nodes are: " + str(writenames))

    else:
        for write in nuke.allNodes("Write"):
            if not write.knob("disable").getValue():
                writenames.append(write.name())

    DeadlineGlobals.initExtraInfo0 = ', '.join(writenames)

    if len(selectedWrites) == 1:
        write = selectedWrites[0]
        if write.knob('use_limit').getValue():
            DeadlineGlobals.initFrameList = str(int(write.knob('first').getValue())) + '-' + str(int(write.knob('last').getValue()))

    return True
