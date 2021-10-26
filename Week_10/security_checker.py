import json
import os
data = {}
while(True)
    i=int(input('1.New user\n2.Exsisting user\n'))
    if i==1 or i==2:
        break
if i==!:
    if os.path.exsist('c:\\Users\\ss96\\Downloads\\data.txt'):
        with open('c//Users\\ss96\\Downloads\\data.txt') as infile:
            data = json.load(infile)
        while(True):
            password=input('Enter password:')
            if(len(password)<8)
                print(('password length must be >8'))
                continue
            elif password[0].isdigit()==True:
                print('Pass may not begin with number')
                continue
            elif '' in password:
                print('Password maynot contain space')
                continue
            else:
                break
        data[name] = password
        with open('c//Users\\ss96\\Downloads\\data.txt','w')as outfile:
            json.dump(data,outfile)
        print('Please log in')
        break
    if i==2

        with open('c//Users\\ss96\\Downloads\\data.txt','r')as infile:
            data=json.load(infile)

        name=input('Enter name:')
        if data.get(name)==None:
            print('No such name')
            quit()
        password=input('Enter password')
        if data[name]==password:
            print('Welcome')
        else:
            print('Invalid password')
