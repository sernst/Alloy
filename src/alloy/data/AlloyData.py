# AlloyData.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

from alloy.data.model import Session
from alloy.data.model.CommandCategories import CommandCategories
from alloy.data.model.UserCommands import UserCommands

#___________________________________________________________________________________________________ AlloyData
class AlloyData(object):
    """A class for..."""

    _COMMAND_INDEX  = 1
    _CATEGORY_INDEX = 4

#===================================================================================================
#                                                                                     P U B L I C

#___________________________________________________________________________________________________ createCategory
    @classmethod
    def createCategory(cls, label):
        session  = Session()
        category = CommandCategories(label=label)
        session.add(category)
        session.commit()
        return {
            'label':category.label,
            'id':'cat' + str(category.i)
        }

#___________________________________________________________________________________________________ modifyCategory
    @classmethod
    def modifyCategory(cls, categoryID, label):
        session = Session()
        result = session.query(CommandCategories).filter_by(
            i=int(CommandCategories.getIndexFromCategoryID(categoryID))
        ).first()

        result.label = label
        session.commit()
        return {
            'label':result.label,
            'id':result.categoryID
        }

#___________________________________________________________________________________________________ deleteCategory
    @classmethod
    def deleteCategory(cls, categoryID):
        session = Session()
        #result =
        return categoryID

#___________________________________________________________________________________________________ createCommand
    @classmethod
    def createCommand(cls, categoryID, **kwargs):
        label = kwargs.get('label')
        info  = kwargs.get('info')
        icon  = kwargs.get('icon')
        return cls._makeButton(label, info, icon)

#___________________________________________________________________________________________________ modifyCommand
    @classmethod
    def modifyCommand(cls, commandID, **kwargs):
        label = kwargs.get('label')
        info  = kwargs.get('info')
        icon  = kwargs.get('icon')
        return cls._makeButton(label, info, icon, commandID)

#___________________________________________________________________________________________________ deleteCommand
    @classmethod
    def deleteCommand(cls, commandID):
        return commandID

#___________________________________________________________________________________________________ getCategories
    @classmethod
    def getCategories(cls):
        return [
            {'label':'General', 'id':'cat1'},
            {'label':'Cadence', 'id':'cat2'},
            {'label':'Polygons', 'id':'cat3'}
        ]

#___________________________________________________________________________________________________ getCommandData
    @classmethod
    def getCommandData(cls, commandID):
        return {
            'language':'python',
            'location':'remote',
            'script':'This is a test script.'
        }

#___________________________________________________________________________________________________ getCommands
    @classmethod
    def getCommands(cls, categoryID):
        if categoryID == 'cat1':
            return cls._createColumns('General')
        elif categoryID == 'cat2':
            return cls._createColumns('Cadence')
        elif categoryID == 'cat3':
            return cls._createColumns('Polygons')

        return cls._createColumns('New Column')

#___________________________________________________________________________________________________ addCategory
    @classmethod
    def addCategory(cls):
        """Doc..."""
        pass

#___________________________________________________________________________________________________ removeCategory
    @classmethod
    def removeCategory(cls):
        """Doc..."""
        pass


#===================================================================================================
#                                                                               P R O T E C T E D

#___________________________________________________________________________________________________ _createColumns
    @classmethod
    def _createColumns(cls, name):
        return [
            cls._makeColumn(name, 1),
            cls._makeColumn(name, 2),
            cls._makeColumn(name, 3),
            cls._makeColumn(name, 4)
        ]

#___________________________________________________________________________________________________ _makeColumn
    @classmethod
    def _makeColumn(cls, name, index):
        import random

        count = random.randint(0,10)
        i     = 0
        cmds  = []

        while i < count:
            cmds.append(cls._makeButton('Label', 'Some info...', '8.jpg'))
            i += 1

        return {
            'commands':cmds,
            'name':name + ' Column ' + str(index)
        }

#___________________________________________________________________________________________________ _makeButton
    @classmethod
    def _makeButton(cls, label, info, iconID, commandID =None):
        """Doc..."""

        if not commandID:
            commandID = 'cmd' + str(cls._COMMAND_INDEX)
            cls._COMMAND_INDEX += 1
        return {
            'id':commandID,
            'label':label,
            'info':info,
            'icon':iconID
        }
