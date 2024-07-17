import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    post_code = Column(String(250), nullable=False)
    street_name = Column(String(250))
    street_number = Column(String(250))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_to_id = Column(String(250), nullable=False)

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    user_to_id = Column(String(250), nullable=False)
   
    
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
