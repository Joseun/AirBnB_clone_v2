#!/usr/bin/python3
""" Amenities Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
	""" The amenity class, contains name of amenities """
	__tablename__ = 'amenities'
	name =  Column(String(128), nullable=False, unique=True)
	if getenv("HBNB_TYPE_STORAGE") == "db":
		place_amenities = relationship("Place", secondary = 'place_amenity',
									   viewonly=False, 
									   back_populates = 'amenities')
