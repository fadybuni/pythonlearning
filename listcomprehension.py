doubles = []
for x in range(1,11):
    doubles.append(x*2)

print(doubles)

doubles = [x * 2 for x in range(1,11)]
triples = [y * 3 for y in range(1,11)]
square = [z * z for z in range(1,11)]
print (doubles)
print (triples)
print (square)


fruits = ["apple", "orange", "banana", "coconut"]
fruits_chars = [fruit[0] for fruit in fruits]
print(fruits)

numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0]
negative_nums =  [num for num in numbers if num < 0]

print(f"These are all the positive numbers: {positive_nums} !")
print(f"These are all the negative numbers: {negative_nums} !")


grades = [85,42,79,90,56,61,30]
passing_grades = [grade for grade in grades if grade >= 60]
failing_grades = [grade for grade in grades if grade < 60]
print(passing_grades)
print(failing_grades)