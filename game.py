import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    
    # Set the maximum number of attempts
    max_attempts = 10
    attempts = 0
    
    while attempts < max_attempts:
        try:
            # Get the player's guess
            guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
            
            # Increment the attempts
            attempts += 1
            
            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Try again. The number is higher.")
            else:
                print("Try again. The number is lower.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if attempts == max_attempts:
        print(f"Sorry, you've reached the maximum number of attempts. The correct number was {secret_number}.")

# Run the game
guess_the_number()
