# using unlimited positional arguments / *args

def add(*args):
    result = 0
    for n in args:
        result += n
    print(result)

# add(50, 20, 30)

# Keyword arguments / **kwargs

def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

# calculate(5, add=2, multiply=5)

# using **kwargs to create class || using .get() instead of key index, so in case any arg is missing it does not give error
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')

my_car = Car(make="Nissan", model="Skyline")
# print(my_car)
