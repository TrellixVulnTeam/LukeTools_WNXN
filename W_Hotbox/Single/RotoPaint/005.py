#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Set LifeTime to Keys
#
#----------------------------------------------------------------------------------------------------------

#modified version of code found on the fourms
#http://community.thefoundry.co.uk/discussion/topic.aspx?f=190&t=102599
elements = []

def getElements(layer): 
  global elements
  for element in layer: 
    if isinstance(element, nuke.rotopaint.Layer): 
      getElements(element)
    elif isinstance(element, nuke.rotopaint.Stroke) or isinstance(element, nuke.rotopaint.Shape):
      elements.append(element)

  return elements

for n in nuke.selectedNodes():
  nodec = n['curves']
  nlayer = nodec.rootLayer
  
  
  # Clear global elements array so that only the current Roto/Rotopaint node's elements are 'autolifed'
  elements = []
  getElements(nlayer)
  
  for element in elements:
#    if element.locked:
#      element.locked = False
      
      # Get keyframes for the 0-indexed control point
      if isinstance(element, nuke.rotopaint.Stroke):
        keys = element[0].getControlPointKeyTimes()
      elif isinstance(element, nuke.rotopaint.Shape):
        keys = element[0].center.getControlPointKeyTimes()
      
      firstKey = keys[0]
      lastKey = keys[-1]
      
      attrs = element.getAttributes()
      attrs.set('ltn', firstKey) # frame range 'from' value
      attrs.set('ltm', lastKey) # frame range 'to' value
      attrs.set('ltt', 4) # set 'lifetime type' of element to 'frame range' - index 4 in combobox
      
#     element.locked = True
      nodec.changed()
    