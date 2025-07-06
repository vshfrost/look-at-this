from sqlalchemy import Integer, Column, String

from database.tools.sqlalchemy import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)