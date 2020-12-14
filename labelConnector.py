# labelConnector v0.05

import math
import logging
import nuke
try:
    # < Nuke 11
    import PySide.QtCore as QtCore
    import PySide.QtGui as QtGui
    import PySide.QtGui as QtGuiWidgets
except ImportError:
    # >= Nuke 11
    import PySide2.QtCore as QtCore
    import PySide2.QtGui as QtGui
    import PySide2.QtWidgets as QtGuiWidgets


log = logging.getLogger("labelMatcher")

undo = nuke.Undo()
undoEventText = "Label Connector"

BUTTON = "border-radius: 8px; font: 13px;"

button_regular_color = 673720575
button_highlight_color = 3261606143


class LayerButton(QtGuiWidgets.QPushButton):
    """Custom QPushButton to change colors when hovering above."""
    def __init__(self, dot, node, button_width, parent=None):
        super(LayerButton, self).__init__(parent)
        self.setMouseTracking(True)
        self.setText(dot.knob('label').getValue())
        self.dot = dot
        self.node = node

        self.setMinimumWidth(button_width / 2)
        self.setSizePolicy(QtGuiWidgets.QSizePolicy.Preferred,
                           QtGuiWidgets.QSizePolicy.Expanding)
        self.color = rgb2hex(interface2rgb(getTileColor(dot)))
        self.highlight = rgb2hex(interface2rgb(button_highlight_color))
        self.setStyleSheet("background-color:"+self.color + ";" + BUTTON)

    def enterEvent(self, event):  # pylint: disable=invalid-name,unused-argument
        """Change color to orange when mouse enters button."""
        self.setStyleSheet("background-color:"+self.highlight + ";" + BUTTON)

    def leaveEvent(self, event):  # pylint: disable=invalid-name,unused-argument
        """Change color to grey when mouse leaves button."""
        self.setStyleSheet("background-color:"+self.color + ";" + BUTTON)


class LineEdit(QtGuiWidgets.QLineEdit):
    """Custom QLineEdit with combined auto completion."""
    def __init__(self, parent, dots, node):
        super(LineEdit, self).__init__(parent)
        self.parent = parent
        self.node = node
        self.dots = dots
        self.setStyleSheet(BUTTON)

        dot_list = []
        for dot in dots:
            dot_list.append(dot.knob('label').getValue())

        self.setSizePolicy(QtGuiWidgets.QSizePolicy.Preferred,
                           QtGuiWidgets.QSizePolicy.Expanding)
        self.completer = QtGuiWidgets.QCompleter(dot_list, self)
        self.completer.setCompletionMode(QtGuiWidgets.QCompleter.InlineCompletion)  # pylint: disable=line-too-long
        self.setCompleter(self.completer)
        self.completer.activated.connect(self.returnPressed)


class labelConnector(QtGuiWidgets.QWidget):
    """User Interface class to provide buttons for each channel layer."""

    def __init__(self, node, dots):
        super(labelConnector, self).__init__()

        length = math.ceil(math.sqrt(len(dots) + 1))
        width, height = length * 200, length * 50
        self.setFixedSize(width, height)
        offset = QtCore.QPoint(width * 0.5, height * 0.5)
        self.move(QtGui.QCursor.pos() - offset)

        grid = QtGuiWidgets.QGridLayout()
        self.setLayout(grid)

        column_counter, row_counter = 0, 0
        button_width = width / length

        for dot in dots:
            button = LayerButton(dot, node, button_width)
            button.clicked.connect(self.clicked)
            grid.addWidget(button, row_counter, column_counter)

            if column_counter > length:
                row_counter += 1
                column_counter = 0

            else:
                column_counter += 1

        self.input = LineEdit(self, dots, node)
        grid.addWidget(self.input, row_counter, column_counter)
        self.input.returnPressed.connect(self.line_enter)

        self.set_window_properties()

    def set_window_properties(self):
        """Set window falgs and focused widget."""
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # make sure the widgets closes when it loses focus
        self.installEventFilter(self)
        self.input.setFocus()

    def keyPressEvent(self, event):  # pylint: disable=invalid-name
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def clicked(self):
        undo.begin(undoEventText)
        self.sender().node["label"].setValue( self.sender().text())
        connectNodeToDot(self.sender().node,self.sender().dot)
        undo.end()
        self.close()


    def line_enter(self):
        undo.begin(undoEventText)
        self.sender().node["label"].setValue( self.input.text())
        for dot in self.sender().dots:
            if self.input.text() == dot.knob('label').getValue():
                connectNodeToDot(self.sender().node,dot)
                undo.end()
                self.close()
        undo.end()

    def eventFilter(self, object, event):
        if event.type() in [QtCore.QEvent.WindowDeactivate, QtCore.QEvent.FocusOut]:
            self.close()
            return True
        return False




def connectNodeToDot(node,dot):
    undo.begin(undoEventText)
    labelNode = node["label"].value()
    labelDot = dot["label"].value()
    if labelNode == labelDot:
        if not node.name().startswith("Connector"):

            node.setInput(0,dot)
            node["hide_input"].setValue(True)
            undo.end()

        return True

    undo.end()
    return False


def getAllDots():
    #here we could filter for a dot nc like
    # if dot.name().startswith("Connector...") just to make it more bullet proof
    # we also return only set of dots with labels
    dots = list()
    compareList = list()
    doubleEntries = False
    for dot in nuke.allNodes("Dot"):
        if dot.name().startswith("Connector"):
                if dot["label"].value():
                    if not dot["label"].value() in compareList:
                        dots.append(dot)
                        compareList.append(dot["label"].value())
                    else:
                        log.info("Double Label Entry found on Connector Dots skipping dot %s" % dot.name())
                        doubleEntries = True
    if doubleEntries:
        nuke.message('Double Connectors found. Check Log for full list!')

    #dots.sort()
    dots.sort(key=lambda dot: dot.knob('label').value())
    return dots

def runLabelMatch():

    uiCheck = False
    dots = getAllDots()
    nodes = nuke.selectedNodes()
    for node in nodes:
        if node["label"].value():
            count = 0
            for dot in dots:
                if not connectNodeToDot(node,dot):
                    count += 1
            if count == len(dots):
                uiCheck = True
        else:
            uiCheck = True

    # if the label is empty or not match could be found and the selection is just one node
    if uiCheck and len(nodes) == 1 and dots:
        global labelConnectorUi  # pylint: disable=global-statement
        labelConnectorUi = labelConnector(node, dots)
        labelConnectorUi.show()




def interface2rgb(hexValue, normalize = True):
    '''
    Convert a color stored as a 32 bit value as used by nuke for interface colors to normalized rgb values.

    '''
    return [(0xFF & hexValue >>  i) / 255.0 for i in [24,16,8]]

def rgb2interface(rgb):
    '''
    Convert a color stored as rgb values to a 32 bit value as used by nuke for interface colors.
    '''
    if len(rgb) == 3:
        rgb = rgb + (255,)

    return int('%02x%02x%02x%02x'%rgb,16)


def getTileColor(node = None):
    '''
    If a node has it's color set automatically, the 'tile_color' knob will return 0.
    If so, this function will scan through the preferences to find the correct color value.
    '''

    if not node:
        node = nuke.selectedNode()

    interfaceColor = node.knob('tile_color').value()

    if interfaceColor == 0 or interfaceColor == nuke.defaultNodeColor(node.Class()) or interfaceColor == 3435973632L:
        interfaceColor = button_regular_color;

    return interfaceColor


def rgb2hex(rgbaValues):
    '''
    Convert a color stored as normalized rgb values to a hex.
    '''
    if len(rgbaValues) < 3:
        return
    return '#%02x%02x%02x' % (rgbaValues[0]*255,rgbaValues[1]*255,rgbaValues[2]*255)

def hex2rgb(hexColor):
    '''
    Convert a color stored as hex to rgb values.
    '''
    hexColor = hexColor.lstrip('#')
    return tuple(int(hexColor[i:i+2], 16) for i in (0, 2 ,4))

def rgb2interface(rgb):
    '''
    Convert a color stored as rgb values to a 32 bit value as used by nuke for interface colors.
    '''
    if len(rgb) == 3:
        rgb = rgb + (255,)

    return int('%02x%02x%02x%02x'%rgb,16)
