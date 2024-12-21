import random

options = ("rock","paper","scissors")
player = 0
computer = random.choice(options)

while player not in options:

    player = input("Enter a choice (rock,paper,scissors): ")

print(f"Player: {player}")
print(f"Computer: {computer}")

if player  == computer:
    print("Tie")
elif player == "rock" and computer =="scissors":
    print("You win!")
elif player == "paper" and computer == "rock":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print("oh ohu You loose 😞")
else:
    print("Ohh baby U loose again!")
