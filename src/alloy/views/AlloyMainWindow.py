# AlloyMainWindow.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

from pyglass.windows.PyGlassWindow import PyGlassWindow

from alloy.AlloyEnvironment import AlloyEnvironment
from alloy.core.home.AlloyHomeWidget import AlloyHomeWidget

#___________________________________________________________________________________________________ AlloyMainWindow
class AlloyMainWindow(PyGlassWindow):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, **kwargs):
        """Creates a new instance of AlloyMainWindow."""
        PyGlassWindow.__init__(
            self,
            widgets={
                'main':AlloyHomeWidget
            },
            widgetID='main',
            title=u'Alloy',
            **kwargs
        )

        self.setStyleSheet(AlloyEnvironment.getStylesheet())
