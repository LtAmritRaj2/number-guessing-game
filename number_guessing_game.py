import random

# Computer picks the random number btw 1 - 100
number = random.randint(1, 100)
guesses = 0

# Keep asking the player for a guess
while True:
    guess = int(input("Guess a number btw 1 and 100"))
    guesses += 1
    
    # Check if the guss is correct
    if guess = number:
        print(f"Congrats! You got it in {guess} guesses!")
        break
    elif guess < number:
        print(f"Your number {guess} is Too low! Try again.")
    else:
        print(f"Your number {guess} is Too high! Try again")
