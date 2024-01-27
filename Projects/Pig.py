'''This is rolling a dice game. Players can be from 2 to 4. Each players have to roll a dice and add the number
to their score rather than the number 1. They can decide the number of roll they want. If a player stop to roll 
the dice, the turn of another player begin.
If they roll the number 1, their total score will be 0. To win the game, player has to get minimum score of 50
in this game.'''

import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    num_user = input("Enter the number of players (2-4): ")
    if num_user.isdigit():
        num_user = int(num_user)
        if 2 <= num_user <= 4:
            break
        else:
            print("Type a number from 2 to 4.")
    else:
        print("Invalid, type a number from 2 to 4.")

max_score = 50
players_score = [0 for _ in range(num_user)]

while max(players_score) < max_score:
    for player_idx in range(num_user):
        print("\nPlayer " + str(player_idx + 1) + "'s turn has started!")
        print(f"Your total score is {players_score[player_idx]}.\n")
        current_score = 0
        while True:
            user_roll = input("Do you want to roll? Type 'y' for yes and 'n' for no: ")
            if user_roll.lower() != 'y':
                break

            value = roll()
            print(f"You got {value}")

            if value == 1:
                current_score = 0
                players_score[player_idx] = 0
                print("You got 1. Your total score is now 0.")
                break
            else:
                current_score += value
                print("You roll a: ", value)
            print("Your score is ", current_score)

        players_score[player_idx] += current_score
        print("Your total score is ", players_score[player_idx])

maxi_score = max(players_score)
winner = players_score.index(maxi_score)
print("Player ", winner + 1, "is the winner!")
