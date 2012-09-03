# AlloyData.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

from sqlalchemy import and_

from alloy.data.model import Session
from alloy.data.model.CommandCategories import CommandCategories
from alloy.data.model.CommandVariants import CommandVariants
from alloy.data.model.UserCommands import UserCommands

#___________________________________________________________________________________________________ AlloyData
class AlloyData(object):
    """A class for..."""

#===================================================================================================
#                                                                                     P U B L I C

#___________________________________________________________________________________________________ createCategory
    @classmethod
    def createCategory(cls, label):
        """ Creates a new category with the specified label and returns the dictionary
            representation of the newly created category, including its id.

            @@@param label:string
                The display label for the new category.

            @@@return dict
                The dictionary representation of the newly created category.
        """

        session  = Session()
        category = CommandCategories(label=unicode(label))
        session.add(category)
        session.commit()

        out = category.toDict()
        session.close()
        return out

#___________________________________________________________________________________________________ modifyCategory
    @classmethod
    def modifyCategory(cls, categoryID, **kwargs):
        session = Session()
        result = session.query(CommandCategories).filter(
            CommandCategories.i == CommandCategories.getIndexFromCategoryID(categoryID)
        ).first()

        if result is None:
            return {'error':'No Such Category'}

        for n,v in kwargs.iteritems():
            if isinstance(v, str):
                v = unicode(v)
            setattr(result, n, v)
            session.commit()

        out = result.toDict()
        session.close()
        return out

#___________________________________________________________________________________________________ deleteCategory
    @classmethod
    def deleteCategory(cls, categoryID):
        session       = Session()
        categoryIndex = CommandCategories.getIndexFromCategoryID(categoryID)
        result = session.query(CommandCategories).filter(CommandCategories.i == categoryIndex).first()

        if result:
            session.delete(result)

        result = session.query(UserCommands).filter(UserCommands.categoryfk == categoryIndex).all()
        for r in result:
            session.delete(r)

            variants = session.query(CommandVariants).filter(CommandVariants.usrcmdfk == r.i).all()
            for v in variants:
                session.delete(v)

        session.commit()
        session.close()

        return {'id':categoryID}

#___________________________________________________________________________________________________ getColumns
    @classmethod
    def getColumns(cls, categoryID):
        session       = Session()
        categoryIndex = CommandCategories.getIndexFromCategoryID(categoryID)

        category = session.query(CommandCategories).filter(
            CommandCategories.i == categoryIndex
        ).first()

        out = []
        for i in range(1, 5):
            name = u'column' + unicode(i)
            out.append({
                'label':getattr(category, name) if category else (u'Column ' + unicode(i)),
                'commands':[]
            })

        session.close()

        if not category:
            return out

        for cmd in cls.getCommands(categoryID):
            out[cmd['column']]['commands'].append(cmd)

        return out

#___________________________________________________________________________________________________ createCommand
    @classmethod
    def createCommand(cls, categoryID, column, row =None, **kwargs):
        session       = Session()
        categoryIndex = CommandCategories.getIndexFromCategoryID(categoryID)

        if row is None or row < 0:
            row = session.query(UserCommands).filter(
                and_(
                    UserCommands.categoryfk == categoryIndex,
                    UserCommands.column == column
                )
            ).count()

        for n,v in kwargs.iteritems():
            if isinstance(v, str):
                kwargs[n] = unicode(v)

        command = UserCommands(categoryfk=categoryIndex, column=column, row=row, **kwargs)
        session.add(command)
        session.commit()

        out = command.toButtonDict()
        session.close()
        return out

#___________________________________________________________________________________________________ reorderColumn
    @classmethod
    def reorderColumn(cls, column, commandIDs):
        session = Session()
        index   = 0
        out     = []
        for cmdID in commandIDs:
            cmdIndex = UserCommands.getIndexFromCommandID(cmdID)
            cmd      = session.query(UserCommands).filter(UserCommands.i == cmdIndex).first()
            if not cmd:
                continue

            cmd.column = column
            cmd.row    = index
            out.append(cmd.commandID)
            index  += 1

        session.commit()
        session.close()
        return out

#___________________________________________________________________________________________________ modifyCommand
    @classmethod
    def modifyCommand(cls, commandID, **kwargs):
        session      = Session()
        commandIndex = UserCommands.getIndexFromCommandID(commandID)
        result       = session.query(UserCommands).filter(UserCommands.i == commandIndex).first()

        if result is None:
            session.close()
            return {'error':'No Such Command'}

        for n,v in kwargs.iteritems():
            if isinstance(v, str):
                v = unicode(v)
            setattr(result, n, v)

        session.commit()

        out = result.toButtonDict()
        session.close()
        return out

#___________________________________________________________________________________________________ deleteCommand
    @classmethod
    def deleteCommand(cls, commandID):
        session      = Session()
        commandIndex = UserCommands.getIndexFromCommandID(commandID)
        result       = session.query(UserCommands).filter(UserCommands.i == commandIndex).first()

        if result is None:
            session.close()
            return {'id':commandID}

        session.delete(result)

        result = session.query(CommandVariants).filter(CommandVariants.usrcmdfk == commandIndex).all()
        for r in result:
            session.delete(result)

        session.commit()
        session.close()

        return {'id':commandID}

#___________________________________________________________________________________________________ getCategories
    @classmethod
    def getCategories(cls):
        session = Session()
        result  = session.query(CommandCategories).all()

        if not result:
            category = CommandCategories()
            session.add(category)
            session.commit()
            out = [category.toDict()]
        else:
            out = []
            for r in result:
                out.append(r.toDict())

        session.close()
        return out

#___________________________________________________________________________________________________ getCommandData
    @classmethod
    def getCommandData(cls, commandID):
        session      = Session()
        commandIndex = UserCommands.getIndexFromCommandID(commandID)
        result       = session.query(UserCommands).filter(UserCommands.i == commandIndex).first()

        if result is None:
            session.close()
            return {'error':'No Such Command'}

        out = result.toDict()
        session.close()
        return out

#___________________________________________________________________________________________________ getCommands
    @classmethod
    def getCommands(cls, categoryID):
        session         = Session()
        categoryIndex   = CommandCategories.getIndexFromCategoryID(categoryID)
        result          = session.query(UserCommands) \
            .filter(UserCommands.categoryfk == categoryIndex) \
            .order_by(UserCommands.row.asc()) \
            .all()

        if not result:
            session.close()
            return []

        out = []
        for r in result:
            out.append(r.toButtonDict())

        session.close()
        return out

#___________________________________________________________________________________________________ getVariants
    @classmethod
    def getVariants(cls, commandID):
        session      = Session()
        commandIndex = UserCommands.getIndexFromCommandID(commandID)
        result       = session.query(CommandVariants).filter(
            CommandVariants.usrcmdfk == commandIndex
        ).order_by(CommandVariants.row.asc()).all()

        out = []
        for r in result:
            out.append(r.toButtonDict())

        return out

#___________________________________________________________________________________________________ getVariantData
    @classmethod
    def getVariantData(cls, variantID):
        session      = Session()
        variantIndex = CommandVariants.getIndexFromVariantID(variantID)
        result       = session.query(CommandVariants).filter(
            CommandVariants.i == variantIndex
        ).first()

        if not result:
            return {'error':'No such variant'}

        return result.toDict()

#___________________________________________________________________________________________________ createVariant
    @classmethod
    def createVariant(cls, commandID, row =None, **kwargs):
        session      = Session()
        commandIndex = UserCommands.getIndexFromCommandID(commandID)

        if row is None or row < 0:
            row = session.query(CommandVariants).filter(
                CommandVariants.usrcmdfk == commandIndex
            ).count()

        for n,v in kwargs.iteritems():
            if isinstance(v, str):
                kwargs[n] = unicode(v)

        variant = CommandVariants(usrcmdfk=commandIndex, row=row, **kwargs)
        session.add(variant)
        session.commit()

        out = variant.toButtonDict()
        session.close()
        return out

#___________________________________________________________________________________________________ reorderVariants
    @classmethod
    def reorderVariants(cls, variantIDs):
        session = Session()
        index   = 0
        out     = []
        for varID in variantIDs:
            varIndex = CommandVariants.getIndexFromVariantID(varID)
            variant  = session.query(CommandVariants).filter(CommandVariants.i == varIndex).first()
            if not variant:
                continue

            variant.row = index
            out.append(variant.variantID)
            index  += 1

        session.commit()
        session.close()
        return out

#___________________________________________________________________________________________________ modifyVariant
    @classmethod
    def modifyVariant(cls, variantID, **kwargs):
        session      = Session()
        variantIndex = CommandVariants.getIndexFromVariantID(variantID)
        result       = session.query(CommandVariants).filter(CommandVariants.i == variantIndex).first()

        if result is None:
            session.close()
            return {'error':'No Such Variant'}

        for n,v in kwargs.iteritems():
            if isinstance(v, str):
                v = unicode(v)
            setattr(result, n, v)

        session.commit()

        out = result.toButtonDict()
        session.close()
        return out

#___________________________________________________________________________________________________ deleteVariant
    @classmethod
    def deleteVariant(cls, variantID):
        session      = Session()
        variantIndex = CommandVariants.getIndexFromVariantID(variantID)
        result       = session.query(CommandVariants).filter(CommandVariants.i == variantIndex).first()

        if result is None:
            session.close()
            return {'id':variantID}

        session.delete(result)

        session.commit()
        session.close()

        return {'id':variantID}

#___________________________________________________________________________________________________ hasVariants
    @classmethod
    def hasVariants(cls, commandID):
        variants = cls.getVariants(commandID)
        if variants:
            return True
        return False
