class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name, end = '.\n')

p = Person('Martin')
p.say_hi()

