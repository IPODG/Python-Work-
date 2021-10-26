print()
selectedClass = (int(input("Please enter the number of the class you would like to be: ")) - 1)
print("You chose", classLabel[selectedClass])


def printStats():
    print()
    # Player specification
    print("Your specs:")
    print('Class'.ljust(15, ' ') + "|", end='')
    for key in range(0, len(specLabel)):
        print((str(key + 1) + " : " + str(specLabel[key])).center(20, ' ') + "|", end='')
    print()
    print('Player'.ljust(15, ' ') + "|", end='')
    for column in range(0, 5):
        print(str(player[column]).center(20, ' ') + "|", end='')
    print()

    print(classLabel[selectedClass].ljust(15, ' ') + "|", end='')
    for column in range(0, 5):
        print(str(minimumSpecs[selectedClass][column]).center(20, ' ') + "|", end='')
    print()

    print('Deficit'.ljust(15, ' ') + "|", end='')
    for column in range(0, 5):
        if player[column] - minimumSpecs[selectedClass][column] < 0:
            print(str(player[column] - minimumSpecs[selectedClass][column]).center(20, ' ') + "|", end='')
        else:
            print("0".center(20, ' ') + "|", end='')
    print()
    surplus = 0
    print('Surplus'.ljust(15, ' ') + "|", end='')
    for column in range(0, 5):
        if player[column] - minimumSpecs[selectedClass][column] > 0:
            print(str(player[column] - minimumSpecs[selectedClass][column]).center(20, ' ') + "|", end='')
            surplus += player[column] - minimumSpecs[selectedClass][column]
        else:
            print("0".center(20, ' ') + "|", end='')
    print("\nYou have", surplus, "points to exchange.")


printStats()

while surplus > 0:
    selectedChar = int(input("Please select the spec you would like to exchange: ")) - 1
    numberOfPoints = player[selectedChar] - minimumSpecs[selectedClass][selectedChar]
    print("You have", numberOfPoints - 3, "points to exchange from", specLabel[selectedChar] + ".")
    numberToExchange = ((numberOfPoints - 3) - (numberOfPoints - 3) % 2) / 2
    numberPoints = int(input("How many points would you like to exchange (Max of {}".format(numberToExchange) + "): "))
    location = int(input("Where would you like to put these points: "))
    player[selectedChar] -= (numberPoints * 2)
    player[location - 1] += numberPoints
    printStats()
    choice = input("Are you ready to proceed y/n: ")
    if choice[0].lower() == "y":
        for key in range(0, len(specLabel)):
            if minimumSpecs[selectedClass][key] > player[key]:
                invalidInput = True
                print("Your character is not valid.")
                input()
        surplus = 0
    else:
        print("Character is valid.")
        input()
        surplus = surplus