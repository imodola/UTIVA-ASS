# MULTI PYTHON CONFIG
### # Stage 1: Build the application
FROM python:3.9 AS builder

### Set working directory in the container
WORKDIR /app

#### Copy the requirements file
COPY requirements.txt .

### Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

### Copy the application code
COPY . .

### Stage 2: Create the final lightweight image
FROM python:3.9-slim AS runtime

### Set working directory in the container
WORKDIR /app

### Copy the installed dependencies and application code from the builder stage
COPY --from=builder /app /app

### Command to run the application
CMD ["python", "guessing_game.py"]


# MULTI DOCKER CODE

### import random

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
