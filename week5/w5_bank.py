from w5_account_v2 import Account

class Bank:
    def __init__(self, name):
        if name == '':
            raise ValueError('Bank name cannot be empty!')
        
        self.__name = name
        self.__accounts = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Bank name cannot be empty!')
        self.__name = value
    
    def add(self, acc):
        self.__accounts.append(acc)

    def remove(self, id):
        found = -1
        for i in range(len(self.__accounts)):
            if id == self.__accounts[i].id:
                found = i
                break
        if found == -1:
            raise ValueError(f'ID {id} not found!')
        
        self.__accounts.pop(found)
    
    def __search(self, id):
        for acc in self.__accounts:
            if acc.id == id:
                return acc
    
    def withdraw(self, id, amount):
        acc = self.__search(id)
        if not acc:
            raise ValueError(f'Account ID {id} not found to withdraw')
        acc.withdraw(amount)

    def deposit(self, id, amount):
        acc = self.__search(id)
        if not acc:
            raise ValueError(f'Account ID {id} not found to deposit')
        acc.deposit(amount)

    def show_account(self, id):
        acc = self.__search(id)
        if not acc:
            print(f'Account ID {id} not found!')
            return
        acc.show()

    def show_all(self):
        for acc in self.__accounts:
            acc.show()