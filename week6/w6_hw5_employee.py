class Employee:
    # static id for all employees
    __id = 0
    __BASIC_SALARY = 1000
    def __init__(self, name, rate):
        self.name = name            # call the setter to set the attribute
        self.rate = rate
        self.__id = Employee.__id
        Employee.__id += 1
    
    @property
    def BASIC_SALARY(self):
        return Employee.__BASIC_SALARY
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def rate(self):
        return self.__rate
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Name cannot be empty')
        self.__name = value
    
    @rate.setter
    def rate(self, value):
        if value < 0:
            raise ValueError('Rate cannot be negative')
        self.__rate = value

    def show(self):
        print(f'Employee ID: {self.id}')
        print(f'Employee Name: {self.name}')
        print(f'Employee Rate: {self.rate}')
        print(f'Employee Salary: {self.salary()}')

    def salary(self):
        return self.BASIC_SALARY * self.rate

class PartTimeEmployee(Employee):
    def __init__(self, name, rate, dow):
        super().__init__(name, rate)    # call parent's constructor to set name and rate
        self.dow = dow
    
    @property
    def dow(self):
        return self.__dow
    
    @dow.setter
    def dow(self, value):
        if value < 0 or value > 6:
            raise ValueError('Invalid working days of week')
        self.__dow = value

    # override the salary method
    def salary(self):
        return super().salary() * self.dow / 5
    
    # override the show method
    def show(self):
        super().show()  # call parent's show method to print id, name, rate, and salary
        print(f'Employee Working Days: {self.dow}')