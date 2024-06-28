#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
