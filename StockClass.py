#!/usr/bin/env python3

"""
@note  This Class is the blueprint of how each StockItem instance should look like.
It has a constructor that holds the rules on how each values(code, description, amount) should define them-self
A built in function has been changed when doing a print or str call from __repr__ to __str__, so the outputs
can be more human readable
"""


class StockItem:
    def __init__(self, code, description, amount):  # This is the constructor
        self.code = code
        self.description = description
        self.amount = amount

    def code(self):
        return self.code

    def description(self):
        return self.description

    def amount(self):
        return self.amount

    def __str__(self): # the object translator, making the values readable when using print and str
        return "{self.code}, {self.description}, {self.amount}".format(self=self)


"""
@note #This class will use the StockItem blueprint to create new instances(copies) of it, editing them and searching
for either entire list or specific value part within an object.
Also the usage of csv model is in place to be able to store the list created once the program is closed.
Each of these functions are being pointed from the main.py
"""


class StockTracker:

    def __init__(self):  # This list is where all the instances of StockItem will be stored(in memory)
        self.StockList = list()

    def add_stock(self, code, description, amount):
        self.StockList.append(StockItem(code, description, amount))
        self.show_list()

    def define_index(self, code):
        for i, Stock in enumerate(self.StockList):  # Making a new index within the list by using enumerate
            if Stock.code == code:
                return i

    def show_list(self):
        for i in self.StockList:
            print(i)

    def search_index(self):
        code = input("enter search: ")
        index = StockTracker.define_index(self, code)  # This line calls the function define_index
        print(self.StockList[index].description)

    def update_stock(self):
        code = input("enter search: ")
        index = StockTracker.define_index(self, code)  # This line calls the function define_index
        new_amount = input("New amount: ")
        self.StockList[index].amount = new_amount

    def delete_stock(self):  # Currently not completed 100%, but will work for the first instance in the list
        code = input("enter search: ")
        index = StockTracker.define_index(self, code)  # This line calls the function define_index
        print(code + "is removed")
        self.StockList.remove(code)
        print(code + "" + " is removed")

    def save_list(self):  # Once this function is called, it will take the list in memory and store it to a csv file
        for i in self.StockList:
            with open("Stocklist.csv", "a", newline="") as writing:
                writing.write(str(i))

