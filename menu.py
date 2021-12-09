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
    nuke.knobDefault('Root.workingSpaceLUT', "acescg")
    nuke.knobDefault('Root.int8Lut', "out_srgb")
    nuke.knobDefault('Root.int16Lut', "out_srgb")
    nuke.knobDefault('Root.logLut', "logc3ei800_alexawide")
    nuke.knobDefault('Root.floatLut', "acescg")

    nuke.knobDefault('Root.format', "HD_1080")
    nuke.knobDefault('Root.fps', "25")
    nuke.knobDefault('Root.first_frame', "1001")
    nuke.knobDefault('Root.last_frame', "1100")
    nuke.knobDefault('Root.lock_range', "1")

    nuke.knobDefault('Write.create_directories', "1")
    nuke.knobDefault('Write.file_type', "exr")
    nuke.knobDefault('Write.write_full_layer_names', "1")
    nuke.knobDefault('Write.standard layer name format', "1")

    # nuke.menu("Nodes").addCommand("3DE4/LD_3DE4_Anamorphic_Standard_Degree_4", "nuke.createNode('LD_3DE4_Anamorphic_Standard_Degree_4')")
    # nuke.menu("Nodes").addCommand("3DE4/LD_3DE4_Anamorphic_Rescaled_Degree_4", "nuke.createNode('LD_3DE4_Anamorphic_Rescaled_Degree_4')")
    # nuke.menu("Nodes").addCommand("3DE4/LD_3DE4_Anamorphic_Degree_6", "nuke.createNode('LD_3DE4_Anamorphic_Degree_6')")
    # nuke.menu("Nodes").addCommand("3DE4/LD_3DE4_Radial_Standard_Degree_4", "nuke.createNode('LD_3DE4_Radial_Standard_Degree_4')")
    # nuke.menu("Nodes").addCommand("3DE4/LD_3DE4_Radial_Fisheye_Degree_8", "nuke.createNode('LD_3DE4_Radial_Fisheye_Degree_8')")
    # nuke.menu("Nodes").addCommand("3DE4/LD_3DE_Classic_LD_Model", "nuke.createNode('LD_3DE_Classic_LD_Model')")


# knobDefaults

nuke.knobDefault('Roto.cliptype', "0")
nuke.knobDefault('Merge.bbox', "B")
nuke.knobDefault('ChannelMerge.bbox', "union")
nuke.knobDefault('Copy.bbox', "B side")

nuke.menu('Nuke').addCommand('Luke/create Read', "L_createRead.createReadFromWrite()", "shift+r")

nuke.menu('Nuke').addCommand('Luke/Open in File Browser',
                             "L_openInFileBrowser.openInFileBrowser()", "ctrl+shift+e")

# import L_djvViewThis
# nuke.menu( 'Nuke' ).addCommand( 'Luke/DJV this', "L_djvViewThis.djvViewThis(nuke.selectedNodes())", "ctrl+shift+d")


# Menues
lukeGizmosMenu = nuke.toolbar("Nodes").addMenu("Luke")

# Gizmos
# lukeGizmosMenu.addCommand("L_AdvancedGrain", "nuke.createNode('L_AdvancedGrain')", '')
# lukeGizmosMenu.addCommand("L_expoglow", "nuke.createNode('L_expoglow')", '')
# lukeGizmosMenu.addCommand("L_UnsharpMask", "nuke.createNode('L_UnsharpMask')", '')
# lukeGizmosMenu.addCommand("L_GradMagic", "nuke.createNode('L_gradmagic')", '')
# lukeGizmosMenu.addCommand("L_DespillMadness", "nuke.createNode('L_DespillMadness')", '')
# lukeGizmosMenu.addCommand("L_LUE4NUKE", "nuke.createNode('L_LUE4NUKE')", '')
# lukeGizmosMenu.addCommand("L_GradientEditor", "nuke.createNode('h_gradienteditor')", '')
# lukeGizmosMenu.addCommand("L_Deflicker_Velocity", "nuke.createNode('L_Deflicker_Velocity')", '')
# lukeGizmosMenu.addCommand("L_LensKernel", "nuke.createNode('L_LensKernel')", '')
# lukeGizmosMenu.addCommand("L_OpticalZDefocus", "nuke.createNode('L_OpticalZDefocus')", '')
# lukeGizmosMenu.addCommand("L_aPMatte", "nuke.createNode('L_aPMatte')", '')

# lukeGizmosMenu.addCommand("EdgeExtend/L_KeyEdgeExtend", "nuke.createNode('L_KeyEdgeExtend')", '')
# lukeGizmosMenu.addCommand("EdgeExtend/L_FillSampler", "nuke.createNode('L_FillSampler')", '')
# lukeGizmosMenu.addCommand("EdgeExtend/L_Pixelspread", "nuke.createNode('L_Pixelspread')", '')

# lukeGizmosMenu.addCommand("P_Matte", "nuke.createNode('P_Matte')", '')

# lukeGizmosMenu.addCommand("X_Tools/L_X_Aton", "nuke.createNode('L_X_Aton')", '')
# lukeGizmosMenu.addCommand("X_Tools/L_X_Distort", "nuke.createNode('L_X_Distort')", '')
# lukeGizmosMenu.addCommand("X_Tools/L_X_Tesla", "nuke.createNode('L_X_Tesla')", '')

# lukeGizmosMenu.addCommand('bm/L_bm_OpticalGlow', 'nuke.createNode("L_bm_OpticalGlow")', icon="bm_OpticalGlow_icon.png")
# lukeGizmosMenu.addCommand('bm/L_bm_Lightwrap', 'nuke.createNode("L_bm_Lightwrap")', icon="bm_Lightwrap_icon.png")
# lukeGizmosMenu.addCommand('bm/L_bm_NoiseGen', 'nuke.createNode("L_bm_NoiseGen")', icon="bm_NoiseGen_icon.png")
# lukeGizmosMenu.addCommand('bm/L_bm_CurveRemapper', 'nuke.createNode("L_bm_CurveRemapper")', icon="bm_CurveRemapper_icon.png")
# lukeGizmosMenu.addCommand('bm/L_bm_CameraShake', 'nuke.createNode("L_bm_CameraShake")', icon="bm_CameraShake_icon.png")
# lukeGizmosMenu.addCommand('bm/L_bm_EdgeMatte', 'nuke.createNode("L_bm_EdgeMatte")', icon="BlackOutside.png")
# lukeGizmosMenu.addCommand('bm/L_bm_MatteCheck', 'nuke.createNode("L_bm_MatteCheck")', icon="bm_MatteCheck_icon.png")

# lukeGizmosMenu.addCommand('L_AutoFlare', 'nuke.createNode("AutoFlare2")')


lukeGizmosMenu.addCommand("sb Backdrop", 'sb_backdrop.sb_backdrop()', 'alt+b')

nuke.menu('Nuke').findItem('Edit').addCommand('HotBox', 'channel_hotbox.start()', 'alt+v')

nuke.menu('Nuke').addCommand('Luke/Make connector', "labelConnector.makeConnector()",
                             'F9')  # also renames an existing connector
nuke.menu('Nuke').addCommand('Luke/Connect connectors', "labelConnector.runLabelMatch()",
                             'F8')  # standard run to match labels, connect nodes, or make new connections
nuke.menu('Nuke').addCommand('Luke/Force Connect connectors', "labelConnector.runLabelMatch(forceShowUi = True)",
                             'ctrl+F8')  # force show UI to make new connection when a single Node is selected


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

nuke.pluginAddPath('./NukeSurvivalToolkit')
