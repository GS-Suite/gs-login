# from models.user_model import User
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import DateTime
from helpers import classroom_helpers
from fastapi_sqlalchemy import db
from models.base import Base
import datetime


class Classroom(Base):
    __tablename__ = "classroom"

    id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(Integer)
    class_name = Column(String)
    # enrolled_users = Column(JSON)
    created_time = Column(DateTime, default=datetime.datetime.now())
    unique_id = Column(Integer)

async def create_classroom(user_id, classroom):
    new_class = Classroom(
        creator_id = user_id,
        class_name = classroom.class_name,
        created_time = datetime.datetime.now(),
        unique_id = await classroom_helpers.id_generator(
            class_name = classroom.class_name,
            created_time = str(datetime.datetime.now())
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
