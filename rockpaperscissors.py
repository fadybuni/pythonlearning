import random
import time
options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

while player not in options:

    player = input(print("Please choose an option: Rock, Paper, or Scissors: "))
    

for i in range(3, 0, -1):
    print(i)
    time.sleep(1)
print(f"Computer picked {computer}")
 