from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from models.user_model import User
from fastapi_sqlalchemy import db
from models.base import Base
import datetime

class Token(Base):

    __tablename__ = "token"
    
    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, ForeignKey(User.id))
    token_value = Column(String)
    date_issued = Column(DateTime, default = datetime.datetime.now())


async def get_token_by_value(token):
    return db.session.query(Token).filter(
        Token.token_value == token,
    ).first()


async def get_token_by_user(user_id):
    return db.session.query(Token).filter(
        Token.user_id == user_id,
    ).first()


async def create_token(user_id, token_value):
    token = Token(
        user_id = user_id,
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


async def refresh_token(user_id, new_token_value):
    ''' delete tokens '''
    tokens = db.session.query(Token).filter(
        Token.user_id == user_id,
    ).all()
    #print(tokens)
    for i in tokens:
        db.session.delete(i)
    new_token = Token(
        user_id = user_id,
        token_value = new_token_value,
        date_issued = datetime.datetime.now()
    )
    ''' add tokens '''
    try:
        db.session.add(new_token)
        db.session.commit()
        return new_token
    except Exception as e:
        db.session.rollback()
        print(e)
        return False
