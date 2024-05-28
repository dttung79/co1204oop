class LightBulb:
    # sometimes we don't need parameters but initialize the object with some default values
    def __init__(self, room):
        self.light = False  # light attribute is off by default
        self.room = room    # room attribute is initialized with the value of the parameter

    def show(self):
        light_state = 'on' if self.light else 'off'
        print(f'Light in {self.room} is {light_state}')
    
    def switch(self):
        self.light = not self.light

    def change_room(self, room):
        self.room = room


# Creat an object of LightBulb class
lr_bulb = LightBulb('Living Room')
lr_bulb.show()
lr_bulb.switch()
lr_bulb.show()
lr_bulb.change_room('Bedroom')
lr_bulb.show()