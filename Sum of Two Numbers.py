# Write a program that asks for two numbers.
# If the sum of the numbers is greater than 100, print "They add up to a big number"
# if it is less than/equal to 100 than print "They add up to ____".

print('Hello, lets play a game.')               # Start

print('Give me a random number:')               # Give me the first number
one_number = input()
one_number_in = float(one_number)                 # Make that number a floating variable

print('I would like one more number please:')   # Given the second number
sec_number = input()
sec_number_in = float(sec_number)                 # Second number an floating variable

print('Wait one while I compute...')                # Computing the data for flair
print('.')
print('.')
print('.')
print('.')
print('.')

if one_number_in + sec_number_in > 100:             # First prompt
    print('They add up to a big number.')

else:                                               # Second prompt
    print('They add up to ' + str(one_number_in + sec_number_in) + '.')
