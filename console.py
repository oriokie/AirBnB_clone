#!/usr/bin/python3
"""
console.py is the entry point of the command
interpreter
"""
import cmd


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
        new_instance = eval(args)()
        new_instance.save()
        print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
