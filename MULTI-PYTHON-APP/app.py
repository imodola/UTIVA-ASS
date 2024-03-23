import random

def guess_number():
    # Generate a random number between 1 and 10
    target_number = random.randint(1, 10)

    # Initialize variables
    attempts = 0
    guessed = False

    # Main game loop
    while not guessed:
        # Prompt the user to guess the number
        guess = int(input("Guess the number between 1 and 10: "))
        attempts += 1

        # Check if the guess is correct
        if guess == target_number:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            guessed = True
        elif guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
