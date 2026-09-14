import random 

def determine_winner(player, computer):
    if player == computer:
        return "Draw"
    elif (player == "snake" and computer == "water") or \
         (player == "water" and computer == "gun") or \
         (player == "gun" and computer == "snake"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    choices = ["snake", "water", "gun"]
    print("Welcome to Snake-Water-Gun Game!")
    
    player_choice = input("Choose snake, water, or gun: ").strip().lower()

    if player_choice not in choices:
        print("Invalid choice! Please select snake, water, or gun.")
        return

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    while True:
        main()
