# from models.user_model import User
from sqlalchemy.dialects.postgresql import insert, JSON
from sqlalchemy import Column, Integer, String, ForeignKey, exc
from sqlalchemy.sql.sqltypes import DateTime

from fastapi_sqlalchemy import db
from models.base import Base
import datetime
import string
import random
import re


class Classroom(Base):
    __tablename__ = "classroom"

    id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(Integer)
    class_name = Column(String)
    # enrolled_users = Column(JSON)
    created_time = Column(DateTime, default=datetime.datetime.now())
    unique_id = Column(Integer)


async def id_generator(class_name, created_time):
    size = 9
    charSet = string.ascii_lowercase + string.ascii_uppercase + \
        string.digits + class_name + created_time
    charSet = re.sub(r"\s+", "", charSet)
    charSet = charSet.strip()
    return await ''.join(random.choice(charSet) for _ in range(size))


async def create_classroom(user_id, classroom):
    new_class = Classroom(
        creator_id=user_id,
        class_name=classroom.class_name,
        created_time=datetime.datetime.now(),
        unique_id=id_generator(
            class_name=classroom.class_name,
            created_time=str(datetime.datetime.now())
        )
    )
    try:
        db.session.add(new_class)
        db.session.commit()
        # print('Committed')
        return True
    except Exception as e:
        print(e)
        return False
