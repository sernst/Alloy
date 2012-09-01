# UserCommands.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

from sqlalchemy import BigInteger
from sqlalchemy import Column
from sqlalchemy import Unicode
from sqlalchemy import UnicodeText

from alloy.data.model import Base

#___________________________________________________________________________________________________ UserCommands
class UserCommands(Base):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

    __tablename__  = 'usercommands'
    __table_args__ = {'sqlite_autoincrement': True}

    i       = Column(BigInteger, primary_key=True)
    groupfk = Column(BigInteger, default=None)
    label   = Column(Unicode, default=u'My Command')
    info    = Column(Unicode, default=u'')
    command = Column(UnicodeText, default=u'')

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
