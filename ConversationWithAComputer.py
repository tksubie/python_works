print('Hello, what is your name my friend?')         # What is the users name
name = input()

print('Nice to meet you ' + name + ', quick question, I was wondering how old are you?')     # How old is the user
age = input()

print('Do you have any pet/pets, yes or no?')
prompt = input()
print('What is the name of one of your pets? If you do not have a pet type "no".')
pet_name = input()
if prompt == 'yes':     # If the user has pets
    print('That is neat, how old is ' + pet_name + '?')
    pet_age = input()       # The pets age
    age_personpet = str(int(age) - int(pet_age))        # Age the person would be if the pet was a baby when they got them
    print('Well, if you got ' + pet_name + ' as a baby, you would have been only ' + age_personpet + ' years old when you got ' + pet_name + '.')
    print('Pretty cool huh? Press enter please :)')

if prompt == 'no':       # If the user doesn't have pets
    print('That is a disappointment, you should get a pet.')
    print('Since you do not have a pet, do you wish to have a pet, yes or no?')
prompt_two = input()

if prompt_two == 'yes':         # Do you wish to have a pet, yes or no, also 10 + age in the string
    print('That is amazing, just do it! If you do, in 10 years you can be living your best life at ' + str(int(age) + int(10)) + ' years old, and kicking it with a furry friend!')
if prompt_two == 'no':
    print('You should do it come on! Just think, in 10 years you can be living your best life at ' + str(int(age) + int(10)) + ' years old, and kicking it with a furry friend!')

print('Entertain me then, if you were to choose between a cat, dog, or neither which would you choose?' + ' Or if your pet is a dog or a cat which is it?')     # Ending question
choice = input()
if choice == 'dog':
    print('Awesome, the person who wrote this program is also a dog person.')
    quit(print('Well, it was nice to get to know you ' + name + '. Have an amazing day fellow dog person, and happy ' + age + ' years on this planet so far!'))

if choice == 'cat':
    print('Not bad but dog people are cooler, but what are ya going to do, ya know?')
    quit(print('Well, it was nice to get to know you ' + name + '. Have an amazing day even if you are a cat person, and happy ' + age + ' years on this planet so far!'))

if choice == 'neither':
    print('There is no winning with you is there? Hopefully you have some kind of pet. If not that is fine I guess too.')
    quit(print('Well, it was nice to get to know you ' + name + '. Have an amazing day even if you are not a person with a dog or cat, and happy ' + age + ' years on this planet so far, with many more to go!'))
