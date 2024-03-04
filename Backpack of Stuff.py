import sys

itemsInBackpack = ["book", "computer", "keys", "travel mug"]

while True:
    print("Would you like to:")
    print("1. Add an item to the backpack?")
    print("2. Check if an item is in the backpack?")
    print("3. Quit")
    # print("4. Print Backpack list.")              # Check to see if code works
    userChoice = input()

    if userChoice == "1":
        print("What item do you want to add to the backpack?")
        itemToAdd = input()
        itemsInBackpack.insert(0, itemToAdd)  # Insert an item into the backpack, at the beginning of the list

    if userChoice == "2":
        print("What item do you want to check to see if it is in the backpack?")
        itemToCheck = input()

        if itemToCheck not in itemsInBackpack:  # If the Item is not in the backpack
            print('You do not have a ' + itemToCheck + ' in the backpack.')
        else:  # If the item is in the Backpack
            print('The ' + itemToCheck + ' is in the backpack.')

    if userChoice == "3":
        sys.exit()

# if userChoice == "4":               # Check to see if code works.
# print(itemsInBackpack)
