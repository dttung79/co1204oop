from w5_account_v2 import Account
from w5_bank import Bank

class BankManagementProgram:
    def __init__(self, name):
        self.__bank = Bank(name)
    
    def run(self):
        running = True
        while running:
            self.__print_menu()
            choice = int(input('Your choice: '))
            if choice == 1:     self.__add_account()
            elif choice == 2:   self.__remove_account()
            elif choice == 3:   self.__withdraw()
            elif choice == 4:   self.__deposit()
            elif choice == 5:   self.__search()
            elif choice == 6:   self.__show_all()
            elif choice == 0:   running = False
            else:               print('Invalid choice!')
    
    def __print_menu(self):
        print('1. Add account')
        print('2. Remove account')
        print('3. Withdraw')
        print('4. Deposit')
        print('5. Search')
        print('6. Show all')
        print('0. Exit')

    
    def __add_account(self):
        id = int(input('Enter account ID: '))
        name = input('Enter account name: ')
        balance = float(input('Enter account balance: '))
        acc = Account(id, name, balance)
        self.__bank.add(acc)
        print('Account added!')
    
    def __remove_account(self):
        try:
            id = int(input('Enter account ID to remove: '))
            self.__bank.remove(id)
            print('Account removed!')
        except ValueError as err:
            print(err)
    
    def __withdraw(self):
        try:
            id = int(input('Enter account ID to withdraw: '))
            amount = float(input('Enter amount to withdraw: '))
            self.__bank.withdraw(id, amount)
            print('Withdraw successful!')
        except ValueError as err:
            print(err)
        
    def __deposit(self):
        try:
            id = int(input('Enter account ID to deposit: '))
            amount = float(input('Enter amount to deposit: '))
            self.__bank.deposit(id, amount)
            print('Deposit successful!')
        except ValueError as err:
            print(err)
    
    def __search(self):
        try:
            id = int(input('Enter account ID to search: '))
            self.__bank.show_account(id)
        except ValueError as err:
            print(err)
    
    def __show_all(self):
        self.__bank.show_all()
        

if __name__ == '__main__':
    program = BankManagementProgram('Vietcombank')
    program.run()