class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
    
    def show(self):
        print(f'Student ID: {self.id}, name: {self.name}, GPA: {self.gpa}')