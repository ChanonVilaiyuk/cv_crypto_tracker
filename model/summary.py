import logging
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui


class Summary(QtWidgets.QTreeWidget):
    """docstring for Summary"""
    def __init__(self, parent=None):
        super(Summary, self).__init__(parent=parent)
        self.setMaximumSize(QtCore.QSize(100000, 60))
        self.item = QtWidgets.QTreeWidgetItem(self)

    def set_header(self, titles):
        self.titles = titles
        self.setHeaderLabels(titles)

    def set_column_size(self, column, size):
        self.header().resizeSection(column, size)

    def add_value(self, column, value):
        self.item.setText(column, str(value))
        self.item.setData(column, QtCore.Qt.UserRole, value)


def find_parent_layout(widget):
    parent_widget = widget.parent()
    children = parent_widget.children()

    for child in children:
        if isinstance(child, QtWidgets.QVBoxLayout):
            for i in range(child.count()):
                if isinstance(child.itemAt(i).widget(), type(widget)):
                    return i, child
