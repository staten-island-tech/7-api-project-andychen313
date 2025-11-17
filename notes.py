""" class Calculator():
    def add(x,y):
        print(x + y)
        return x + y
    def add_many(list):
        print(sum(list))
        return(sum(list))
    def subtract(list):
        return list

Calculator.add(5,6) """

""" class Villain:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
Zee_yee = Villain("Zee-ye", 0, ["Basketball", "protractor"])
Zee_yee.buy("Xi-yang")
print(Zee_yee.__dict__) """

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def get_age(self):
        return 19
    