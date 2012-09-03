# AlloyApplication.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

from PySide.QtGui import *

from alloy.AlloyEnvironment import AlloyEnvironment
from alloy.core.home.AlloyHomeWidget import AlloyHomeWidget

#___________________________________________________________________________________________________ AlloyApplication
class AlloyApplication(QMainWindow):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent =None, flags =0):
        """Creates a new instance of AlloyApplication."""
        QMainWindow.__init__(self, parent, flags)

        cw = AlloyHomeWidget(self)
        self.setCentralWidget(cw)
        self.setWindowTitle('Alloy')

        self.setStyleSheet(AlloyEnvironment.getStylesheet())

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: propertyName
    @property
    def propertyName(self):
        return None
    @propertyName.setter
    def propertyName(self, value):
        pass

#===================================================================================================
#                                                                                     P U B L I C

#___________________________________________________________________________________________________ publicMethod
    def publicMethod(self):
        """Doc..."""
        pass

#===================================================================================================
#                                                                               P R O T E C T E D

#___________________________________________________________________________________________________ _internalMethod
    def _internalMethod(self):
        """Doc..."""
        pass

#===================================================================================================
#                                                                               I N T R I N S I C

#___________________________________________________________________________________________________ __repr__
    def __repr__(self):
        return self.__str__()

#___________________________________________________________________________________________________ __unicode__
    def __unicode__(self):
        return unicode(self.__str__())

#___________________________________________________________________________________________________ __str__
    def __str__(self):
        return '<%s>' % self.__class__.__name__
