# food = input("For the main dish do you want lasange or stirfry?")
#
# if food =="lasange":
#     sides = input("do you want garlic bead or fries?")
#     if sides == "garlic bread":
#         print("Your have ordered",food, "with a side of",sides)
#     if sides == "fries":
#         print("Your have ordered", food, "with a side of", sides)
# if food == "stirfry":
#     sides1 = input("Do you want noodles or crispy seaweed?")
#     if sides1 == "noodles":
#         print("Your have ordered", food, "with a side of", sides1)
#     if sides1 == "crispy seaweed":
#          print("Your have ordered", food, "with a side of", sides1)
#
# else:
#     print("This is not on the menu")

print("Main dishes are:")
print("1. Lasagne")
print("2. Stir Fry")
main_dish = int(input("Please select dish: "))

if main_dish == 1:
    print("Side dishes are:")
    print("1. Garlic bread")
    print("2. Fries")
    side_dish = int(input("Please select side dish: "))
    if side_dish == 1:
        print("You have selected Lasagne with garlic bread")
    elif side_dish == 2:
        print("You have selected Lasagne with fries")
    else:
        print("Invalid item selected")
elif main_dish == 2:
    print("Side dishes are:")
    print("1. Noodles")
    print("2. Crispy Seaweed")

    side_dish = int(input("Please select side dish: "))
    if side_dish == 1:
        print("You have selected Stirfry with Noodles")
    elif side_dish == 2:
        print("You have selected Stirfry with Crispy Seaweed")
else:
    print("Invalid item selected")