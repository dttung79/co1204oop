from w8_rect import Rectangle

class Square(Rectangle):
    def __init__(self, name, side):
        super().__init__(name, side, side) # pass same value for width and height
        self._shape_type = "Square"
    
    @property
    def side(self):
        return self.width   # or self.height, they are the same
    
    @side.setter
    def side(self, value):
        self.width = value
        self.height = value

if __name__ == "__main__":
    sq1 = Square("S1", 5)
    print(sq1)