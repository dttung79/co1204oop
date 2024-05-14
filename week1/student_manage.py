ids = [1, 2, 3]
names = ['John', 'Anna', 'Mike']
gpas = [8.0, 7.5, 9.5]

def run():
    running = True
    while running:
        show_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            add_student()
        elif choice == 2:
            edit_student()
        elif choice == 3:
            delete_student()
        elif choice == 4:
            show_all()
        elif choice == 5:
            search_student()
        elif choice == 0:
            print('Goodbye! See you next time')
            running = False
        else:
            print('Invalid choice!')

def show_menu():
    print('~~~~~~~~ STUDENT MANAGEMENT ~~~~~~~~')
    print('1. Add student')
    print('2. Edit student')
    print('3. Delete student')
    print('4. Show all students')
    print('5. Search student')

def add_student():
    print('Enter new student information')
    id = int(input('Enter student id: '))
    name = input('Enter student name: ')
    gpa = float(input('Enter student GPA: '))

    pos = check_id(id)
    if pos != -1:
        print(f'Student id {id} exist! Duplicate id is not allowed')
        return
    
    ids.append(id)
    names.append(name)
    gpas.append(gpa)

    print(f'Student {name} added succesfully!')

def check_id(id):
    for i in range(len(ids)):
        if ids[i] == id:
            return i
    
    return -1

def edit_student():
    id = int(input('Enter student id to edit: '))
    pos = check_id(id)

    if pos == -1:
        print(f'Student id {id} does not exist!')
        return
    
    name = input('Enter new name: ')
    gpa = float(input('Enter new gpa: '))

    names[pos] = name
    gpas[pos] = gpa
    print(f'Student {name} edited succesfully!')

def delete_student():
    id = int(input('Enter student id to delete: '))
    pos = check_id(id)

    if pos == -1:
        print(f'Student id {id} does not exist!')
        return
    
    ids.pop(pos)    # remove id at position pos
    names.pop(pos)
    gpas.pop(pos)
    print(f'Student id {id} deleted succesfully!')

def show_all():
    print('All students:')
    for i in range(len(ids)):
        print(f'ID: {ids[i]}, name: {names[i]}, GPA: {gpas[i]}')
    
def search_student():
    name = input('Enter a name to search: ')
    count = 0
    for i in range(len(names)):
        if name in names[i]:
            print(f'ID: {ids[i]}, name: {names[i]}, GPA: {gpas[i]}')
            count += 1
    
    if count == 0:
        print(f'No student found for name {name}')


#####
run()