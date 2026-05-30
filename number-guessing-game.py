import random


def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy (1–50, 10 tries)")
    print("2. Medium (1–100, 7 tries)")
    print("3. Hard (1–200, 5 tries)")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            return 50, 10
        elif choice == "2":
            return 100, 7
        elif choice == "3":
            return 200, 5
        else:
            print("Invalid choice.")

def get_guess(max_num):
    while True:
        try:
            guess = int(input(f"Enter your guess (1–{max_num}): "))
            if 1 <= guess <= max_num:
                return guess
            print("Out of range.")
        except ValueError:
            print("Enter a valid number.")

def play_game():
    print("=== NUMBER GUESSING GAME ===")

    max_num, tries = choose_difficulty()
    secret = random.randint(1, max_num)

    score = 100
    attempts_used = 0

    print(f"\nI picked a number between 1 and {max_num}.")
    print(f"You have {tries} tries.\n")

    while attempts_used < tries:
        guess = get_guess(max_num)
        attempts_used += 1

        if guess == secret:
            print("\nYou got it!")
            print(f"Attempts: {attempts_used}")
            print(f"Score: {score}")
            break

        diff = abs(secret - guess)

        if guess < secret:
            print("Too low.")
        else:
            print("Too high.")

        if diff <= 3:
            print("🔥 VERY HOT")
        elif diff <= 10:
            print("🔥 Hot")
        elif diff <= 20:
            print("😐 Warm")
        else:
            print("🥶 Cold")

        score -= 10

        print(f"Tries left: {tries - attempts_used}\n")

    else:
        print("\nYou lost.")
        print(f"The number was: {secret}")

    print("Game over.\n")

def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing.")
            break

if __name__ == "__main__":
    main()