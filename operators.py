word = "APPLE"
letter = ""
while letter != "!":
    letter = input("Guess a letter in the secret word: ").upper()

    if letter == "!":
        break

    if letter in word:
        print(f"There is a {letter}")
    else: print(f"{letter} was not found")


grades = {"Sandy": "A",
"Squidward": "B",
"Spongebob": "C",
"Patrick": "D"}
while letter != "@":

    student = input("Enter the name of a student: ")
    if student == "!":
        break
    if student in grades:
        print(f"{student}'s grade is {grades[student]}.")
    else:
        print(f"{student} was not found.")

email = "fadybuni2004@gmail.com"

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")
