# __init__.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from alloy.AlloyEnvironment import AlloyEnvironment

if AlloyEnvironment.DEVELOPMENT:
    print 'Creating engine: ' + str(AlloyEnvironment.getDatabaseURL())


try:
    engine = create_engine(AlloyEnvironment.getDatabaseURL())
except Exception, err:
    print 'DATABASE FAILURE: Unable to create engine for database'
    print 'Url:', AlloyEnvironment.getDatabaseURL()
    raise

try:
    Base = declarative_base(bind=engine)
except Exception, err:
    print 'DATABASE FAILURE: Unable to create database engine Base.'
    print 'Url:', AlloyEnvironment.getDatabaseURL()
    print 'Engine:', engine
    raise

try:
    Session = scoped_session(sessionmaker(bind=engine))
except Exception, err:
    print 'DATABASE FAILURE: Unable to create bound Session.'
    print 'Url:', AlloyEnvironment.getDatabaseURL()
    print 'Engine:', engine
    print 'Base:', Base
    raise

try:
    from alloy.data.model.UserCommands import UserCommands
    from alloy.data.model.CommandCategories import CommandCategories
    from alloy.data.model.CommandVariants import CommandVariants
except Exception, err:
    print 'DATABASE FAILURE: Unable to import models.'
    print 'Url:', AlloyEnvironment.getDatabaseURL()
    print 'Engine:', engine
    print 'Base:', Base
    print 'Sesssion:', Session
    raise

try:
    Base.metadata.create_all()
except Exception, err:
    print 'DATABASE FAILURE: Unable to create models.'
    print 'Url:', AlloyEnvironment.getDatabaseURL()
    print 'Engine:', engine
    print 'Base:', Base
    print 'Sesssion:', Session
    raise
