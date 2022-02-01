import nuke
import DeadlineGlobals

def L_sanityChecks():
    DeadlineGlobals.initMemoryUsage = 25000
    DeadlineGlobals.initBatchMode = True
    DeadlineGlobals.initUseNukeX = False
    DeadlineGlobals.initReloadPlugin = True

    DeadlineGlobals.initSelectedOnly = True
    DeadlineGlobals.initConcurrentTasks = 2   

    writenames = []

    selectedWrites = nuke.selectedNodes()

    if selectedWrites:
        for n in selectedWrites:
            writenames.append(n.name())

        for write in nuke.allNodes("Write"):
            if write not in selectedWrites:
                write.knob("disable").setValue(True)

        # print("selected Nodes are: " + str(writenames))

        DeadlineGlobals.initExtraInfo0 = writenames

    if len(selectedWrites) == 1:
        write = selectedWrites[0]
        if write.knob('use_limit').getValue():
            DeadlineGlobals.initFrameList = str(int(write.knob('first').getValue())) + '-' + str(int(write.knob('last').getValue()))


    return True