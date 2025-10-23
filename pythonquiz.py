questions = (pu)

options = ((),(),(),(),())

answers = ()
guesses = []
score = 0
questions_num

for question in questions:
    print("=-=-=-=-=-=-=")
    print(question)
    for option in options[question_num]
        print(option)
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]
        score += 1
        print("correct")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer"")
    question_num += 1