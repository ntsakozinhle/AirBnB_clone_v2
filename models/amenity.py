#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """ This class represents an amenity"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
