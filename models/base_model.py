#!/usr/bin/python3
"""Module for class BaseModel"""
import uuid
import datetime
import models


class BaseModel():
    """Defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """
        Constructor for BaseModel's instances.
        """
        if len(kwargs) != 0:
            for key in kwargs:
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    kwargs[key] = datetime.datetime.fromisoformat(kwargs[key])
                self.__setattr__(key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """The str of the class."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing
        all keys/values of __dict__of the instance.
        """
        di = self.__dict__.copy()
        di["__class__"] = self.__class__.__name__
        di["created_at"] = self.created_at.isoformat()
        di["updated_at"] = self.updated_at.isoformat()
        return di
