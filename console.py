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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
