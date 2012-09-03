# AlloyCommunicator.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

import json

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

from alloy.AlloyEnvironment import AlloyEnvironment

#___________________________________________________________________________________________________ AlloyCommunicator
class AlloyCommunicator(QObject):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self):
        """Creates a new instance of AlloyCommunicator."""
        QObject.__init__(self)
        self._frame     = None
        self._callbacks = dict()

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: frame
    @property
    def frame(self):
        return self._frame
    @frame.setter
    def frame(self, value):
        self._frame = value

#===================================================================================================
#                                                                                     P U B L I C

#___________________________________________________________________________________________________ addAction
    def addAction(self, action, callback):
        self._callbacks[action] = callback

#___________________________________________________________________________________________________ getImage
    @Slot(unicode, result=QPixmap)
    def getImage(self, imageID):
        image = AlloyEnvironment.getImage(unicode(imageID))
        if not image:
            image = AlloyEnvironment.getImage(u'8.jpg')
        return image

#___________________________________________________________________________________________________ receive
    @Slot(unicode, result=unicode)
    def receive(self, request):
        print u'RECEIVING: ' + unicode(request)
        request = json.loads(request)

        if request['action'] in self._callbacks:
            response = self._callbacks[request['action']](request['payload'])
            print u'RESPONSE: ' + unicode(response)
        else:
            print u'ERROR: Unrecognized request: ', request
            return u'{"result":false}'

        if isinstance(response, bool):
            return '{"result":%s}' % ('true' if response else 'false')
        elif response:
            return json.dumps(response)

        return '{"result":true}'

#___________________________________________________________________________________________________ send
    def send(self, action, payload):
        print u'SENDING: %s -> %s' % (action, unicode(payload))
        request  = json.dumps({'action':action, 'payload':payload})
        response = self._frame.evaluateJavaScript(u'window.alloyReceiver(%s)' % unicode(request))
        print u'RESPONSE: ' + unicode(response)
        return json.loads(response)

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
