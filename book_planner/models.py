from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

Base = declarative_base() 

class Novel(Base):
    __tablename__='novels'
    id=Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    author= Column(String)
    status= Column(String)

    chapters = relationship("Chapter", back_populates="novel")
    characters=relationship("Character", back_populates="novel")
    themes=relationship("Theme", back_populates="novel")


class Chapter(Base):
    __tablename__="chapters"
    id=Column(Integer, primary_key=True)
    title=Column(String)
    number =Column(Integer)
    summary=Column(Text)
    content=Column(Text)
    novel_id=Column(Integer, ForeignKey("novels.id"))

    novel=relationship("Novel", back_populates="chapters")



class Character(Base):
    __tablename__='characters'
    id =Column(Integer,primary_key=True)
    name = Column(String)
    role=Column(String)
    description=Column(Text)
    novel_id=Column(Integer ,ForeignKey('novels.id'))

    novel= relationship("Novel",back_populates="characters")

class Theme(Base):
    __tablename__='themes'
    id=Column(Integer,primary_key=True)
    content =Column(Text)
    
    novel_id=Column(Integer,ForeignKey('novels.id'))

    novel=relationship("Novel",back_populates="themes")
    





