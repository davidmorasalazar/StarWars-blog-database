import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Favorites(Base): 
    __tablename__ = 'Favorites'
    User_ID = Column(Integer,primary_key=True)
    # FavoritesPlanet_ID = Column(Integer)
    # FavoritesPerson_ID = Column(Integer)


class CardPerson(Base):
    __tablename__ = 'CardPerson'
    #Siempre usar guion bajo cuando se hace una tabla
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Person_name = Column(String(250), nullable=False)
    Hair_color = Column(String(250))
    Skin_color = Column(String(250))
    Gender  = Column(String(250))
    Birth_year = Column(Integer, nullable=False)
    height = Column(Integer)
class CardPlanet(Base):
    __tablename__ = 'CardPlanet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Planet_name = Column(String(250), nullable=False)
    Population = Column(Integer)
    Terrain = Column(String(250))
    Climate = Column(String(250))
    Orbital_Period = Column(Integer)
    #person_id = Column(Integer, ForeignKey('CardPerson.id'))
    person = relationship(CardPerson)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram2.png')