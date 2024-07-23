class Item:
    def __init__(self, item_id, name, brand, price):
        self.__item_id = item_id
        self.__name = name
        self.__brand = brand
        self.__price = price
    
    @property
    def item_id(self):
        return self.__item_id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def brand(self):
        return self.__brand
    
    @property
    def price(self):
        return self.__price
    
    @name.setter
    def name(self, name):
        self.__name = name  # skip validation
    
    @brand.setter
    def brand(self, brand):
        self.__brand = brand  # skip validation

    @price.setter
    def price(self, price):
        self.__price = price  # skip validation