import nuke
import DeadlineGlobals

def L_sanityChecks():
    DeadlineGlobals.initMemoryUsage = 25000
    DeadlineGlobals.initBatchMode = True
    DeadlineGlobals.initUseNukeX = False
    DeadlineGlobals.initReloadPlugin = True

    DeadlineGlobals.initSelectedOnly = True

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

    return True