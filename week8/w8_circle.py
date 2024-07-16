from w8_shape import Shape

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)      # call the constructor of the parent class to set the name
        self.radius = radius        # call the setter method to set the radius
        self._shape_type = "Circle" # set the shape type
    
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self.__radius = value
    
    # override the area method
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def __str__(self):
        shape_info = super().__str__()
        return shape_info + f", radius {self.radius}"
    
if __name__ == "__main__":
    c = Circle("C1", 5)
    print(c)
    