import random

# Computer picks a random number between 1 and 100
number = random.randint(1, 100)
guesses = 0
max_guesses = 5

# Keep asking the player for a guess
while guesses < max_guesses:
    guess = int(input(f"Guess a number between 1 and 100 ({max_guesses - guesses} guesses left): "))
    guesses += 1
    
    # Check if the guess is correct
    if guess == number:
        print(f"Congrats! You got it in {guesses} guesses!")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# If out of guesses
if guesses >= max_guesses and guess != number:
    print(f"Game over! The number was {number}.")