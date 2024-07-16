class Account:
    def __init__(self, id, name, balance):
        if id == '' or name == '':
            raise ValueError('ID and name cannot be empty')
        if balance < 0 or balance == '':
            raise ValueError('Balance cannot be negative')
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
        return self.__balance
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Name cannot be empty')
        self.__name = value
    
    def withdraw(self, amount):
        if self.__balance < amount or amount <= 0:
            raise ValueError('Invalid amount!')
        self.__balance -= amount
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Invalid amount')
        self.__balance += amount
