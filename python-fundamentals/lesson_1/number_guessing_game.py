"""Number Guessing Game"""

"""A user inputs a number guess between 1 and 100, and the
program tells them if they have guessed the number correctly.
It tells them if the guess is too high or too low, and keeps
track of how many attempts the user has made."""

secret = 7
attempts = 0
while True:
    guess = int(input("Enter your guess (1-100):"))
    attempts += 1

    if guess < secret:
        print("Too low! Try again")
    elif guess > secret:
        print("Too high! Try again")
    else:
        print("Congratulations! You've guessed the number.")
        attempts = 0

    break