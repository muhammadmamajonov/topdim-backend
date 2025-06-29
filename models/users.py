from database import Base
from sqlalchemy import Column, String, Integer, Boolean


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    is_active = Column(Boolean, server_default="t")
    tg_id = Column(Integer)
    phone_number = Column(String(17))

    def __str__(self):
        return self.first_name + " " + self.last_name
    