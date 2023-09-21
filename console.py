#!/usr/bin/env python3
"""basic console program - airbnb clone"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        Exit the program on EOF (Ctrl+D)
        """
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """
        Do nothing on an empty line
        """
        pass
    
    def do_create(self, line):
        """
        Usage: katcreayi <class> <key1> = <value1> <key2> = <value2>...
	line: halawah halawah
	"""

if __name__ == "__main__":
    HBNBCommand().cmdloop()
