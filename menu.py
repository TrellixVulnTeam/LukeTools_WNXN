import convertGizmosToGroups
import sb_convertCornerPin
import W_hotboxManager
import W_hotbox
import AnimationMaker
import AlignDots
import L_dragDropHandler
import L_ToolSets
import RetimeCamera
import SearchReplacePanel
import labelConnector
import channel_hotbox
import sb_backdrop
import pixelfudger
import L_openInFileBrowser
import L_createRead
import nukescripts
import nuke

nuke.tprint('LukeTools menu.py')

if __lukescripts_local__:
    nuke.tprint('local LukeTools menu.py')
    import L_newProject
    nuke.menu('Nuke').addCommand('Luke/new Project', "L_newProject.L_newProject()")

    import L_callbacks

    nuke.addKnobChanged(L_callbacks.updateWriteNameCallback, nodeClass="Write")
    nuke.addOnCreate(L_callbacks.writeNodeFields, nodeClass="Write")
    nuke.addOnScriptSave(L_callbacks.updateAllWriteNames)

    # knobDefaults local
    # nuke.knobDefault('Root.workingSpaceLUT', "acescg")
    # nuke.knobDefault('Root.int8Lut', "out_srgb")
    # nuke.knobDefault('Root.int16Lut', "out_srgb")
    # nuke.knobDefault('Root.logLut', "logc3ei800_alexawide")
    # nuke.knobDefault('Root.floatLut', "acescg")

    nuke.knobDefault('Root.format', "HD_1080")
    nuke.knobDefault('Root.fps', "25")
    nuke.knobDefault('Root.first_frame', "1001")
    nuke.knobDefault('Root.last_frame', "1100")
    nuke.knobDefault('Root.lock_range', "1")

    nuke.knobDefault('Write.create_directories', "1")
    nuke.knobDefault('Write.file_type', "exr")
    nuke.knobDefault('Write.write_full_layer_names', "1")
    nuke.knobDefault('Write.standard layer name format', "1")

# knobDefaults

nuke.knobDefault('Roto.cliptype', "0")
nuke.knobDefault('Merge.bbox', "B")
nuke.knobDefault('ChannelMerge.bbox', "union")
nuke.knobDefault('Copy.bbox', "B side")

nuke.menu('Nuke').addCommand('Luke/create Read', "L_createRead.createReadFromWrite()", "shift+r", shortcutContext=2)

nuke.menu('Nuke').addCommand('Luke/Open in File Browser',
                             "L_openInFileBrowser.openInFileBrowser()", "ctrl+shift+e")

# Menues
lukeGizmosMenu = nuke.toolbar("Nodes").addMenu("Luke")

lukeGizmosMenu.addCommand("sb Backdrop", 'sb_backdrop.sb_backdrop()', 'alt+b', shortcutContext=2)

nuke.menu('Nuke').findItem('Edit').addCommand('HotBox', 'channel_hotbox.start()', 'alt+v')

nuke.menu('Nuke').addCommand('Luke/Make connector', "labelConnector.makeConnector()",
                             'alt+shift+A', shortcutContext=2)  # also renames an existing connector
nuke.menu('Nuke').addCommand('Luke/Connect connectors', "labelConnector.runLabelMatch()",
                             'A', shortcutContext=2)  # standard run to match labels, connect nodes, or make new connections
nuke.menu('Nuke').addCommand('Luke/Force Connect connectors', "labelConnector.runLabelMatch(forceShowUi = True)",
                             'alt+A', shortcutContext=2)  # force show UI to make new connection when a single Node is selected


def addSRPanel():
    '''Run the panel script and add it as a tab into the pane it is called from'''
    myPanel = SearchReplacePanel.SearchReplacePanel()
    return myPanel.addToPane()


nuke.menu('Pane').addCommand('SearchReplace', addSRPanel)
nukescripts.registerPanel('com.ohufx.SearchReplace', addSRPanel)

# currently no Nuke 13 support
# import knob_scripter

lukeGizmosMenu.addCommand('Retime Camera', 'RetimeCamera.create_RCPanel()')

L_ToolSets.createToolsetsMenu(nuke.menu("Nodes"))

nuke.menu('Nuke').findItem('Edit').findItem('Extract').setShortcut('e')

# drag n drop handler
nukescripts.drop.addDropDataCallback(L_dragDropHandler.dropHandler)

nuke.menu('Nuke').addCommand('Luke/Align Dots', "AlignDots.AlignDots()", "alt+.", shortcutContext=2)

lukeGizmosMenu.addCommand('Luke/sb_convertCornerPin', "sb_convertCornerPin.sb_convertCornerPin()")

lukeGizmosMenu.addCommand('Luke/convertGizmosToGroups', "convertGizmosToGroups.convertGizmosToGroups()")

nuke.pluginAddPath('./NukeSurvivalToolkit')

nuke.pluginAddPath('./Deadline')

menuBar = nuke.menu("Nuke")

import W_smartAlign

menuBar.addCommand("Edit/Node/Align/Left", 'W_smartAlign.alignNodes("left")', "shift+left", shortcutContext=2)
menuBar.addCommand("Edit/Node/Align/Right", 'W_smartAlign.alignNodes("right")', "shift+right", shortcutContext=2)
menuBar.addCommand("Edit/Node/Align/Up", 'W_smartAlign.alignNodes("up")', "shift+up", shortcutContext=2)
menuBar.addCommand("Edit/Node/Align/Down", 'W_smartAlign.alignNodes("down")', "shift+down", shortcutContext=2)

import L_moveNodes

menuBar.addCommand("Edit/Node/Move/Left", 'L_moveNodes.moveSel_left()', "ctrl+alt+left", shortcutContext=2)
menuBar.addCommand("Edit/Node/Move/Right", 'L_moveNodes.moveSel_right()', "ctrl+alt+right", shortcutContext=2)
menuBar.addCommand("Edit/Node/Move/Up", 'L_moveNodes.moveSel_up()', "ctrl+alt+up", shortcutContext=2)
menuBar.addCommand("Edit/Node/Move/Down", 'L_moveNodes.moveSel_down()', "ctrl+alt+down", shortcutContext=2)

menuBar.addCommand("Edit/Node/Move/Left (large)", 'L_moveNodes.moveSel_left(large = True)', "ctrl+shift+left", shortcutContext=2)
menuBar.addCommand("Edit/Node/Move/Right (large)", 'L_moveNodes.moveSel_right(large = True)', "ctrl+shift+right", shortcutContext=2)
menuBar.addCommand("Edit/Node/Move/Up (large)", 'L_moveNodes.moveSel_up(large = True)', "ctrl+shift+up", shortcutContext=2)
menuBar.addCommand("Edit/Node/Move/Down (large)", 'L_moveNodes.moveSel_down(large = True)', "ctrl+shift+down", shortcutContext=2)
