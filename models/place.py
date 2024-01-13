#!/usr/bin/python3
"""
Place Module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class representing a place with various details.

    Attributes:
        city_id (str): The identifier of the city associated with the place.
        user_id (str): The identifier of the user who owns the place.
        name (str): The name of the place.
        description (str): A brief description of the place.
        number_rooms (int): The number of rooms available in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests accommodated.
        price_by_night (int): The nightly price of the place.
        latitude (float): The latitude coordinates of the place.
        longitude (float): The longitude coordinates of the place.
        amenity_ids (list): A list of identifiers for associated amenities.
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
