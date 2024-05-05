import random
computer = random.randint(1, 3)
player = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
if computer == 1:
    if player == 1:
        print("Computer chose Rock, you chose Rock, it's a tie!")
    elif player == 2:
        print("Computer chose Rock, you chose Paper, you win!")
    elif player == 3:
        print("Computer chose Rock, you chose Scissors, you lose!")
elif computer == 2:
    if player == 1:
        print("Computer chose Paper, you chose Rock, you lose!")
    elif player == 2:
        print("Computer chose Paper, you chose Paper, it's a tie!")
    elif player == 3:
        print("Computer chose Paper, you chose Scissors, you win!")
else:
    if player == 1:
        print("Computer chose Scissors, you chose Rock, you win!")
    elif player == 2:
        print("Computer chose Scissors, you chose Paper, you lose!")
    elif player == 3:
        print("Computer chose Scissors, you chose Scissors, it's a tie!")

# Path: main.py