import random
min = int(input("please input your minimum: "))
max = int(input("please enter your maximum: "))
number = random.randint(min, max)

print(f"A number in between your range of {min} and {max} is {number}")