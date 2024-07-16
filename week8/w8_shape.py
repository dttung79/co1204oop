from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        super().__init__()
        self.name = name                # this is setter method
        self._shape_type = "General"    # this is protected attribute
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be empty")
        self.__name = value
    
    @property
    def shape_type(self):
        return self._shape_type
    
    # area is abstract method because we don't know how to calculate area of a general shape
    # but we still declare it here to make sure all subclasses have this method
    @abstractmethod
    def area(self): 
        pass

    def __str__(self):
        return f"{self._shape_type} {self.name}: area {self.area()}"
