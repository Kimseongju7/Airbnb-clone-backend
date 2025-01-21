class Person:
    def __init__(self, name):
        self.name = name;
    def say_hello(self):
        print('Hello, my name is ' + self.name)
class Player(Person):
    def __init(self, name, age):
        super().__init__(name)
        self.age = age
class fan(Person):
    def __init__(self, name, team):
        super().__init__(name)
        self.fav_team = team
min = fan('mini', "wolfs")
min.say_hello()