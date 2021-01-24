from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime, String
from db import db
import datetime


Base = declarative_base()


class UserModel(Base):

    __tablename__ = 'user'
    
    id = Column(String, primary_key=True)
    username = Column(String, unique = True)
    password = Column(String)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    date_joined = Column(DateTime, default = datetime.datetime)