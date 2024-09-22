import random

choices = ["rock", "paper", "scissor"]
computer = random.choice(choices)

user_score = 0
computer_score = 0

while True:

    user = input("\n[ rock, paper, scissor ]\nEnter your choice: ").lower()
    if user not in choices:
        print("Invalid choice! Please choose rock or paper or scissor.")
        continue
    if user == computer:
        result = "It's a tie"

    elif (user == "rock" and computer == "paper") or (user == "paper" and computer == "scissor") or (user == "scissor" and computer == "rock"):
        result = "You Win"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1

    print("\nYour choice: ",user)
    print("Computer's choice",computer)
    print(result)
    print("\nScore: your's score: ",user_score, "Computer's score",computer_score)

    replay = input("\nDo you want to replay! ( yes / no ): ").lower()
    if replay != "yes":
        break
print("\nThank you for playing!\n")