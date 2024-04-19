#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

from models.base_model import BaseModel, Base
from models.place import place_amenity


class Amenity(BaseModel, Base):
    '''Amenity class'''

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary=place_amenity)
