# CommandCategories.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

from sqlalchemy import BigInteger
from sqlalchemy import Column
from sqlalchemy import Unicode

from alloy.data.model import Base

#___________________________________________________________________________________________________ CommandCategories
class CommandCategories(Base):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

    __tablename__  = 'commandcategories'
    __table_args__ = {'sqlite_autoincrement': True}

    i       = Column(BigInteger, primary_key=True)
    label   = Column(Unicode, default=u'My Group')

    _ID_PREFIX = u'cat'

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: categoryID
    @property
    def categoryID(self):
        return CommandCategories._ID_PREFIX + unicode(self.i)

#===================================================================================================
#                                                                                     P U B L I C

#___________________________________________________________________________________________________ GS: getCategoryIDFromIndex
    @classmethod
    def getCategoryIDFromIndex(cls, index):
        return CommandCategories._ID_PREFIX + unicode(index)

#___________________________________________________________________________________________________ GS: getIndexFromCategoryID
    @classmethod
    def getIndexFromCategoryID(cls, categoryID):
        return int(categoryID[len(CommandCategories._ID_PREFIX):])

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
