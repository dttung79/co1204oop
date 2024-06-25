class Employee:
    # static id for all employees
    __id = 0
    def __init__(self, name, rate):
        self.name = name            # call the setter to set the attribute
        self.rate = rate
        self.__id = Employee.__id
        Employee.__id += 1
    
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

## Test
# john = Employee('John', 10)
# john.show()

# paul = Employee('Paul', 20)
# paul.show()

# vincent = Employee('', 30)