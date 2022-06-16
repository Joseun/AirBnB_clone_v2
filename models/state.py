#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
	""" State class """
	__tablename__ = 'states'
	name =  Column(String(128), nullable=False)
	cities = []
	
	if getenv('HBNB_TYPE_STORAGE') == 'db':
		cities = relationship("City",  back_populates="state",
							 cascade="all, delete-orphan", single_parent=True)
	
	if getenv('HBNB_TYPE_STORAGE') != 'db':
		@property
		def cities(self):
			"""" Getter attribute to retrieve City object """
			from models import storage
			from models.city import City

			all_objects = storage.all(City)
			city_list = [v for k, v in all_objects.items()
			 		     if v.state_id == self.id]
			return city_list
