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

    def help_EOF(self):
        """
        Help Method for end of file

        """
        print("Exit on end-of-file character (Ctrl-D).")

    def emptyline(self):
        """Do nothing on empty input."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
