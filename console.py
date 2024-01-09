#!/usr/bin/python3
"""This module contains how to run python file in command
line(shell) or interractive mode
"""


import cmd, sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Commander interpreter for shell or interractive mode"""

    prompt = "(hbnb) "

    def do_baseModel(self, my_model):
        """Runs the base model class"""
        my_model = BaseModel()
        print(my_model)

    def do_quit(self, line):
        """Exit the console using the quit command"""
        return True

    def emptyline(self):
        """Prints an empty line if no argument is passes"""
        pass

    def do_EOF(self, line):
        """Exit the console using EOF (Ctrl-D)"""
        print()
        return True

if __name__ == "__main__":
    hbnb_console = HBNBCommand()

    if len(sys.argv) > 1:
        hbnb_console.onecmd(' '.join(sys.argv[1:]))
    elif sys.stdin.isatty():
        hbnb_console.cmdloop()
    else:
        for line in sys.stdin:
            hbnb_console.onecmd(line.strip())
