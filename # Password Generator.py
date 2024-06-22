import random

# Number Generator or wtv its called

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

# Entering player amount

while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Must be between 1 - 4 players.")
    else:
        print("Invalid, try again. ")

# Creating Score

max_score = 50
player_scores = [0 for _ in range(players)]

print(player_scores)

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score this turn is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

# Finding and announcing winner
winner = player_scores.index(max(player_scores)) + 1
print(f"Player {winner} wins with a score of {player_scores[winner-1]}!")