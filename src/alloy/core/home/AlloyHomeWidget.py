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
from alloy.core.application.remoteExec import remoteExec
from alloy.data.AlloyData import AlloyData
import nimble

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
        comm.addAction('getColumns', self._handleGetColumns)
        comm.addAction('getCommandData', self._handleGetCommandData)
        comm.addAction('getVariantData', self._handleGetVariantData)
        comm.addAction('hasVariants', self._handleHasVariants)
        comm.addAction('getVariants', self._handleGetVariants)

        comm.addAction('getImageCategories', self._handleGetImageCategories)
        comm.addAction('getImageList', self._handleGetImageList)

        comm.addAction('updateColumn', self._handleUpdateColumn)
        comm.addAction('reorderVariants', self._handleReorderVariants)

        comm.addAction('createVariant', self._handleCreateVariant)
        comm.addAction('modifyVariant', self._handleModifyVariant)
        comm.addAction('deleteVariant', self._handleDeleteVariant)

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
            conn = nimble.getConnection()
        except Exception, err:
            pass

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
    def _handleGetColumns(self, payload):
        return AlloyData.getColumns(payload.get('categoryID', None))

#___________________________________________________________________________________________________ _handleExecuteCommand
    def _handleExecuteCommand(self, payload):

        if 'commandID' in payload:
            command = AlloyData.getCommandData(payload['commandID'])
        elif 'variantID' in payload:
            command = AlloyData.getVariantData(payload['variantID'])
        else:
            return False

        if not command:
            return False

        if command['language'] == 'python':
            if command['location'] == 'remote':
                return remoteExec(command['script'])
            else:
                try:
                    conn = nimble.getConnection()
                    conn.runPythonScript(command['script'])
                except Exception, err:
                    return False
        else:
            print 'Executing mel script'
            try:
                conn = nimble.getConnection()
                conn.runMelScript(command['script'])
            except Exception, err:
                return False

        return True

#___________________________________________________________________________________________________ _handleGetImageCategories
    def _handleGetImageCategories(self, payload):
        out      = []
        rootPath = AlloyEnvironment.getRootIconPath()
        for p in os.listdir(rootPath):
            path = os.path.join(rootPath, p)
            if not os.path.isdir(path):
                continue

            items = os.listdir(path)
            if not items:
                continue

            out.append({'label':p[0].upper() + p[1:], 'id':p})

        return out

#___________________________________________________________________________________________________ _handleGetImageList
    def _handleGetImageList(self, payload):
        out      = []
        rootPath = AlloyEnvironment.getRootIconPath()
        folder   = payload['imageCategoryID']

        for image in os.listdir(os.path.join(rootPath, folder)):
            if image.split(u'.')[-1] not in [u'jpg', u'png']:
                continue
            out.append(folder + os.sep + image)

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
        return AlloyData.getCommandData(**payload)

#___________________________________________________________________________________________________ _handleModifyCategory
    def _handleModifyCategory(self, payload):
        return AlloyData.modifyCategory(**payload)

#___________________________________________________________________________________________________ _handleDeleteCategory
    def _handleDeleteCategory(self, payload):
        return AlloyData.deleteCategory(**payload)

#___________________________________________________________________________________________________ _handleUpdateColumn
    def _handleUpdateColumn(self, payload):
        return AlloyData.reorderColumn(**payload)

#___________________________________________________________________________________________________ _handleGetVariant
    def _handleGetVariantData(self, payload):
        return AlloyData.getVariantData(**payload)

#___________________________________________________________________________________________________ _handleGetVariants
    def _handleGetVariants(self, payload):
        return AlloyData.getVariants(**payload)

#___________________________________________________________________________________________________ _handleCreateVariant
    def _handleCreateVariant(self, payload):
        return AlloyData.createVariant(**payload)

#___________________________________________________________________________________________________ _handleModifyVariant
    def _handleModifyVariant(self, payload):
        return AlloyData.modifyVariant(**payload)

#___________________________________________________________________________________________________ _handleCreateVariant
    def _handleDeleteVariant(self, payload):
        return AlloyData.deleteVariant(**payload)

#___________________________________________________________________________________________________ _handleReorderVariants
    def _handleReorderVariants(self, payload):
        return AlloyData.reorderVariants(**payload)

#___________________________________________________________________________________________________ _handleHasVariants
    def _handleHasVariants(self, payload):
        return AlloyData.hasVariants(**payload)

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