# import file syntax: from file import class
from w3_student import Student

class ClassRoom:
    # init a class room with a name and an empty list of students
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self):
        id = int(input('Enter student id: '))
        name = input('Enter student name: ')
        gpa = float(input('Enter student GPA: '))
        # create student object
        s = Student(id, name, gpa)
        # add student object to the list
        self.students.append(s)

    def check_id(self, id):
        for i in range(len(self.students)):
            # if student at i position has the same id as the parameter id then return i
            if self.students[i].id == id:
                return i
        # if no student has the same id as the parameter id then return -1
        return -1
    
    def edit_student(self):
        id = int(input('Enter student id to edit: '))
        pos = self.check_id(id)

        if pos == -1:
            print(f'Student id {id} does not exist!')
            return

        name = input('Enter new name: ')
        gpa = float(input('Enter new gpa: '))
        # edit student at position pos, self.students[pos] is a student object
        self.students[pos].name = name
        self.students[pos].gpa = gpa

    def show_all(self):
        # loop through all students in the list
        # and call method show() of each student object
        for s in self.students:
            s.show()

    def edit_student(self):
        id = int(input('Enter student id to edit: '))
        pos = self.check_id(id)

        if pos == -1:
            print(f'Student id {id} does not exist!')
            return

        name = input('Enter new name: ')
        gpa = float(input('Enter new gpa: '))
        # edit student at position pos, self.students[pos] is a student object
        self.students[pos].name = name
        self.students[pos].gpa = gpa
    
    def delete_student(self):
        id = int(input('Enter student id to delete: '))
        pos = self.check_id(id)

        if pos == -1:
            print(f'Student id {id} does not exist!')
            return

        # remove student at position pos
        self.students.pop(pos)
    
    def search_student(self):
        name = input('Enter student name to search: ')
        count = 0
        for s in self.students:
            if name in s.name:
                s.show()
                count += 1
        if count == 0:
            print(f'Student name {name} does not exist!')
    
    def print_menu(self):
        print('1. Add student')
        print('2. Edit student')
        print('3. Delete student')
        print('4. Show all students')
        print('5. Search student')
        print('0. Exit')

    def run(self):
        running = True
        while running:
            self.print_menu()
            choice = int(input('Enter your choice: '))
            if choice == 1:     self.add_student()
            elif choice == 2:   self.edit_student()
            elif choice == 3:   self.delete_student()
            elif choice == 4:   self.show_all()
            elif choice == 5:   self.search_student()
            elif choice == 0:   running = False
            else:               print('Invalid choice!')

### main ###
gch1204 = ClassRoom('GCH1204')
gch1204.run()
