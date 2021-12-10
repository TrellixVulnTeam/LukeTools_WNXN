import nuke
import DeadlineGlobals

def RunSanityCheck():



    DeadlineGlobals.initMemoryUsage = 25000
    DeadlineGlobals.initBatchMode = True
    DeadlineGlobals.initUseNukeX = False
    DeadlineGlobals.initReloadPlugin = True

    DeadlineGlobals.initSelectedOnly = True

    writenames = []

    for n in nuke.selectedNodes():
        writenames.append(n.name())

    # print("selected Nodes are: " + str(writenames))

    DeadlineGlobals.initExtraInfo0 = writenames

    return True
