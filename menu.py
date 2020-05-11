nuke.tprint('LukeTools menu.py')

import nukescripts

if __lukescripts_local__:
    nuke.tprint('local LukeTools menu.py')
    import L_newProject
    nuke.menu( 'Nuke' ).addCommand( 'Luke/new Project', "L_newProject.L_newProject()")

    import L_callbacks
    nuke.addOnCreate(L_callbacks.writeNodeFields, nodeClass= "Write")

#knobDefaults
nuke.knobDefault('Roto.cliptype', "0")
nuke.knobDefault('Merge.bbox', "B")
nuke.knobDefault('Write.create_directories', "1")
nuke.knobDefault('Write.file_type', "exr")

#Menues
lukeGizmosMenu = nuke.toolbar("Nodes").addMenu( "Luke" )

#Gizmos
lukeGizmosMenu.addCommand("AdvancedGrain", "nuke.createNode('AdvancedGrain')", '')
lukeGizmosMenu.addCommand("expoglow", "nuke.createNode('expoglow')", '')
lukeGizmosMenu.addCommand("UnsharpMask", "nuke.createNode('UnsharpMask')", '')
lukeGizmosMenu.addCommand("GradMagic", "nuke.createNode('gradmagic')", '')
lukeGizmosMenu.addCommand("DespillMadness", "nuke.createNode('DespillMadness')", '')
lukeGizmosMenu.addCommand("KeyEdgeExtend", "nuke.createNode('KeyEdgeExtend')", '')

import pixelfudger

import sb_backdrop
lukeGizmosMenu.addCommand("sb Backdrop", 'sb_backdrop.sb_backdrop()', '')

#Tools
import channel_hotbox
nuke.menu('Nuke').findItem('Edit').addCommand('HotBox', 'channel_hotbox.start()', 'alt+v')

import labelConnector
nuke.menu( 'Nuke' ).addCommand( 'Luke/Label connector', "labelConnector.runLabelMatch()", 'ctrl+shift+y' )

import AnimationMaker  

import W_hotbox, W_hotboxManager

#searchReplacePanel
import SearchReplacePanel

def addSRPanel():
        '''Run the panel script and add it as a tab into the pane it is called from'''
        myPanel = SearchReplacePanel.SearchReplacePanel()
        return myPanel.addToPane()
 
#THIS LINE WILL ADD THE NEW ENTRY TO THE PANE MENU
nuke.menu('Pane').addCommand('SearchReplace', addSRPanel)
 
#THIS LINE WILL REGISTER THE PANEL SO IT CAN BE RESTORED WITH LAYOUTS
nukescripts.registerPanel('com.ohufx.SearchReplace', addSRPanel)
#searchReplacePanelEnd

import knob_scripter

import RetimeCamera
nuke.menu( 'Nuke' ).addCommand( 'Luke/Retime Camera', 'RetimeCamera.create_RCPanel()')

# custom Drag and Drop Handler
import L_dragDropHandler
nukescripts.drop.addDropDataCallback(L_dragDropHandler.dropHandler)
