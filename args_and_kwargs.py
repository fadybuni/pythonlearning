def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,2,5,3,2,1))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("spongebob","harold", "squarepants", "III")

def print_address(**kwargs):
    for key, value in kwargs.key():
        print(key)

    pass

print_address(street="123 fake st", city="detroit", state="MI", zip="54312")
