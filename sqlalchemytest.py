from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarativce import declarative_base

Base=declarative_base()

class User(Base):
    __tablename__='user'


    id=Column(String(20),primary_key=True)
    name=Column(String(20))

engine=create_engine('mysql+mysqlconnector://root:password@localhost:3306/awesome')
DBSession=sessionmaker(bind=engine)
    
