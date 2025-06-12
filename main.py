# Snake Water Gun Game.

import random  # Import the random module to let the computer choose randomly

# Function to determine the winner based on player and computer choices
def determine_winner(player, computer):
    if player == computer:
        return "Draw"  # Same choice leads to a draw
    elif (player == "snake" and computer == "water") or \
         (player == "water" and computer == "gun") or \
         (player == "gun" and computer == "snake"):
        return "You win!"  # These are the winning conditions for the player
    else:
        return "Computer wins!"  # All other valid cases mean the computer wins

# Main function to run the game
def main():
    choices = ["snake", "water", "gun"]  # Valid choices
    print("Welcome to Snake-Water-Gun Game!")  # Game intro
    
    # Ask for the player's choice
    player_choice = input("Choose snake, water, or gun: ").strip().lower()

    # Validate the player's input
    if player_choice not in choices:
        print("Invalid choice! Please select snake, water, or gun.")
        return  # Exit the game if input is invalid

    # Randomly choose for the computer
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine and print the result
    result = determine_winner(player_choice, computer_choice)
    print(result)

# Call the main function if this script is run directly
if __name__ == "__main__":
    while True:
        main()