#!/usr/bin/python3
"""
console.py - Module
Command interpreter for HBNB project using cmd module.
"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class.
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Amenity", "Place", "Review", "State", "City"]

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        print()
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_help(self, arg):
        """
        Custom help message.
        """
        print("Available commands:")
        print("  quit - Exit the program")
        print("  EOF - Exit the program")
        print("  help - Show this help message")
        print("  <class name>.all() - Print all instances of a class")
        print("  <class name>.show(<id>) - Show an instance by ID")
        print("  <class name>.destroy(<id>) - Destroy an instance by ID")
        print("  <class name>.count() - Count instances of a class")
        print("  <class name>.update(<id>, <attribute>, <value>) - Update an instance")
        print()

    def default(self, arg):
        """
        Default behavior for cmd module when input is invalid.
        """
        commands = shlex.split(arg)
        cls_nm = commands[0] if commands else ""

        if cls_nm not in self.valid_classes:
            print(f"** Unknown syntax: {arg} **")
            return

        command = commands[1].split('(') if len(commands) > 1 else ["", ""]
        cmd_met = command[0]
        e_arg = command[1].split(')')[0] if len(command) > 1 else ""

        method_dict = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'count': self.do_count,
            'update': self.do_update
        }

        if cmd_met in method_dict.keys():
            if cmd_met != "update":
                return method_dict[cmd_met](f"{cls_nm} {e_arg}")
            else:
                try:
                    obj_id, attr_val = e_arg.split(', ')
                    return method_dict[cmd_met](f"{cls_nm} {obj_id} {attr_val}")
                except ValueError:
                    print("** Invalid syntax for update command **")
        else:
            print(f"** Unknown syntax: {arg} **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
