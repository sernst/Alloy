# AlloyWebPage.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

#___________________________________________________________________________________________________ AlloyWebPage
class AlloyWebPage(QWebPage):
    """A class for..."""

#===================================================================================================
#                                                                                     P U B L I C

#___________________________________________________________________________________________________ javaScriptConsoleMessage
    def javaScriptConsoleMessage(self, msg, line, source):
        if msg == 'Empty trace item':
            return

        print 'LOG:', msg
        print '    LINE: #%d OF %s' % (line, source)

#___________________________________________________________________________________________________ javaScriptAlert
    def javaScriptAlert(self, originatingFrame, msg):
        print 'ALERT:', msg

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
