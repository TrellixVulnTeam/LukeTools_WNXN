#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Copy UNC Path
# COLOR: #254052
#
#----------------------------------------------------------------------------------------------------------

if nuke.NUKE_VERSION_MAJOR < 11:
    from PySide import QtCore, QtGui, QtGui as QtWidgets
else:
    from PySide2 import QtGui, QtCore, QtWidgets

clipboard = QtWidgets.QApplication.clipboard()

text = ""

for i in nuke.selectedNodes():
    text += os.path.dirname(i['file'].getValue())+'/\n'

clipboard.setText(text.replace('/','\\'))