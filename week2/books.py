ids = [1, 2, 3, 4]
titles = ["I hate Fe", "I love Cu", "I'm Hg", "Digger"]
authors = ["Cu", "Fe", "Hg", "H"]
statuses = [True for i in ids]

def run():
    running = True
    while running:
        show_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:     add_book()
        elif choice == 2:   search_books()
        elif choice == 3:   edit_book()
        elif choice == 4:   delete_book()
        elif choice == 5:   display_all_books()
        elif choice == 6:   borrow_book()
        elif choice == 7:   running = False
        else:               print('Invalid choice')

def show_menu():
    print('1. Add book')
    print('2. Search book')
    print('3. Edit book')
    print('4. Delete book')
    print('5. Display all books')
    print('6. Borrow book')
    print('7. Exit')

def check_id(id):
    for i in range(len(ids)):
        if ids[i] == id:
            return i
    return -1

def add_book():
    id = int(input('Book ID: '))
    pos = check_id(id)
    if pos != -1:
        print(f'Book id{id} exist! Duplicate id is not allowed')
        return
    
    title = input('Enter title: ')
    author = input('Enter author: ')
    status = True
    
    ids.append(id)
    titles.append(title)
    authors.append(author)
    statuses.append(status)

    print('Book added successfully')

def search_books():
    id = int(input('Enter id: '))
    pos = check_id(id)
    if pos == -1:
        print(f"Book id{id} didn't exist!")
        return
    
    print(f'Book name: {titles[pos]}')
    print(f'Book id: {ids[pos]}')
    print(f'Book author: {authors[pos]}')
    print(f'Book status: {"available" if statuses[pos] else "unavailable"}')

def edit_book():
    id = int(input('Enter id: '))
    pos = check_id(id)
    if pos == -1:
        print(f"Book id{id} didn't exist!")
        return
    
    title = input('Enter title: ')
    author = input('Enter author: ')
    
    titles[pos] = title
    authors[pos] = author
    
    print('Book edited successfully')

def delete_book():
    id = int(input('Enter id: '))
    pos = check_id(id)
    if pos == -1:
        print(f"Book id{id} didn't exist!")
        return
    
    ids.pop(pos)
    titles.pop(pos)
    authors.pop(pos)
    statuses.pop(pos)
    
    print('Book deleted successfully')

def display_all_books():
    for i in range(len(ids)):
        print(f'Book name: {titles[i]}')
        print(f'Book id: {ids[i]}')
        print(f'Book author: {authors[i]}')
        print(f'Book status: {"available" if statuses[i] else "unavailable"}')
        print(f'----------------------------------------------------------------')

def borrow_book():
    id = int(input('Enter id: '))
    pos = check_id(id)
    
    if pos == -1:
        print(f"Book id{id} didn't exist!")
        return
    
    if statuses[pos] == False:
        print('Book is not available')
        return
    
    statuses[pos] = False
    print('Book borrowed successfully')
    
def return_book():
    id = int(input('Enter id: '))
    pos = check_id(id)
    
    if pos == -1:
        print(f"Book id{id} didn't exist!")
        return
    
    if statuses[pos] == True:
        print('Book is not borrowed')
        return
    
    statuses[pos] = True
    print('Book returned successfully')

############ MAIN ############
run()