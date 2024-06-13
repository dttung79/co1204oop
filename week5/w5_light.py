class LightBulb:
    def __init__(self, room):
        self.__light = False  
        self.__room = room    

    def show(self):
        print(f'Light in {self.__room} is {self.light}')
    
    def switch(self):
        self.__light = not self.__light
    
    @property
    def light(self):
        #return self.__light
        return 'on' if self.__light else 'off'
    
    @property
    def room(self):
        return self.__room
    
    @room.setter
    def room(self, value):
        self.__room = value


# Creat an object of LightBulb class
lr_bulb = LightBulb('Living Room')
lr_bulb.show()
lr_bulb.switch()
lr_bulb.room = 'Bedroom'    # call room.setter property
lr_bulb.show()
print(lr_bulb.light)        # call light property
print(lr_bulb.room)         # call room property