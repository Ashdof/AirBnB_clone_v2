#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import shlex


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Get list of objects

        Description:
        This method fetches a list of objects of a type of class
        from the file storage

        Args:
        cls (class): the class of objects to fetch

        Returns:
        A dictionary of objects of the provided type of class
        """

        obj_dict = {}

        if cls:
            objs = self.__objects

            for key in objs:
                split = key.replace('.', ' ')
                split = shlex.split(split)

                if split[0] == cls.__name__:
                    obj_dict[key] = self.__objects[key]
            return obj_dict
        else:
            return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete an object

        Args:
        obj (object): the object to delete
        """

        if obj:
            key = f'{type(obj).__name__}.{obj.id}'
            del self.__objects[key]

    def close(self):
        """Reload

        Description:
        This method calls the reload() method for deserializing the
        JSON file to objects
        """

        self.reload()
