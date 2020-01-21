nuke.tprint('LukeTools menu.py')

#knobDefaults
nuke.knobDefault('Roto.cliptype', "0")
nuke.knobDefault('Merge.bbox', "B")

#Menues
lukeGizmosMenu = nuke.toolbar("Nodes").addMenu( "Luke" )

#Gizmos
lukeGizmosMenu.addCommand("AdvancedGrain", "nuke.createNode('AdvancedGrain')", '')
lukeGizmosMenu.addCommand("expoglow", "nuke.createNode('expoglow')", '')
lukeGizmosMenu.addCommand("GradMagic", "nuke.createNode('gradmagic')", '')
lukeGizmosMenu.addCommand("DespillMadness", "nuke.createNode('DespillMadness')", '')
lukeGizmosMenu.addCommand("KeyEdgeExtend", "nuke.createNode('KeyEdgeExtend')", '')

import pixelfudger

import sb_backdrop
lukeGizmosMenu.addCommand("sb Backdrop", 'sb_backdrop.sb_backdrop()', '')


#Tools
import channel_hotbox
nuke.menu('Nuke').findItem('Edit').addCommand('HotBox', 'channel_hotbox.start()', 'shift+v')

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