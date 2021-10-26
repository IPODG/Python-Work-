num = 10
rainbow = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

while num != -1:
    num = int(input("Enter an integer from 1 to 7 or -1 to quit: "))
    if num == -1:
        print("Program end.")
    elif num < 1 or num > 7:
        print("Your input is invalid, please try again.")
        print("*" * 40)
    else:
        print("Rainbow colour: {}".format(rainbow[num-1]))
        print("*" * 40)

