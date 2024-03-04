# A program that prints 2n where n goes from 1 to 100. Print one answer per line


print('How high can you count on X fingers?')               # Start of program
print('Press Enter:')

enter = input()             # Press Enter to start calculations

if enter == '':             # If statement so the calculations don't start right away

    for fingers in range(1, 101):               # for loop for 2**n from 1 to 100
        fingers_number = int(fingers)               # Amount of fingers changed to an integer
        calculation = 2**fingers_number
        print('If the number of fingers is ' + str(fingers) + ' you can count to ' + str(calculation) + '.')
