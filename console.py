#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """the entry point of the command interpreter."""

    prompt = "(hbnb) "

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
        if args[0] == "BaseModel":
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
        if args[0] != "BaseModel":
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
        """Prints the string representation of an instance."""
        if line == "":
            print("** class name missing **")
            return
        args = line.split()
        if args[0] != "BaseModel":
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
