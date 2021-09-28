#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: rename Connector
# COLOR: #54360f
#
#----------------------------------------------------------------------------------------------------------

n = nuke.selectedNode()

txtold = n['label'].getValue()
txtnew = nuke.getInput('Change label', txtold)

if txtnew:
    txtnew = txtnew.upper()
    n['label'].setValue(txtnew)
    for x in n.dependent(nuke.INPUTS | nuke.HIDDEN_INPUTS, forceEvaluate = False):
        if x['label'].getValue() == txtold:
            x['label'].setValue(txtnew)