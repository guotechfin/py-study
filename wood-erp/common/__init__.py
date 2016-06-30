from sqlalchemy_ctl import Base
from sqlalchemy_ctl import DBSession
from sqlalchemy_ctl import engine

def create_table(table_name=""):
    if table_name == "":
        Base.metadata.create_all(engine)
    else:
        Base.metadata.tables[table_name].create(
                bind=engine, checkfirst=True)

def drop_table(table_name=""):
    if table_name == "":
        Base.metadata.drop_all(engine)
    else:
        Base.metadata.tables[table_name].drop(
                bind=engine, checkfirst=True)
