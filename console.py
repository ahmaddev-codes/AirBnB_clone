#!/usr/bin/python3
"""Command line or interractive shell"""


import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


all_class = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
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

    def do_update(self, line):
        """Updates an instance based on the class anme and id
        Usage: update <class name> <id> <attribute name> "<attribute value>"
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

            if new_str not in storage.all().keys():
                print("** no instance found **")
            elif len(array) < 3:
                print("** attribute name missing **")
                return
            elif len(array) < 4:
                print("** value missing **")
                return
            else:
                setattr(storage.all()[new_str], array[2], array[3])
                storage.save()

    def do_count(self, line):
        """Print the count of all class instances
        Usage: <class name>.count()
        """
        parts = line.split(",")

        class_name, method_name = parts

        my_class = globals().get(class_name, None)

        if my_class is None:
            print("** class doesn't exist **")
            return

        method = getattr(my_class, method_name)

        if callable(method):
            all_values = storage.all().values()
            count = sum(1 for obj in all_values if isinstance(obj, my_class))
            print(count)

    def default(self, line):
        if line is None:
            return
        regex_filepath = "pattern.txt"

        with open(regex_filepath, "r", encoding="utf8") as file:
            cmdPattern = file.readline().strip()
            paramsPattern = file.readline().strip()

        match = re.match(cmdPattern, line)

        if not match:
            super().default(line)
            return

        mName, method, params = match.groups()

        m = re.match(paramsPattern, params)
        params = [item for item in m.groups() if item] if m else []

        cmd = " ".join([mName] + params)

        if method == 'all':
            return self.do_all(cmd)

        if method == 'count':
            return self.do_count(cmd)

        if method == 'show':
            return self.do_show(cmd)

        if method == 'destroy':
            return self.do_destroy(cmd)

        if method == 'update':
            return self.do_update(cmd)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
