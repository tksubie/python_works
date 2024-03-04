print('Please enter your name to continue.')
name = input()              # Receiving users name

print('Hello ' + name + ', good day to you. We are here to know whether or not you can vote.')
print('Please input your age as an integer:')
age = input()  # Figuring out age of user
new_age = int(age)              # Making age an integer

if new_age >= 18:             # If age is greater than or equal to 18, user can vote
    quit(print('Perfect ' + name + ', you are of legal voting age!'))

else:               # If age is not greater than or equal to 18, user can not vote
    quit(print('Sorry to inform you ' + name + ', you are not old enough to vote yet.'))
