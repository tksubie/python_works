# Write a program that counts down from 10. Implement your program first with a while loop.
# Now implement your program with a for loop. Include both versions in your submission file.

print('We will countdown 10 to 0 using two different loops, a while loop and a for loop.')
print('Which loop would you like to start with? Type either "while" or "for" for which loop you choose:')               # Start of program

choice = input()

if choice == 'while':
    i = 10              # Starting the program at 10 to then count down.
    while i > -1:               # While loop to continue counting until 0
        print(i)
        i = i - 1               # Make it so the loop counts down, -1, from i = 10
    print('This is a while loop.')              # Tells you which loop you chose

if choice == 'for':               # If the user input is for the for loop you will receive this for loop
    for i in range(10, -1, -1):             # This is the for loop
        print(i)
    print('This is a for loop.')                # Tells you which loop you chose
