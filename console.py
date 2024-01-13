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

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
