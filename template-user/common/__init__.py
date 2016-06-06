from sqlalchemy_ctl import Base
from sqlalchemy_ctl import DBSession
from sqlalchemy_ctl import engine

def create_table():
    Base.metadata.create_all(engine)

def drop_table():
    Base.metadata.drop_all(engine)
