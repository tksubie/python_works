listToPrint = []
while True:
    newWord = input("Enter a word to add to the list (press return to stop adding words) > ")
    if newWord == "":
        break
    else:
        listToPrint.append(newWord)

if len(listToPrint) > 1:                # If the list is only 1 value, do not add 'and' to the last item in list
    listToPrint.append('and ' + listToPrint[-1])                # Add 'and' to the last item in the list
    del listToPrint[-2]             # Delete the extra item to the list from the append.
    print(listToPrint)
else:
    print(listToPrint)
