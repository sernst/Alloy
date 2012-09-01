# __init__.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

import sys

from PySide.QtGui import *

from alloy.core.application.AlloyApplication import AlloyApplication

#===================================================================================================
#                                                                               F U N C T I O N S

#___________________________________________________________________________________________________ run
def run(args =None):
    app = QApplication(args)
    win = AlloyApplication()
    win.show()

    app.exec_()
    sys.exit()
