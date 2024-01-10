#!/usr/bin/python3
"""Command line or interractive shell"""


import cmd
from models.base_model import BaseModel
from models import storage


all_class = {
    "BaseModel": BaseModel
}


class HBNBCommand(cmd.Cmd):
    """Commander interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Prints an empty line if no argument is passes"""
        pass

    def do_EOF(self, line):
        """Exit the console using EOF (Ctrl-D)"""
        print()
        return True

    def do_create(self, line):
        """Creates a new instances of a class"""
        if line:
            try:
                glob_cls = globals().get(line, None)
                obj = glob_cls()
                obj.save()
                print(obj.id)  # print the id
                print()
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of a class instance
        based on the class name and id
        """
        array = line.split()

        if len(array) < 1:
            print("** class name missing **")
        elif array[0] not in all_class:
            print("** class doesn't exist")
        elif len(array) < 2:
            print("** instance id is missing **")
        else:
            new_str = f"{array[0]}.{array[1]}"

            if new_str not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[new_str])
                print()

    def do_destroy(self, line):
        """Deletes an instance
        based on the class name and id
        """
        array = line.split()

        if len(array) < 1:
            print("** class name missing **")
        elif array[0] not in all_class:
            print("** class doesn't exist")
        elif len(array) < 2:
            print("** instance id is missing **")
        else:
            new_str = f"{array[0]}.{array[1]}"

            if new_str not in storage.all():
                print("** no instance found **")
            else:
                # Delete the instance
                del storage.all()[new_str]
                # Save the changes to the file
                storage.save()

    def do_all(self, line):
        """Prints string representation of all instances"""
        objects = []

        if line == "":
            print([str(value) for key, value in storage.all().items()])
        else:
            array = line.split(" ")

            if array[0] not in all_class:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    my_class = key.split('.')

                    if my_class[0] == array[0]:
                        objects.append(str(value))

                print(objects)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
