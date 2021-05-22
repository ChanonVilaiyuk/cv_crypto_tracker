import os
from PySide2 import QtWidgets
import qt_utils
# reload(qt_utils)
moduleDir = os.path.dirname(__file__)
uiPath = '{}/ui.ui'.format(moduleDir)
qt_utils.convert(uiPath)

import ui
reload(ui)

class MainTool(QtWidgets.QMainWindow):
    """docstring for MainTool"""
    def __init__(self, parent=None):
        super(MainTool, self).__init__(parent=parent)
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)


def show():
    app = MainTool(qt_utils.getMayaWindow())
    app.show()
    return app
