import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))

class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(250))
    lastname = Column(String(250))
    planet_born_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_fav_id = Column(Integer, ForeignKey('vehicle.id'))

class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    size = Column(Integer)
    
class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    size = Column(Integer)
    num_pasajeros = (Integer)

class Favorites(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    contador = Column(Integer)
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
