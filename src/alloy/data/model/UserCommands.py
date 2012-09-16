# UserCommands.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import UnicodeText

from alloy.AlloyEnvironment import AlloyEnvironment
from alloy.data.model import Base
from alloy.data.model.CommandCategories import CommandCategories

#___________________________________________________________________________________________________ UserCommands
class UserCommands(Base):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

    __tablename__  = 'usercommands'
    __table_args__ = {'sqlite_autoincrement': True}

    i          = Column(Integer, primary_key=True)
    categoryfk = Column(Integer, default=None)
    column     = Column(Integer, default=1)
    row        = Column(Integer, default=0)
    label      = Column(Unicode, default=u'My Command')
    info       = Column(Unicode, default=u'')
    icon       = Column(Unicode, default=AlloyEnvironment.DEFAULT_ICON)
    language   = Column(Unicode, default=u'python')
    location   = Column(Unicode, default=u'maya')
    script     = Column(UnicodeText, default=u'')

    _ID_PREFIX = u'cmd'

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: variants
    @property
    def variants(self):
        from alloy.data.model import Session
        from alloy.data.model.CommandVariants import CommandVariants
        session = Session()
        result = session.query(CommandVariants).filter(CommandVariants.usrcmdfk == self.i).all()

        out = []
        for r in result:
            out.append(r.toButtonDict())

        session.close()
        return out

#___________________________________________________________________________________________________ GS: commandID
    @property
    def commandID(self):
        return UserCommands._ID_PREFIX + str(self.i)

#===================================================================================================
#                                                                                     P U B L I C

#___________________________________________________________________________________________________ toButtonDict
    def toButtonDict(self):
        return {
            'id':self.commandID,
            'column':self.column,
            'row':self.row,
            'categoryID':CommandCategories.getCategoryIDFromIndex(self.categoryfk),
            'label':self.label,
            'info':self.info,
            'icon':self.icon,
            'hasVariants':len(self.variants) > 0
        }

#___________________________________________________________________________________________________ toDict
    def toDict(self):
        return {
            'id':self.commandID,
            'column':self.column,
            'row':self.row,
            'categoryID':CommandCategories.getCategoryIDFromIndex(self.categoryfk),
            'label':self.label,
            'info':self.info,
            'icon':self.icon,
            'language':self.language,
            'location':self.location,
            'script':self.script,
            'variants':self.variants
        }

#___________________________________________________________________________________________________ GS: getCommandIDFromIndex
    @classmethod
    def getCommandIDFromIndex(cls, index):
        return UserCommands._ID_PREFIX + unicode(index)

#___________________________________________________________________________________________________ GS: getIndexFromCommandID
    @classmethod
    def getIndexFromCommandID(cls, commandID):
        return int(commandID[len(UserCommands._ID_PREFIX):])

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
