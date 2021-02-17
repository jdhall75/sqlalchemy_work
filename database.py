from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, aliased
import os

db_name = "test.db"
# if os.path.exists(db_name):
#    os.remove(db_name)

engine = create_engine("sqlite:///test.db", echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()