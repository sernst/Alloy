# AlloyEnvironment.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

import os
from PySide.QtGui import *

#___________________________________________________________________________________________________ AlloyEnvironment
class AlloyEnvironment(object):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

    _styleSheets = dict()

    ROOT_CONFIG_PATH   = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'config')
    ROOT_RESOURCE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'resources')
    DEFAULT_ICON       = u'8.jpg'

#___________________________________________________________________________________________________ getIconPath
    @classmethod
    def getRootIconPath(cls):
        return unicode(os.path.join(cls.ROOT_RESOURCE_PATH, u'icons')) + os.sep

#___________________________________________________________________________________________________ getIconPath
    @classmethod
    def getIconPath(cls, name, folder =None):
        name = unicode(name)

        if not folder:
            folder = u'icons'

        path = unicode(os.path.join(cls.ROOT_RESOURCE_PATH, folder, name))
        if os.path.exists(path):
            return path

        for ext in [u'jpg', u'png']:
            p = path + u'.' + ext
            if os.path.exists(p):
                return p

        return unicode(os.path.join(cls.ROOT_RESOURCE_PATH, u'icons', cls.DEFAULT_ICON))

#___________________________________________________________________________________________________ getDatabaseURL
    @classmethod
    def getDatabaseURL(cls, name =None, folder =None):
        name = unicode(name)
        if not name.endswith(u'.alloy'):
            name += u'.alloy'

        if not folder:
            folder = u'data'

        return u'sqlite:///' + unicode(os.path.join(cls.ROOT_RESOURCE_PATH, folder, name))

#___________________________________________________________________________________________________ getImage
    @classmethod
    def getImage(cls, name =None, folder =None):
        pix  = QPixmap()
        pix.load(cls.getIconPath(name, folder))
        return pix

#___________________________________________________________________________________________________ getStylesheetPath
    @classmethod
    def getStylesheetPath(cls, name =None, folder =None):
        if not name:
            name = 'global.css'

        if not folder:
            folder = 'style'

        stylePath = os.path.join(cls.ROOT_RESOURCE_PATH, folder, name)
        if os.path.exists(stylePath):
            return stylePath
        elif os.path.exists(stylePath + '.css'):
            return stylePath + '.css'

        return None

#___________________________________________________________________________________________________ getStylesheet
    @classmethod
    def getStylesheet(cls, name =None, folder =None):
        path = cls.getStylesheetPath(name, folder)
        if not path:
            return u''

        if path in cls._styleSheets:
            return cls._styleSheets[path]

        f = open(path, 'r')
        css = f.read().decode('utf-8', 'ignore')
        f.close()

        cls._styleSheets[path] = css

        return css
