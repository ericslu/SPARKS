import random

# Variables
wins = 0
losses = 0
ties = 0

yourMove = ""
theirMove = ""

moves = ["rock", "paper", "scissors"]

# Get moves
while (yourMove not in moves):
    yourMove = input("Rock, Paper or Scissors? >")

theirMove = moves[random.randint(0, 2)]

# Print out the moves
print()
print(yourMove, "vs.", theirMove)
print()

# Logic
if (yourMove == theirMove):
    print("It is a tie")
    ties += 1
elif ((yourMove == "rock" and theirMove == "scissors") or
      (yourMove == "paper" and theirMove == "rock") or
      (yourMove == "rock" and theirMove == "scissors")):
    print("You win!")
    wins += 1
else:
    print("You lose!")
    losses += 1
