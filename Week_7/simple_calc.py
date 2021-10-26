# a, b, c = input("Enter a three value: ").split()
# print("Number 1 equals : ", a)
# print("Number 2 equals : ", b)
# print("Your operator is : ", c)
# print()
#
# sum = (a ,c ,b)
#
# print(sum)


# a, b, operator = input("Enter two numbers and an operator: ").split()
#
# function = {
#     '+': lambda x,y: x+y,
#     '-': lambda x,y: x-y,
#     '*': lambda x,y: x*y,
#     '/': lambda x,y: x/y
# }[operator]
#
# if operator == '/' and b == '0':
#     print("Can't divide by zero")
# else:
#     print(f"{a} {operator} {b} = {function(int(a), int(b))}")

a,b,c=(input('Enter sum:').split())
a = int(a)
b = int(b)
print("You entered :{} {} {} and the answer is ".format(a,c,b), end="")
if c== "+":
    print('{}'.format(a+b))
if c=='*':
    print('{}'.format (a*b))
if c== "/":
    if b==0:
        print('Invalid number--->0')
    else:
        print('{}'.format (a/b))
if c=='-':
    print('{}'.format (a-b))
else:
    print(' invalid operator-->{}'.format(c))