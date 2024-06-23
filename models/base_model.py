"""Module for class BaseModel"""
import uuid
import datetime


class BaseModel():
    """Defines all common attributes/methods for other classes."""

    def __init__(self):
        """
        Constructor for BaseModel's instances.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

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
