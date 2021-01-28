from models.user_model import User
from sqlalchemy.dialects.postgresql import insert, JSON
from sqlalchemy import Column, Integer, String, ForeignKey, exc
from sqlalchemy.sql.sqltypes import DateTime

from fastapi_sqlalchemy import db
from models.base import Base
import datetime


class Classroom(Base):
    __tablename__ = "classroom"

    id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    class_name = Column(String)
    # enrolled_users = Column(JSON)
    created_time = Column(DateTime, default=datetime.datetime.now())


async def create_classroom(classroom, user_id):
    new_class = Classroom(
        creator_id = user_id,
        class_name = classroom.class_name
    )
    try:
        db.session.add(new_class)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False
