# Number guessing game using Python
import random

print("Hi there! This is a number guessing game.\nYou got 7 chances to guess the number.\nLet's begin!")

# Generate a random number of 100
number_to_guess = random.randrange(100)

chances = 7

guess_counter = 0

while guess_counter < chances:

    guess_counter += 1
    my_guess = int(input("Enter your guess: "))

    if my_guess == number_to_guess:
        print("Congratulations! You guessed the number in", guess_counter, "tries.")
        break

    elif my_guess > number_to_guess:
        print("Your guess is higher.")

    elif my_guess < number_to_guess:
        print("Your guess is lower.")

if guess_counter == chances:
    print("You ran out of chances. Better luck next time!")
        