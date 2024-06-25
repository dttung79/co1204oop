from w6_hw5_employee import Employee

class Company:
    def __init__(self, name):
        self.name = name
        self.__employees = []
    
    @property
    def name(self):
        return self.__name  
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Name cannot be empty')
        self.__name = value
    
    def add(self, emp):
        self.__employees.append(emp)

    def __search(self, id):
        for emp in self.__employees:
            if emp.id == id:
                return emp
    
    def remove(self, id):
        e = self.__search(id)
        if not e:
            raise ValueError('Employee not found')
        self.__employees.remove(e)
    
    def change(self, id, new_rate):
        e = self.__search(id)
        if not e:
            raise ValueError('Employee not found')
        e.rate = new_rate
    
    def show(self, id):
        e = self.__search(id)
        if not e:
            raise ValueError('Employee not found')
        e.show()
    
    def show_all(self):
        for e in self.__employees:
            e.show()