#!/usr/bin/python3
"""
Contains class BaseModel
"""

from datetime import datetime
import models
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The BaseModel class from which future classes will be derived"""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
<<<<<<< HEAD
        " Returns the string representation of
        an instance of the Base Model class "
        d = self.id
        f = self.__dict__
        return("[{}] ({}) {}".format(self.__class__.__name__, d, f))
=======
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)
>>>>>>> 08760a8a68db4a085bea3a6258455d2227701a48

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
<<<<<<< HEAD
        " returns a dictionary containing all keys/
        values of __dict__ of the instance "
        dict_copy = {**self.__dict__}
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = datetime.isoformat(self.created_at)
        dict_copy["updated_at"] = datetime.isoformat(self.updated_at)
        return dict_copy

    @classmethod
    def all(cls):
        " Returns a list of all instances of selected class model "
        all = m.storage.all()
        data_list = []
        cls_name = cls.__name__

        for cls_name_id_key in all:

            if cls_name_id_key.startswith(cls_name):
                data_list.append(all[cls_name_id_key].__str__())

        return data_list

    @classmethod
    def count(cls):
        " Returns number of instances of selected class model "
        return len(cls.all())

    @classmethod
    def show(cls, id):
        '''
        Returns a single instance retrived by id of selected class model
        Returns
        -------
            int(1) : Error(** instance id missing **)
            int(2) : Error(** no instance found **)
            object : Success (selected instance)
        '''

        if not id:
            return (1)

        cls_name_id_key = cls.__name__+"."+id
        all = m.storage.all()

        if cls_name_id_key in all:
            return all[cls_name_id_key]
        else:
            return(2)

    @classmethod
    def destroy(cls, id):
        '''
        Destroys a single instance retrived from the selected class model by id
        Returns
        -------
            int(1) : Error(** instance id missing **)
            int(2) : Error(** no instance found **)
            None : Success
        '''

        if not id:
            return (1)

        key_to_del = cls.__name__+"."+id
        all = m.storage.all()

        if key_to_del in all:
            all.pop(key_to_del)
            m.storage.save()
        else:
            return(2)

    @classmethod
    def update(cls, id, attr_name, attr_value):
        cls_name_id_key = cls.__name__+"."+id
        all = m.storage.all()
        selected_record = all[cls_name_id_key]
        setattr(selected_record, attr_name, eval(attr_value))
        m.storage.save()
=======
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
>>>>>>> 08760a8a68db4a085bea3a6258455d2227701a48
