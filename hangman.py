import random

words = ("apple", "orange", "banana", "coconut", "pineapple")

#dictionary of key:()
hangman_art = {0:("   ",
"   ",
"   "),
1:(" o ",
"   ",
"   "),
2:(" o ",
"  | ",
"   "),
3:(" o ",
"/|   ",
"   "),
4:(" o ",
"/|\\",
"   "),
5:(" o ",
"/|\\",
"/  "),
6:(" o ",
"/|\\",
"/ \\")}

def display_man(wrong_guesses):
    print("***************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***************")


def display_hint(hint):
    print("")
    print(" ".join(hint))

def display_answer(answer):
        print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    print(hint)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("That letter has already been guessed")
            continue
    
        guessed_letters.add(guess)

        if guess in answer: 
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print("That is not a correct guess")

        if "_" not in hint:
            print(f"You win! The word was: {answer}")
            is_running = False
        elif wrong_guesses >= 6:
            print("Game Over! You have no more guesses!")
            break
        
        



if __name__ == "__main__":
    main()

for line in hangman_art[3]:
    print(line)