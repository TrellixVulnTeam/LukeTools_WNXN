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
txtnew = txtnew.upper()

if txtnew:
    n['label'].setValue(txtnew)
    for x in n.dependent():
        if x['label'].getValue() == txtold:
            x['label'].setValue(txtnew)