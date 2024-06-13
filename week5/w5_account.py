class Account:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name
        self.__balance = balance

    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name

    @property
    def balance(self):
        return self.balance
    
    @name.setter
    def name(self, value):
        if value == '':
            self.__name = 'No name'
            return
        self.__name = value
    
    def withdraw(self, amount):
        if self.__balance < amount or amount <= 0:
            print('Invalid amount!')
            return
        self.__balance -= amount
    
    def deposit(self, amount):
        if amount <= 0:
            print('Invalid amount')
            return
        self.__balance += amount

    def show(self):
        print(f'Account ID {self.id}, name: {self.name}, balance: ${self.balance}')