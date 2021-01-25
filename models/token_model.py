from models.user_model import User
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from models.user_model import User
from fastapi_sqlalchemy import db
from models.base import Base
import datetime


class Token(Base):

    __tablename__ = "token"
    
    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, ForeignKey(User.id), primary_key = True)
    token_value = Column(String)
    date_issued = Column(DateTime, default = datetime.datetime.now())


async def get_token_by_value(token):
    return db.session.query(Token).filter(
        Token.token_value == token.token_value,
    ).first()

async def get_token_by_user(user):
    return db.session.query(Token).filter(
        Token.user_id == user.id,
    ).first()

async def refresh_token(user, token_value):
    
    stmt = insert(Token).values(
        user_id = user.id, 
        token_value = token_value, 
        date_issued = datetime.datetime.now()
    )
    stmt.on_conflict_do_update(
        index_element = [Token.user_id]
    )
    try:
        db.session.execute(stmt)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False