#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""
import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
import models
import json


class HBNBCommand(cmd.Cmd):
    """the entry point of the command interpreter."""

    prompt = "(hbnb) "

    def check(self, cls=""):
        """Check if class name is exist.."""
        for key in models.FileStorage._FileStorage__objects:
            if cls in key:
                return True
        return False

    def do_EOF(self, line):
        """Exit the program."""
        print("")
        return True

    def do_quit(self, line):
        """Exit the program."""
        return True

    def emptyline(self):
        """Pass."""
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        if line == "":
            print("** class name missing **")
            return
        args = line.split()
        cls_list = ["BaseModel", "User", "State", "City",
                    "Amenity", "Place", "Review"]
        if args[0] in cls_list:
            classs = eval(args[0])
            instance = classs()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance."""
        if line == "":
            print("** class name missing **")
            return
        args = line.split()
        if self.check(args[0]) is not True:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in models.FileStorage._FileStorage__objects:
            print("** no instance found **")
            return
        else:
            obj = models.FileStorage._FileStorage__objects[key]
            print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        if line == "":
            print("** class name missing **")
            return
        args = line.split()
        if self.check(args[0]) is not True:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in models.FileStorage._FileStorage__objects:
            print("** no instance found **")
            return
        else:
            del models.FileStorage._FileStorage__objects[key]
            models.FileStorage.save(self)

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        li = []
        args = line.split()
        dic = models.FileStorage._FileStorage__objects
        if line != "" and args[0] != "":
            if self.check(args[0]) is not True:
                print("** class doesn't exist **")
                return
            cls = args[0]
            for key in dic:
                if cls in key:
                    obj = dic[key]
                    li.append(obj.__str__())
            print(li)
        else:
            for key in dic:
                obj = dic[key]
                li.append(obj.__str__())
            print(li)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        di = models.FileStorage._FileStorage__objects
        if line == "":
            print("** class name missing **")
            return
        args = line.split()
        if self.check(args[0]) is not True:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in models.FileStorage._FileStorage__objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = di[key]
        setattr(obj, args[2], json.loads(args[3]))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
