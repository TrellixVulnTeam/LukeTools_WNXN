#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Toggle BBox Error
# COLOR: #602400
#
#----------------------------------------------------------------------------------------------------------

boxWarning = nuke.toNode('preferences').knob('boundingBoxWarning')

if boxWarning.value():
    boxWarning.setValue(False)
else:
    boxWarning.setValue(True)