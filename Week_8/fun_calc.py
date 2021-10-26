def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def div(a,b):
    if(b!=0):
        return (a/b)
    else:
        print('invalid')
        return (0)
def mul(a,b):
    return (a*b)
def rem(a,b):
    return (a%b)

def menu(mes):
    print('Choose your selection:')
    for s in mes:
        print(s)
    a=int(input('Enter a number:'))
    return a
messages=['1-add', '2-sub', '3-mul', '4-div','5-rem']
a,b=map(int,input('Enter 2 numbers:').split())
i=menu(messages)
if i==1:
    s=add(a,b)
elif i==2:
    s=sub(a,b)
elif i==3:
    s=mul(a,b)
elif i==4:
    s=div(a,b)
elif i==5:
    s=rem(a,b)
else:
    print('Invalid number')

print('Result is:{}'.format(s))