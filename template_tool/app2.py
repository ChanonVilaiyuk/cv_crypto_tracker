import os
from PySide2 import QtWidgets
import qt_utils
# reload(qt_utils)
moduleDir = os.path.dirname(__file__)
uiPath = '{}/ui.ui'.format(moduleDir)
UiClass, BaseClass = qt_utils.loadUiType(uiPath)

class MainTool(BaseClass):
    """docstring for MainTool"""
    def __init__(self, parent=None):
        super(MainTool, self).__init__(parent=parent)
        self.ui = UiClass()
        self.ui.setupUi(self)


def show():
    app = MainTool(qt_utils.getMayaWindow())
    app.show()
    return app
