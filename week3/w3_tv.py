class Television:
    def __init__(self, name):
        self.name = name
        self.channel = 1
        self.state = False
    
    def show(self):
        state = 'on' if self.state else 'off'
        print(f'TV {self.name} is {state} on channel {self.channel}')
    
    def turn_on(self):
        self.state = True
        print(f'TV {self.name} is on, playing channel {self.channel}')

    def turn_off(self):
        self.state = False
        print(f'TV {self.name} is off')
    
    def switch(self, channel):
        if self.state == True:
            self.channel = channel
            print(f'TV {self.name} is playing channel {self.channel}')
        else:
            print('TV is off, please turn on the TV first')
######
tv_samsung = Television('Samsung')
tv_samsung.show()
tv_samsung.turn_on()
tv_samsung.switch(5)
tv_samsung.turn_off()
tv_samsung.switch(7)
tv_samsung.show()
tv_samsung.turn_on()