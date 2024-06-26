#!/usr/bin/python3
"""Module for FileStorage class."""
import json


class FileStorage():
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(self.__objects, f, default=str)

    def reload(self):
        """Deserializes the JSON file to __objects ."""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                self.__objects = json.load(f)
        except Exception:
            pass
