class Node:
    """A node of a linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    @property
    def data(self):
        """Get node data"""
        return self._data

    @data.setter
    def data(self, node_data):
        """Set node data"""
        self._data = node_data

    @property
    def next(self):
        """Get next node"""
        return self._next

    @next.setter
    def next(self, node_next):
        """Set next node"""
        self._next = node_next

    def __str__(self):
        """String"""
        return str(self._data)
