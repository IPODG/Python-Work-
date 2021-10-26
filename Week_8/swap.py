def print_int_list(numbers):
    print("You chose:", *numbers)


def swap(numbers):
    numbers.reverse()
    print("Swapped:", *numbers)


numbers = input("Please enter 2 integers: ").split()
print_int_list(numbers)
swap(numbers)