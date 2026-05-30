import random

choices = ["rock", "paper", "scissors"]

def get_user_choice():
    while True:
        user = input("Choose rock, paper, or scissors: ").lower().strip()
        if user in choices:
            return user
        print("Invalid choice. Try again.")

def get_computer_choice():
    return random.choice(choices)

def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    print("=== ROCK PAPER SCISSORS ===")

    while True:
        user = get_user_choice()
        computer = get_computer_choice()

        print(f"Computer chose: {computer}")

        result = decide_winner(user, computer)

        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        again = input("Play again? (y/n): ").lower().strip()
        if again != "y":
            break

    print("\nFINAL SCORE")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()