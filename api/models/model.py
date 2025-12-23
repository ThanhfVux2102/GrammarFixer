from sqlalchemy import Column, Integer, String,ForeignKey
from ..database import Base

class TextModel(Base):
    __tablename__="texts"
    id = Column(Integer,primary_key=True,index=True)
    body = Column(String)
class ResponseModel(Base):
    __tablename__="responses"
    id =Column(Integer,primary_key=True,index=True)
    body = Column(String)
