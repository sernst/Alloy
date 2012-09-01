# AlloyHomeWidget.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

import os

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

from alloy.AlloyEnvironment import AlloyEnvironment
from alloy.core.application.AlloyWebPage import AlloyWebPage
from alloy.core.home.AlloyCommunicator import AlloyCommunicator
from alloy.data.AlloyData import AlloyData
import nimble
from nimble.data.enum.DataKindEnum import DataKindEnum

#___________________________________________________________________________________________________ AlloyHomeWidget
class AlloyHomeWidget(QWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent =None, flags =0):
        """Creates a new instance of AlloyHomeWidget."""
        QWidget.__init__(self, parent, flags)
        self.setStyleSheet(AlloyEnvironment.getStylesheet())

        comm = AlloyCommunicator()
        self._comm  = comm
        comm.addAction('execute', self._handleExecuteCommand)

        comm.addAction('getCategories', self._handleGetCategories)
        comm.addAction('getCommands', self._handleGetCommands)
        comm.addAction('getImageList', self._handleGetImageList)
        comm.addAction('getCommandData', self._handleGetCommandData)

        comm.addAction('createCommand', self._handleCreateCommand)
        comm.addAction('modifyCommand', self._handleModifyCommand)
        comm.addAction('deleteCommand', self._handleDeleteCommand)

        comm.addAction('createCategory', self._handleCreateCategory)
        comm.addAction('modifyCategory', self._handleModifyCategory)
        comm.addAction('deleteCategory', self._handleDeleteCategory)

        self._mainBox = QVBoxLayout()
        self.setLayout(self._mainBox)

        self._view  = QWebView()
        page        = AlloyWebPage()
        self._view.setPage(page)
        self._webInspector = QWebInspector()
        self._webInspector.setPage(page)
        page.settings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)

        shortcut = QShortcut(self)
        shortcut.setKey(QKeySequence(Qt.Key_F12))
        shortcut.activated.connect(self.toggleInspector)
        self._webInspector.setVisible(False)

        self._view.loadFinished.connect(self._handleLoadFinished)
        self._view.setUrl(QUrl('http://17.vizmedev.com/guiHome/'))
        self._mainBox.addWidget(self._view)

        try:
            self._conn = nimble.getConnection()
        except Exception, err:
            self._conn = None

#===================================================================================================
#                                                                               P R O T E C T E D

#___________________________________________________________________________________________________ toggleInspector
    def toggleInspector(self):
        self._webInspector.setVisible(not self._webInspector.isVisible())

#___________________________________________________________________________________________________ _handleLoadFinished
    def _handleLoadFinished(self, result):
        frame = self._view.page().mainFrame()
        self._comm.frame = frame
        frame.addToJavaScriptWindowObject('ALLOY', self._comm)

#___________________________________________________________________________________________________ _handleGetCategories
    def _handleGetCategories(self, payload):
        return AlloyData.getCategories()

#___________________________________________________________________________________________________ _handleGetCommands
    def _handleGetCommands(self, payload):
        return AlloyData.getCommands(payload.get('categoryID', None))

#___________________________________________________________________________________________________ _handleExecuteCommand
    def _handleExecuteCommand(self, payload):
        command = AlloyData.getCommandData(payload['commandID'])
        if command is None:
            return False

        print 'EXECUTING:', command
        try:
            if not self._conn:
                self._conn = nimble.getConnection()

            if command['kind'] == DataKindEnum.MAYA_COMMAND:
                self._conn.maya(command['command'], *command['args'], **command['kwargs'])
        except Exception, err:
            return False

        return True

#___________________________________________________________________________________________________ _handleGetImageList
    def _handleGetImageList(self, payload):
        out = []
        for image in os.listdir(AlloyEnvironment.getRootIconPath()):
            if image.split(u'.')[-1] not in [u'jpg', u'png']:
                continue
            out.append(image)

        return out

#___________________________________________________________________________________________________ _handleCreateCommand
    def _handleCreateCommand(self, payload):
        return AlloyData.createCommand(**payload)

#___________________________________________________________________________________________________ _handleModifyCommand
    def _handleModifyCommand(self, payload):
        return AlloyData.modifyCommand(**payload)

#___________________________________________________________________________________________________ _handleDeleteCommand
    def _handleDeleteCommand(self, payload):
        return AlloyData.deleteCommand(**payload)

#___________________________________________________________________________________________________ _handleCreateCategory
    def _handleCreateCategory(self, payload):
        return AlloyData.createCategory(**payload)

#___________________________________________________________________________________________________ _handleGetCommandData
    def _handleGetCommandData(self, payload):
        return AlloyData.getCommandData(payload['id'])

#___________________________________________________________________________________________________ _handleModifyCategory
    def _handleModifyCategory(self, payload):
        return AlloyData.modifyCategory(**payload)

#___________________________________________________________________________________________________ _handleDeleteCategory
    def _handleDeleteCategory(self, payload):
        return AlloyData.deleteCategory(**payload)

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
