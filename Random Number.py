# Implement a random number guessing game.
# The computer will pick a number at random from 0-9, the user will be asked to guess the number.
# Inform the user if they get the answer correct.
# You will need to include the following in your program
# to create a variable "randomNum" and set it to a number from 0-9 at random:

from random import randint              # Create random number
randomNum = randint(0, 9)

print('Today we will play a game.')             # Start game
print('The computer is picking a random number 0-9.')

print('What do you think the number is?')               # User guessing
guess = input()
guess_num = int(guess)              # Turning the guess into an integer

if guess_num == randomNum:              # If the number is correctly guessed
    print('You guessed correctly! The number was ' + str(randomNum) + '.')

if guess_num > 9:           # If the user guessing a number out of parameters
    print('Error...')
    print('I asked for a number 0-9.')

if guess_num < 0:           # If the user guessing a number out of parameters
    print('Error...')
    print('I asked for a number 0-9. Run the program again.')

elif guess_num != randomNum:               # If the number is not right, try again
    print('Run the game again.')
