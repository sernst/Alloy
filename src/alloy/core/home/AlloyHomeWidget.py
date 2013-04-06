# AlloyHomeWidget.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

import os

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

from pyglass.gui.web.PyGlassWebView import PyGlassWebView
from pyglass.widgets.PyGlassWidget import PyGlassWidget

import nimble

from alloy.AlloyEnvironment import AlloyEnvironment
from alloy.core.application.remoteExec import remoteExec
from alloy.data.AlloyData import AlloyData

#___________________________________________________________________________________________________ AlloyHomeWidget
class AlloyHomeWidget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of AlloyHomeWidget."""
        PyGlassWidget.__init__(self, parent, widgetFile=False, **kwargs)

        try:
            conn = nimble.getConnection()
        except Exception, err:
            pass

#===================================================================================================
#                                                                               P R O T E C T E D

#___________________________________________________________________________________________________ _handleReturnDefaultImage
    def _handleReturnDefaultImage(self, payload):
        return AlloyEnvironment.DEFAULT_ICON

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
                    print err
                    return False
        else:
            print 'Executing mel script'
            try:
                conn = nimble.getConnection()
                conn.runMelScript(command['script'])
            except Exception, err:
                print err
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
