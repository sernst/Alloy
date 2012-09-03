# CommandCategories.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Unicode

from alloy.data.model import Base

#___________________________________________________________________________________________________ CommandCategories
class CommandCategories(Base):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

    __tablename__  = 'commandcategories'
    __table_args__ = {'sqlite_autoincrement': True}

    i       = Column(Integer, primary_key=True)
    label   = Column(Unicode, default=u'My Group')
    column1 = Column(Unicode, default=u'Column 1')
    column2 = Column(Unicode, default=u'Column 2')
    column3 = Column(Unicode, default=u'Column 3')
    column4 = Column(Unicode, default=u'Column 4')

    _ID_PREFIX = u'cat'

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: categoryID
    @property
    def categoryID(self):
        return CommandCategories._ID_PREFIX + unicode(self.i)

#===================================================================================================
#                                                                                     P U B L I C

#___________________________________________________________________________________________________ toDict
    def toDict(self):
        return {
            'id':self.categoryID,
            'label':self.label,
            'column1':self.column1,
            'column2':self.column2,
            'column3':self.column3,
            'column4':self.column4,
        }

#___________________________________________________________________________________________________ GS: getCategoryIDFromIndex
    @classmethod
    def getCategoryIDFromIndex(cls, index):
        return CommandCategories._ID_PREFIX + unicode(index)

#___________________________________________________________________________________________________ GS: getIndexFromCategoryID
    @classmethod
    def getIndexFromCategoryID(cls, categoryID):
        if isinstance(categoryID, CommandCategories):
            categoryID = categoryID.categoryID
        elif isinstance(categoryID, dict):
            categoryID = categoryID['id']

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
