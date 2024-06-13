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
        return self.__balance
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Name cannot be empty!')
        self.__name = value
    
    def withdraw(self, amount):
        if self.__balance < amount:
            raise ValueError('Balance is not enough to withdraw')
        if amount <= 0:
            raise ValueError('Amount must be positive!')
        self.__balance -= amount
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Amount must be positive!')
        self.__balance += amount

    def show(self):
        print(f'Account ID {self.id}, name: {self.name}, balance: ${self.balance}')