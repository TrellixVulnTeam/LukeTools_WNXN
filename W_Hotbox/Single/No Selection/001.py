#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Jump to Viewed
# COLOR: #335152
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('selected').setValue(False)

activeViewer = nuke.activeViewer()

activeViewer.node().input(activeViewer.activeInput()).knob('selected').setValue(True)

nuke.zoomToFitSelected()