#!/usr/bin/python3
"""
City Module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class representing a city with relevant details.

    Attributes:
        state_id (str): The identifier of the associated state.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
