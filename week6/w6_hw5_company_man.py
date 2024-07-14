from w6_hw5_employee import Employee, PartTimeEmployee
from w6_hw5_company import Company

class CompanyManagement:
    def __init__(self, name):
        self.__company = Company(name)
    
    def run(self):
        running = True
        while running:
            print('1. Add employee')
            print('2. Remove employee')
            print('3. Change rate')
            print('4. Show employee')
            print('5. Show all employees')
            print('0. Exit')
            choice = input('Enter your choice: ')
            if choice == '1':   self.add_employee()
            elif choice == '2': self.remove_employee()
            elif choice == '3': self.change_rate()
            elif choice == '4': self.show_employee()
            elif choice == '5': self.show_all_employees()
            elif choice == '0': running = False
            else: print('Invalid choice')
    
    def add_employee(self):
        try:
            emp_type = input('Enter employee type (1. Full-time/ 2. Part-time): ')
            name = input('Enter employee name: ')
            rate = float(input('Enter employee rate: '))
            
            if emp_type == '1': 
                emp = Employee(name, rate)
            elif emp_type == '2':
                dow = int(input('Enter working days of week: '))
                emp = PartTimeEmployee(name, rate, dow)
            else:
                raise ValueError('Invalid employee type')
            
            self.__company.add(emp)    
        except ValueError as e:
            print(e)
    
    def remove_employee(self):
        try:
            id = int(input('Enter employee ID: '))
            self.__company.remove(id)
            print('Employee removed')
        except ValueError as e:
            print(e)
    
    def change_rate(self):
        try:
            id = int(input('Enter employee ID: '))
            rate = float(input('Enter new rate: '))
            self.__company.change(id, rate)
            print('Rate changed')
        except ValueError as e:
            print(e)

    def show_employee(self):
        try:
            id = int(input('Enter employee ID: '))
            self.__company.show(id)
        except ValueError as e:
            print(e)
    
    def show_all_employees(self):
        self.__company.show_all()

if __name__ == '__main__':
    program = CompanyManagement('ABC Company')
    program.run()