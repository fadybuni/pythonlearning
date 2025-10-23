def happy_birthday(name, age):

    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy birthday to {name}!")
    print()

happy_birthday("James",20)
happy_birthday("Alex",40)
happy_birthday("fady",60)

def add(x, y):
    z = x +y
    return z
def subtract(x, y):
    z = x - y
    return z
def multiply(x, y):
    z = x*y
    return z
def devide(x, y):
    z = x/y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(devide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)