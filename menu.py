import convertGizmosToGroups
import sb_convertCornerPin
import W_hotboxManager
import W_hotbox
import AlignDots

import labelConnector
import channel_hotbox
import sb_backdrop

import nukescripts

####################################################################################
# ADD THIS TO YOUR meu.py IN YOUR .nuke FODLER
# nuke.pluginAddPath('PATH_TO_THIS_FOLDER')
####################################################################################

####################################################################################
# WENN DU NUR DAS NST WILLST, SCHMEISS ALLES WEG AUSSER DIE ZWEI HIER
####################################################################################
import nuke
nuke.pluginAddPath('./NukeSurvivalToolkit')


nuke.tprint('LukeTools menu.py')
# nuke.knobDefault('Roto.cliptype', "0")
# nuke.knobDefault('RotoPaint.cliptype', "0")
# nuke.knobDefault('Merge.bbox', "B")
# nuke.knobDefault('ChannelMerge.bbox', "union")
# nuke.knobDefault('Copy.bbox', "B side")


# Menues
lukeGizmosMenu = nuke.toolbar("Nodes").addMenu("Luke")
lukeGizmosMenu.addCommand("sb Backdrop", 'sb_backdrop.sb_backdrop()', 'alt+b', shortcutContext=2)

menuBar = nuke.menu("Nuke")

menuBar.findItem('Edit').addCommand('HotBox', 'channel_hotbox.start()', 'alt+v')

menuBar.addCommand('Luke/Make connector', "labelConnector.makeConnector()",
                             'alt+shift+A', shortcutContext=2)  # also renames an existing connector
menuBar.addCommand('Luke/Connect connectors', "labelConnector.runLabelMatch()",
                             'A', shortcutContext=2)  # standard run to match labels, connect nodes, or make new connections
menuBar.addCommand('Luke/Force Connect connectors', "labelConnector.runLabelMatch(forceShowUi = True)",
                             'alt+A', shortcutContext=2)  # force show UI to make new connection when a single Node is selected


# menuBar.findItem('Edit').findItem('Extract').setShortcut('e')

menuBar.addCommand('Luke/Align Dots', "AlignDots.AlignDots()", "alt+.", shortcutContext=2)

lukeGizmosMenu.addCommand('Luke/sb_convertCornerPin', "sb_convertCornerPin.sb_convertCornerPin()")


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
