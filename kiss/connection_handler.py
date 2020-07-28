"""Detect when nodes overlap and connect them."""

# Import third-party modules
import nuke

# Import local modules
from kiss.constants import CONNECTION_RADIUS

# The global ConnectionHandler that detects overlapping and connects nodes when
# they do. Making this a global (but only used inside this module) to have
# just -one- ConnectionHandler and keeping used resources at a reasonable
# level.
_HANDLER = None


def launch_kiss():
    """Add kiss knob changed callback."""
    nuke.addKnobChanged(kiss)


def kiss():
    """Main entry to check for collisions and connect nodes-

    This will create a ConnectionHandler if not already existing and run
    the main method which checks for node overlappings and if detected connect
    nodes.

    """
    global _HANDLER

    if not _HANDLER:
        _HANDLER = ConnectionHandler(nuke.thisNode())

    try:
        _HANDLER.main()
    except ValueError:
        # The node has been deleted which raises a ValueError as we try to
        # access a node and knobs that don't exist anymore. In that case remove
        # the handler as we don't need to process anything anymore.
        _HANDLER.remove_handler()


class ConnectionHandler(object):
    """Connect nodes when they are close to each other.

    This handler checks the given node's location against all other node's
    locations. When they overlap we connect them to each other.

    """

    def __init__(self, node):
        """Initialize the ConnectionHandler instance.

        Args:
            node (nuke.Node): The node to create a node connection for.

        """
        self.node = node
        self.nodes = self._init_node_data()

    def _init_node_data(self):
        """Get all nodes and their location in the DAG."""
        return {
            node: [node.xpos(), node.xpos()]
            for node in nuke.allNodes()
            if node != self.node
        }

    def remove_handler(self):
        """Remove the handler and the knobChanged callback."""
        nuke.removeKnobChanged(kiss)
        global _HANDLER
        _HANDLER = None

    def check_collision(self):
        """Check if nodes overlap and if so return the overlapping nodes.

        Returns:
            nuke.Node, nuke.Node: The nodes that overlap.

        """
        for node in self.nodes:
            xpos = node.xpos()
            x_min = xpos - CONNECTION_RADIUS
            x_max = xpos + node.screenWidth() + CONNECTION_RADIUS

            if x_min < self.node.xpos() < x_max:
                ypos = node.ypos()
                y_min = ypos - CONNECTION_RADIUS
                y_max = ypos + node.screenHeight() + CONNECTION_RADIUS

                if y_min < self.node.ypos() < y_max:

                    # Connect selected node's input with other node's output.
                    if self.node.ypos() > node.ypos():
                        return self.node, node

                    # Connect other nodes output with selected node's input.
                    return node, self.node

        return None, None

    def connect(self, node_a, node_b):
        """Connect node a to node b and remove handler and callback.

        Args:
            node_a (nuke.Node): The node to connect to.
            node_b (nuke.Node): The node to connect.

        """
        # Return early when node_a cannot connect to any more nodes.
        if node_a.inputs() == node_a.maxInputs():
            return

        # In case node_b is already connected to node_a, we don't want to
        # connect it again to node_a.
        for index in range(node_a.inputs()):
            if node_a.input(index) == node_b:
                return

        node_a.setInput(node_a.inputs(), node_b)

        self.remove_handler()

    def main(self):
        """Check if nodes overlap and if so connect them,"""
        node_a, node_b = self.check_collision()
        if not all([node_a, node_b]):
            return

        self.connect(node_a, node_b)
