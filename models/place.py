#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    
    user = relationship("User", back_populates="places")
    city = relationship("City", back_populates="places")

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amaenity = Table(
                'place_amenity', Base.emtadata,
                Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False)
                Column('amenity_id', String(60), ForeignKey('amenity.id'), primary_key=True, nullable=False)
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)


    @property
    def reviews(self):
        from models import storage
        review_list = []
        all_reviews = storage.all(Review)
        for review in all_reviews.values():
            if review.place_id == self.id:
                review_list.append(review)
        return review_list
