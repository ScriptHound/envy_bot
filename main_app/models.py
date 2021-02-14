from sqlalchemy import Column, String, ForeignKey, Unicode, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', String(100), nullable=False)
    username = Column('username', Unicode(150))

    def __init__(self, user_id, username) -> None:
        self.user_id = user_id
        self.username = username


class Films(Base):
    __tablename__ = 'films'

    id = Column('id', Integer, primary_key=True)
    film_name = Column('film_name', Unicode(300), nullable=False)
    date_created = Column('date_created', DateTime, nullable=False)
    user = Column('user', Integer, ForeignKey('users.id'))

    def __init__(self, film_name, date_created) -> None:
        self.film_name = film_name
        self.date_created = date_created
