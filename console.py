#!/usr/bin/python3
"""
console.py - Module
Command interpreter for HBNB project using cmd module.
"""

import cmd
import shlex
import json
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
    valid_classes = ["BaseModel", "User", "Amenity",
                     "Place", "Review", "State", "City"]

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
        print("quit - Exit the program")
        print("EOF - Exit the program")
        print("help - Show this help message")
        print("<class name>.all() - Print all instances of a class")
        print("<class name>.show(<id>) - Show an instance by ID")
        print("<class name>.destroy(<id>) - Destroy an instance by ID")
        print("<class name>.create() - Create a new instance of a class")

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
            'create': self.do_create,
            'update': self.do_update
        }

        if cmd_met in method_dict.keys():
            if cmd_met != "update":
                return method_dict[cmd_met](f"{cls_nm} {e_arg}")
            else:
                try:
                    obj_id, attr_val = e_arg.split(', ')
                    return method_dict[cmd_met]
                    (f"{cls_nm} {obj_id} {attr_val}")
                except ValueError:
                    print("** Invalid syntax for update command **")
        else:
            print(f"** Unknown syntax: {arg} **")

    def do_create(self, arg):
        """
        Creates a new instance of a class, saves it, and prints the id.
        """
        commands = shlex.split(arg)
        if not commands or commands[0] not in self.valid_classes:
            print("** class name missing **" if not commands
                  else "** class doesn't exist **")
            return

        new_instance = eval(f"{commands[0]}()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string rep of an instance based on the class name and id.
        """
        commands = shlex.split(arg)
        if not commands or commands[0] not in self.valid_classes:
            print("** class name missing **" if not commands
                  else "** class doesn't exist **")
            return
        if len(commands) < 2:
            print("** instance id missing **")
            return

        key = f"{commands[0]}.{commands[1]}"
        instances = storage.all()
        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        commands = shlex.split(arg)
        if not commands or commands[0] not in self.valid_classes:
            print("** class name missing **" if not commands
                  else "** class doesn't exist **")
            return
        if len(commands) < 2:
            print("** instance id missing **")
            return

        key = f"{commands[0]}.{commands[1]}"
        instances = storage.all()
        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        commands = shlex.split(arg)
        instances = storage.all()
        if not commands or commands[0] not in self.valid_classes:
            print("** class doesn't exist **" if not commands else "")
            return

        result = [str(obj) for key, obj in instances.items()
                  if key.startswith(commands[0])]
        print(result)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        """
        commands = shlex.split(arg)
        if not commands or commands[0] not in self.valid_classes:
            print("** class name missing **" if not commands
                  else "** class doesn't exist **")
            return
        if len(commands) < 2:
            print("** instance id missing **")
            return

        key = f"{commands[0]}.{commands[1]}"
        instances = storage.all()
        if key not in instances:
            print("** no instance found **")
            return

        if len(commands) < 3:
            print("** attribute name missing **")
            return
        if len(commands) < 4:
            print("** value missing **")
            return

        attribute = commands[2]
        value = commands[3].strip("'\"")

        obj = instances[key]
        setattr(obj, attribute, value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
