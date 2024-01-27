import random
# To count the number of time user_wins and computer_wins.
user_wins = 0
computer_wins = 0
draw = 0

while True:

    user_input = input("Enter rock, paper, scissors or 'q' to quit: ").lower()
    choices = ["rock", "paper", "scissors"]
    computer_input = random.choice(choices)

    if user_input == "q":
        break

    if user_input == "rock" and computer_input == "rock":
        print(f"computer's choice : {computer_input}")
        print("Draw!")
        draw += 1
    elif user_input == "rock" and computer_input == "paper":
        print(f"computer's choice : {computer_input}")
        print("Lose!")
        computer_wins += 1
    elif user_input == "rock" and computer_input == "scissors":
        print(f"computer's choice : {computer_input}")
        print("Win!")
        user_wins += 1
    elif user_input == "paper" and computer_input == "rock":
        print(f"computer's choice : {computer_input}")
        print("Win!")
        user_wins += 1
    elif user_input == "paper" and computer_input == "paper":
        print(f"computer's choice : {computer_input}")
        print("Draw!")
        draw += 1
    elif user_input == "paper" and computer_input == "scissors":
        print(f"computer's choice : {computer_input}")
        print("Lose!")
        computer_wins += 1
    elif user_input == "scissors" and computer_input == "rock":
        print(f"computer's choice : {computer_input}")
        print("Lose!")
        computer_wins += 1
    elif user_input == "scissors" and computer_input == "paper":
        print(f"computer's choice : {computer_input}")
        print("Win!")
        user_wins += 1
    elif user_input == "scissors" and computer_input == "scissors":
        print(f"computer's choice : {computer_input}")
        print("Draw!")
        draw += 1
    else:
        print("Please make sure you choose 'rock', 'paper' or 'scissors' next time.\n")
        continue
    
print(f"User score : {user_wins}\nComputer score : {computer_wins}\nNumber of draws : {draw}")
if user_wins > computer_wins:
    print("You win the game!")
elif user_wins < computer_wins:
    print("You lose the game!")
elif user_wins == computer_wins:
    print("No one win the game!")
