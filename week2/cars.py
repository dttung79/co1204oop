# car information: id, brand, model, price and mileage
cars = {1: ['Toyota', 'Prius', 10000, 0],
        2: ['Toyota', 'Corolla', 12000, 2000],
        3: ['Honda', 'Civic', 15000, 0],
        4: ['Honda', 'Accord', 8000, 1000]}

def print_menu():
    print('1. Show all cars')
    print('2. Search by brand')
    print('3. Search by price')
    print('4. Search by mileage')
    print('5. Add car')
    print('6. Delete car')
    print('7. Edit car')
    print('0. Exit')

def show_cars():
    print('All cars in the showroom:')
    for id, car in cars.items():
        print(f'{id}: {car[0]} {car[1]} - ${car[2]} - {car[3]} miles')

def search_brand():
    brand = input('Enter a brand to search: ')
    count = 0
    print(f'All cars of brand {brand}: ')
    
    for id, car in cars.items():
        if brand.lower() == car[0].lower():
            print(f'{id}: {car[1]} - ${car[2]} - {car[3]} miles')
            count += 1
    
    if count == 0:
        print(f'No car of brand {brand}')

def search_price():
    price = int(input('Enter a price to search: '))
    count = 0
    print(f'All cars which has price >= {price}: ')
    
    for id, car in cars.items():
        if car[2] >= price:
            print(f'{id}: {car[0]} {car[1]} - ${car[2]} - {car[3]} miles')
            count += 1
    
    if count == 0:
        print(f'No car which has price >= {price}')

def search_mileage():
    miles = int(input('Enter minimum miles to search: '))
    count = 0
    print(f'All cars which has mileage <= {miles}: ')
    
    for id, car in cars.items():
        if car[3] <= miles:
            print(f'{id}: {car[0]} {car[1]} - ${car[2]} - {car[3]} miles')
            count += 1
    
    if count == 0:
        print(f'No car which has mileage <= {miles}')

def add_car():
    id = int(input('Enter new car id: '))
    # check if id is already in the dictionary
    if id in cars:
        print(f'Car id {id} existed! Please enter new id')
        return
    # enter other information
    brand = input('Enter new car brand: ')
    model = input('Enter new car model: ')
    price = get_int('Enter new car price: ', 3, lambda a: a > 0)
    miles = get_int('Enter new car mileage: ', 3, lambda a: a >= 0)
    # add new car
    cars[id] = [brand, model, price, miles]
    print(f'New car added.')

def delete_car():
    id = int(input('Enter car id to delete: '))
    if id not in cars:
        print(f'Car id {id} not existed! Please enter existed id!')
        return
    
    cars.pop(id)
    print(f'Car id {id} deleted successfully')

def edit_car():
    id = int(input('Enter car id to edit: '))
    # check if id is not in the dictionary
    if id not in cars:
        print(f'Car id {id} not existed! Please enter existed id')
        return
    # enter other information
    brand = get_string('Enter car new brand: ', 3, lambda a: len(a) > 0)
    model = input('Enter car new model: ')
    price = int(input('Enter car new price: '))
    miles = int(input('Enter car new mileage: '))
    # edit car
    cars[id] = [brand, model, price, miles]
    print(f'Car edited.')

def run():
    running = True
    while running:
        print_menu()
        option = get_int('Enter an option: ', 3)
        if option == 1:   show_cars()
        elif option == 2: search_brand()
        elif option == 3: search_price()
        elif option == 4: search_mileage()
        elif option == 5: add_car()
        elif option == 6: delete_car()
        elif option == 7: edit_car()
        elif option == 0: running = False
        else: print('Invalid option!')


def get_int(prompt, n_try, validate=lambda a: True):
    for i in range(n_try):
        try:
            value = int(input(prompt))
            if validate(value):
                return value
            print('Invalid input! Please enter again!')
        except ValueError:
            print('Invalid input! Please enter a number')
    
    print(f'Max number of try exceed! Stops program.')
    exit(0)

def get_string(prompt, n_try, validate=lambda a: True):
    for i in range(n_try):
        value = input(prompt)
        if validate(value):
            return value
        print('Invalid input! Please enter again!')
        
    print(f'Max number of try exceed! Stops program.')
    exit(0)

run()