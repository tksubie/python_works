import csv
import sys

# The password list - We start with it populated for testing purposes
passwords = [["yahoo","XqffoZeo"],["google","CoIushujSetu"]]


# The password file name to store the passwords to
passwordFileName = "samplePasswordFile"

# The encryption key for the caesar cypher
encryptionKey = 16


# Caesar Cypher Encryption
def passwordEncrypt(unencryptedMessage, key):
    # We will start with an empty string as our encryptedMessage
    encryptedMessage = ''

    # For each symbol in the unencryptedMessage we will add an encrypted symbol into the encryptedMessage
    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol

    return encryptedMessage


def loadPasswordFile(fileName):
    with open(fileName, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)

    return passwordList


def savePasswordFile(passwordList, fileName):
    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)


while True:
    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Lookup a password")
    print(" 3. Add a password")
    print(" 4. Save password file")
    print(" 5. Print the encrypted password list (for testing)")
    print(" 6. Delete a password")              # Added Delete a password
    print(" 7. Delete a Website")               # Added Delete a Website
    print(" 8. Delete list")                # Added delete the whole list
    print(" 9. Quit Program")
    print("Please enter a number (1-9)")
    choice = input()

    if choice == '1':               # Load the password list from a file
        passwords = loadPasswordFile(passwordFileName)

    if choice == '2':               # Lookup at password
        print("Which website do you want to lookup the password for?")
        for keyvalue in passwords:                  # Gives you options for which website
            print(keyvalue[0])
        passwordToLookup = input()

        for i in range(len(passwords)):             # 1. Create a loop that goes through each item in the password list

            if passwordToLookup == passwords[i][0]:             # 2. Check if the name is found. Name is [i][0]

                print(passwordEncrypt(passwords[i][1], -encryptionKey))                # 3. If the name is found then decrypt it and printed it.

    if choice == '3':               # Add a Password
        print("What website is this password for?")
        website = input()
        print("What is the password?")
        unencryptedPassword = input()

        encryptedPassword = passwordEncrypt(unencryptedPassword, encryptionKey)             # Step 1

        newaddedPassword = [website, encryptedPassword]             # Step 2

        passwords.append(newaddedPassword)              # Step 3

    if choice == '4':               # Save the passwords to a file
        savePasswordFile(passwords, passwordFileName)

    if choice == '5':               # print out the password list
        for keyvalue in passwords:
            print(', ' .join(keyvalue))

    if choice == '6':               # Delete a Password
        print("These are your websites:")
        for keyvalue in passwords:                  # Gives you options for which website
            print(keyvalue[0])
        passToDelete = input('Delete which website password? :')

        for i in range(len(passwords)):             # Goes through items in the password list

            if passToDelete == passwords[i][0]:         # Checks it

                del passwords[i][1]                 # remove password from website
                print('You have deleted your selected password.')

    if choice == '7':               # Delete Website
        print("These are your websites:")
        for keyvalue in passwords:                  # Gives you options for which website
            print(keyvalue[0])
        websiteToDelete = input('Delete which website? :')

        for i in range(len(passwords)):             # Goes through items in the password list

            if websiteToDelete == passwords[i][0]:         # Checks it

                del passwords[i][0]                 # remove password from website
                print('You have deleted your selected website.')

    if choice == '8':               # Delete List and start over
        del passwords[:]                # Delete the list contents
        print('Password list is clear of all values.')

    if choice == '9':               # quit our program
        sys.exit()

    print()
    print()
