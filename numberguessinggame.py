import random

lowest_num = int(input("Please enter min: "))
highest_num = int(input("Please enter max: "))
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess: ") 
    if guess == "q":
        break
    if guess.isdigit() and int(guess) >= lowest_num and int(guess) <=highest_num:
        guess = int(guess)
        guesses += 1
        pass
    if guess == answer:
        print(f"Congrats you have guessed the correct number. The number was {answer}. It took you {guesses} tries")

    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")

