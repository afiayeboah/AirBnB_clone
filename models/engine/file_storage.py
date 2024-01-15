#!/usr/bin/python3
"""
    Define class FileStorage Module
"""
import json
import models
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}
    classes = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        objects_dict = {key: val.to_dict()
                        for key, val in self.__objects.items()}

        with open(self.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        try:
            with open(self.__file_path, encoding="UTF8") as fd:
                objects_dict = json.load(fd)

            for key, val in objects_dict.items():
                class_name = val["__class__"]
                class_ = self.classes[class_name]
                self.__objects[key] = class_(**val)

        except FileNotFoundError:
            pass
