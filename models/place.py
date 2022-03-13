#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

if getenv("HBNB_TYPE_STORAGE") == 'db':
    association_table = Table(
        'place_amenity',
        Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'), primary_key = True, nullable = False),
        Column('amenities_id', String(60), ForeignKey('amenities.id'), primary_key = True, nullable = False)
    )

    class Place(BaseModel, Base):
        """ A place to stay """
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        amenities = relationship('Amenity', secondary = 'place_amenity', viewonly=False, back_populates = 'place_amenities')
        reviews = relationship("Review", backref = "place", cascade='all, delete')

else:
    class Place(BaseModel):
        """This is the class for Place
            Attributes:
            city_id: city id
            user_id: user id
            name: name input
            description: string of description
            number_rooms: number of room in int
            number_bathrooms: number of bathrooms in int
            max_guest: maximum guest in int
            price_by_night:: pice for a staying in int
            latitude: latitude in flaot
            longitude: longitude in float
            amenity_ids: list of Amenity ids
        """
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ Get a list of all linked reviews """
            from models import storage
            review_list = []
            for review in storage.all(Review).values():
                if review.place_id ==self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """ Get linked amenities """
            from models import storage
            amenity_list = []
            for amenity in storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
