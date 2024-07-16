from w8_shape import Shape

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
        self._shape_type = "Rectangle"
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self.__width = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self.__height = value
    
    def area(self):
        return self.width * self.height
    
    def __str__(self):
        shape_info = super().__str__()
        return shape_info + f", dimension: {self.width} x {self.height}"

if __name__ == "__main__":
    r = Rectangle("R1", 3, 4)
    print(r)