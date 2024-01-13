#!/usr/bin/python3
"""
Amenity Module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class representing an amenity with a specified name.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
