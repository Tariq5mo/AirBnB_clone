#!/usr/bin/python3
"""Module for FileStorage class."""
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        objs = {}
        for key in FileStorage.__objects.keys():
            objs[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(objs, f, default=str)

    def reload(self):
        """Deserializes the JSON file to __objects ."""
        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                    di = json.load(f)
                    for key, value in di.items():
                        classname = di[key]["__class__"]
                        classs = eval(classname)
                        instan = classs(**value)
                        di[key] = instan
                    FileStorage.__objects = di
            except Exception:
                pass
