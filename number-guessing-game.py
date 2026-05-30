import random

number = random.randint(1, 100)
guess = None
tries = 0

print("I picked a number between 1 and 100.")

while guess != number:
    guess = int(input("Your guess: "))
    tries += 1

    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print(f"Correct! You got it in {tries} tries.")