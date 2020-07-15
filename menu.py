nuke.tprint('LukeTools menu.py')

import nukescripts

if __lukescripts_local__:
    nuke.tprint('local LukeTools menu.py')
    import L_newProject
    nuke.menu( 'Nuke' ).addCommand( 'Luke/new Project', "L_newProject.L_newProject()")

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

    nuke.knobDefault('Write.create_directories', "1")
    nuke.knobDefault('Write.file_type', "exr")


# knobDefaults

nuke.knobDefault('Roto.cliptype', "0")
nuke.knobDefault('Merge.bbox', "B")

import L_createRead
nuke.menu( 'Nuke' ).addCommand( 'Luke/create Read', "L_createRead.createReadFromWrite()", "shift+r")


#Menues
lukeGizmosMenu = nuke.toolbar("Nodes").addMenu( "Luke" )

#Gizmos
lukeGizmosMenu.addCommand("L_AdvancedGrain", "nuke.createNode('L_AdvancedGrain')", '')
lukeGizmosMenu.addCommand("L_expoglow", "nuke.createNode('L_expoglow')", '')
lukeGizmosMenu.addCommand("L_UnsharpMask", "nuke.createNode('L_UnsharpMask')", '')
lukeGizmosMenu.addCommand("L_GradMagic", "nuke.createNode('L_gradmagic')", '')
lukeGizmosMenu.addCommand("L_DespillMadness", "nuke.createNode('L_DespillMadness')", '')
lukeGizmosMenu.addCommand("L_LUE4NUKE", "nuke.createNode('L_LUE4NUKE')", '')
lukeGizmosMenu.addCommand("L_GradientEditor", "nuke.createNode('h_gradienteditor')", '')
lukeGizmosMenu.addCommand("L_Deflicker_Velocity", "nuke.createNode('L_Deflicker_Velocity')", '')
lukeGizmosMenu.addCommand("L_LensKernel", "nuke.createNode('L_LensKernel')", '')

lukeGizmosMenu.addCommand("EdgeExtend/L_KeyEdgeExtend", "nuke.createNode('L_KeyEdgeExtend')", '')
lukeGizmosMenu.addCommand("EdgeExtend/L_FillSampler", "nuke.createNode('L_FillSampler')", '')
lukeGizmosMenu.addCommand("EdgeExtend/L_Pixelspread", "nuke.createNode('L_Pixelspread')", '')

lukeGizmosMenu.addCommand("X_Tools/L_X_Aton", "nuke.createNode('L_X_Aton')", '')
lukeGizmosMenu.addCommand("X_Tools/L_X_Distort", "nuke.createNode('L_X_Distort')", '')
lukeGizmosMenu.addCommand("X_Tools/L_X_Tesla", "nuke.createNode('L_X_Tesla')", '')

lukeGizmosMenu.addCommand('bm/L_bm_OpticalGlow', 'nuke.createNode("L_bm_OpticalGlow")', icon="bm_OpticalGlow_icon.png")
lukeGizmosMenu.addCommand('bm/L_bm_Lightwrap', 'nuke.createNode("L_bm_Lightwrap")', icon="bm_Lightwrap_icon.png")
lukeGizmosMenu.addCommand('bm/L_bm_NoiseGen', 'nuke.createNode("L_bm_NoiseGen")', icon="bm_NoiseGen_icon.png")
lukeGizmosMenu.addCommand('bm/L_bm_CurveRemapper', 'nuke.createNode("L_bm_CurveRemapper")', icon="bm_CurveRemapper_icon.png")
lukeGizmosMenu.addCommand('bm/L_bm_CameraShake', 'nuke.createNode("L_bm_CameraShake")', icon="bm_CameraShake_icon.png")
lukeGizmosMenu.addCommand('bm/L_bm_EdgeMatte', 'nuke.createNode("L_bm_EdgeMatte")', icon="BlackOutside.png")
lukeGizmosMenu.addCommand('bm/L_bm_MatteCheck', 'nuke.createNode("L_bm_MatteCheck")', icon="bm_MatteCheck_icon.png")

import pixelfudger

import sb_backdrop
lukeGizmosMenu.addCommand("sb Backdrop", 'sb_backdrop.sb_backdrop()', '')

import channel_hotbox
nuke.menu('Nuke').findItem('Edit').addCommand('HotBox', 'channel_hotbox.start()', 'alt+v')

import labelConnector
nuke.menu( 'Nuke' ).addCommand( 'Luke/Label connector', "labelConnector.runLabelMatch()", 'ctrl+shift+y' )

import AnimationMaker  

import W_hotbox, W_hotboxManager

import SearchReplacePanel
def addSRPanel():
        '''Run the panel script and add it as a tab into the pane it is called from'''
        myPanel = SearchReplacePanel.SearchReplacePanel()
        return myPanel.addToPane()
 
nuke.menu('Pane').addCommand('SearchReplace', addSRPanel)
nukescripts.registerPanel('com.ohufx.SearchReplace', addSRPanel)

import knob_scripter

import RetimeCamera
nuke.menu( 'Nuke' ).addCommand( 'Luke/Retime Camera', 'RetimeCamera.create_RCPanel()')

import ColorGradientUi

import L_ToolSets
L_ToolSets.createToolsetsMenu(nuke.menu("Nodes"))