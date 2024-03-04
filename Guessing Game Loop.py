# Write a program that picks a random number from 1-100.  Then ask the user to guess a number.
# Tell the user if the answer is higher or lower than the number they guessed, or if they got the correct answer.
# Allow them to guess again if they got the guess incorrect.
# They should be able to guess numbers an infinite number of times until they get the correct answer, at which point your loop will end.

from random import randint              # To use the random module, I have to import it
randomNum = randint(1, 100)

print('Today we will play a game.')             # Start game
print('The computer is picking a random number 1 - 100.')

print('What do you think the number is?')               # User guessing, add str(randomNum) to print string to test code knowing what the randomNum is.
guess = input()
guess_num = int(guess)              # Turning the guess into an integer

while guess_num != randomNum:
    if randomNum > guess_num:               # If the random number is higher
        print('Incorrect, the number is larger than that.')
    else:                                   # If the random number is lower
        print('Incorrect, the number is lower than that.')
    guess = input()
    guess_num = int(guess)              # Turning the guess into an integer again
    if guess_num == randomNum:              # If the number is correctly guessed after infinite attempts
        break                           # End if guessed correctly
print('You guessed correctly!')
