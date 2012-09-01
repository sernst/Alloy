# __init__.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from alloy.AlloyEnvironment import AlloyEnvironment
from alloy.data.model.UserCommands import UserCommands
from alloy.data.model.CommandCategories import CommandCategories

engine  = create_engine(AlloyEnvironment.getDatabaseURL())
Base    = declarative_base(bind=engine)
Session = scoped_session(sessionmaker(bind=engine))

Base.metadata.create_all()
