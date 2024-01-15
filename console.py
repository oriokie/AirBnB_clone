#!/usr/bin/python3
"""
console.py is the entry point of the command
interpreter

"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models

classes = {'BaseModel': BaseModel, "User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter."""

    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, args):
        """Exit on end-of-file character (Ctrl-D)."""
        return True

    def emptyline(self):
        """Do nothing on empty input."""
        pass

    def do_create(self, args):
        """
        Create a new instance of BaseModel, saves it
        to the JSON file and prints the id
        """
        if not args:
            print("** class name missing **")
            return
        cmd_args = args.split()
        if cmd_args[0] not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[cmd_args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id
        Ex: $ show BaseModel 1234-1234-1234
        """
        cmd_args = arg.split()
        if not cmd_args:
            print("** class name missing **")
            return False
        if cmd_args[0] in classes:
            if len(cmd_args) > 1:
                key = f"{cmd_args[0]}.{cmd_args[1]}"
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)

        Args:
            arg (str): The command-line argument containing the class name
            and instance id.

        Example:
            $ destroy BaseModel 1234-1234-1234.
        """
        cmd_args = arg.split()
        if not cmd_args:
            print("** class name missing **")
        elif cmd_args[0] in classes:
            if len(cmd_args) > 1:
                key = f"{cmd_args[0]}.{cmd_args[1]}"
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name.

        Args:
            arg (str): The command-line argument

        Example:
            $ all BaseModel or $ all.
        """
        cmd_args = arg.split()
        if not cmd_args or cmd_args[0] not in classes:
            print("** class doesn't exist **")
            return False
        if cmd_args[0] in classes:
            obj_dict = models.storage.all(classes[cmd_args[0]])
        else:
            obj_dict = models.storage.all()

        obj_list = [str(obj_dict[key]) for key in obj_dict]

        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
