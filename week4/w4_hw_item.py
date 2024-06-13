class Item:
    def __init__(self, id, name, price, quantity):
        self.__set_id(id)
        self.set_name(name)
        self.set_price(price)
        self.__quantity = 0
        self.increase(quantity)

    def __set_id(self, id):
        if id < 0:
            print('ID cannot be negative. Set to 0')
            self.__id = 0
            return
        self.__id = id

    def set_name(self, name):
        if name == '':
            print('Name cannot be empty. Set to default')
            self.__name = 'No name'
            return
        
        self.__name = name
    
    def set_price(self, price):
        if price < 0:
            print('Price cannot be negative. Set to default')
            self.__price = 0
            return

        self.__price = price
    
    def increase(self, quantity):
        if not isinstance(quantity, int) or quantity < 0:
            print('Quantity must be number and cannot be negative. Set to default.')
            self.__quantity = 0q [[ [q œœœœœ]]]
            return
        self.__quantity += quantity

    def show(self):
        print(f'Item id {self.__id}, name: {self.__name}, price: {self.__price}, quantity: {self.__quantity}')
        
car = Item(-99, '', -100, '100')
car.show()