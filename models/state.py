#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.city import City
import models

import shlex


class State(BaseModel):
    """ State class """

    if models.env_hbnb == "db":
        
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
        
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.env_hbnb != "db":

        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)

            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            
            return city_list

    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete, delete-orphan',
                          backref='state')

    @property
    def cities(self):
        objs = models.storage.all()
        list_cities = []
        rs = []

        for key in objs:
            city = key.replace('.', ' ')
            city = shlex.split(city)

            if city[0] == 'City':
                list_cities.append(objs[key])

        for val in list_cities:
            if val.state_id == self.id:
                rs.append(val)

        return rs
    """
