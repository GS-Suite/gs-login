from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import DateTime
from fastapi_sqlalchemy import db
from models.base import Base
import datetime


class User(Base):

    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique = True)
    password = Column(String)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    date_joined = Column(DateTime, default = datetime.datetime.now())


async def create_user(user):
    db_user = User(
        username = user.username,
        password = user.password,
        email = user.email,
        first_name = user.first_name,
        last_name = user.last_name,
    )
    try:
        db.session.add(db_user)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False

async def get_user_by_username(username):
    return db.session.query(User).filter(
        User.username == username
    ).first()