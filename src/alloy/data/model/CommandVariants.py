# CommandVariants.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode
from sqlalchemy import UnicodeText

from alloy.data.model import Base
from alloy.data.model.UserCommands import UserCommands

#___________________________________________________________________________________________________ CommandVariants
class CommandVariants(Base):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

    __tablename__  = 'usercommandvariants'
    __table_args__ = {'sqlite_autoincrement': True}

    i          = Column(Integer, primary_key=True)
    usrcmdfk   = Column(Integer, default=None)
    row        = Column(Integer, default=0)
    label      = Column(Unicode, default=u'My Command')
    info       = Column(Unicode, default=u'')
    icon       = Column(Unicode, default=u'8.jpg')
    language   = Column(Unicode, default=u'python')
    location   = Column(Unicode, default=u'maya')
    script     = Column(UnicodeText, default=u'')

    _ID_PREFIX = u'cmdvar'

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: variantID
    @property
    def variantID(self):
        return CommandVariants._ID_PREFIX + str(self.i)

#===================================================================================================
#                                                                                     P U B L I C

#___________________________________________________________________________________________________ toButtonDict
    def toButtonDict(self):
        return {
            'id':self.variantID,
            'commandID':UserCommands.getCommandIDFromIndex(self.usrcmdfk),
            'label':self.label,
            'info':self.info,
            'icon':self.icon
        }

#___________________________________________________________________________________________________ toDict
    def toDict(self):
        return {
            'id':self.variantID,
            'commandID':UserCommands.getCommandIDFromIndex(self.usrcmdfk),
            'label':self.label,
            'info':self.info,
            'icon':self.icon,
            'language':self.language,
            'location':self.location,
            'script':self.script
        }

#___________________________________________________________________________________________________ GS: getVariantIDFromIndex
    @classmethod
    def getVariantIDFromIndex(cls, index):
        return CommandVariants._ID_PREFIX + unicode(index)

#___________________________________________________________________________________________________ GS: getIndexFromVariantID
    @classmethod
    def getIndexFromVariantID(cls, variantID):
        return int(variantID[len(CommandVariants._ID_PREFIX):])

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
