# AlloyEnvironment.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

import os
from PySide.QtGui import *

#___________________________________________________________________________________________________ AlloyEnvironment
class AlloyEnvironment(object):
    """ Stores environmental variables as well as acting as an environmental interface via
        class method getters.
    """

#===================================================================================================
#                                                                                       C L A S S

    ROOT_CONFIG_PATH   = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', '..', 'config'
    )

    ROOT_RESOURCE_PATH = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', '..', 'resources'
    )

    DEFAULT_ICON = u'maya.png'
    DEVELOPMENT  = False
    LOG_LEVEL    = 0

    _styleSheets = dict()

    _URL     = 'http://17.vizmeweb.com/guiHome/'
    _DEV_URL = 'http://17.vizmedev.com/guiHome/'

#___________________________________________________________________________________________________ getHomeUrl
    @classmethod
    def getHomeUrl(cls):
        return cls._DEV_URL if cls.DEVELOPMENT else cls._URL

#___________________________________________________________________________________________________ getRootIconPath
    @classmethod
    def getRootIconPath(cls):
        return unicode(os.path.join(cls.ROOT_RESOURCE_PATH, u'icons')) + os.sep

#___________________________________________________________________________________________________ getIconPath
    @classmethod
    def getIconPath(cls, name, folder =None):
        if not name:
            name = cls.DEFAULT_ICON
        else:
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
        if not name:
            name = u'user.alloy'
        else:
            name = unicode(name)
            if not name.endswith(u'.alloy'):
                name += u'.alloy'

        if not folder:
            folder = u'data'

        path = unicode(os.path.join(cls.ROOT_RESOURCE_PATH, folder, name))
        if not path.startswith(u'/'):
            path = u'/' + path

        return u'sqlite://' + path

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
            name = u'global.css'

        if not folder:
            folder = u'style'

        stylePath = os.path.join(cls.ROOT_RESOURCE_PATH, folder, name)
        if os.path.exists(stylePath):
            return stylePath
        elif os.path.exists(stylePath + u'.css'):
            return stylePath + u'.css'

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
