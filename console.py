#!/usr/bin/env python3

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter."""

    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program."""
        print("Quitting.")
        return True  # Signal to cmdloop to quit

    def do_EOF(self, args):
        """Exit on end-of-file character (Ctrl-D)."""
        print("Quitting.")
        return True

    def help_quit(self):
        """
        Help Method for quitting

        """
        print("Quit command to exit the program.")

    def help_eof(self):
        """
        Help Method for end of file

        """
        print("Exit on end-of-file character (Ctrl-D).")

    def emptyline(self):
        """Do nothing on empty input."""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel
        and saves it to the JSON file,
        prints the id. Ex: $ create BaseModel """
        if not args:
            print("** class name missing **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
