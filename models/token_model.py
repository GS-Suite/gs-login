from re import T
from models.user_model import User
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import Column, Integer, String, ForeignKey, exc
from sqlalchemy.sql.sqltypes import DateTime
from models.user_model import User
from fastapi_sqlalchemy import db
from models.base import Base
import datetime


class Token(Base):

    __tablename__ = "token"
    
    user_id = Column(Integer, ForeignKey(User.id), primary_key = True)
    token_value = Column(String)
    date_issued = Column(DateTime, default = datetime.datetime.now())


async def get_token_by_value(token):
    return db.session.query(Token).filter(
        Token.token_value == token,
    ).first()

async def get_token_by_user(user):
    return db.session.query(Token).filter(
        Token.user_id == user.id,
    ).first()

async def update_token(token, token_value):
    token.token_value = token_value, 
    token.date_issued = datetime.datetime.now()
    try:
        db.session.commit()
        return token
    except Exception as e:
        print(e)
        return False

async def create_token(user, token_value):
    token = Token(
        user_id = user.id,
        token_value = token_value,
        date_issued = datetime.datetime.now()
    )
    try:
        db.session.add(token)
        db.session.commit()
        return token
    except Exception as e:
        print(e)
        return False

async def delete_token(token):
    try:
        db.session.delete(token)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False