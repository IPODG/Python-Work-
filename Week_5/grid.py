
columns = int(input("Enter amount of columns"))
rows = int(input("Enter amount of rows"))

for i in range(rows):
    for j in range(columns):
        print("*", end="")
    print()

#put comma inbetween to seperate rows and columns. Thats what split is for
(r, c) = map(int,input('enter row and column:').split(','))
for i in range(r):
    for j in range(c):
        print('*',end=""),
    print('')

(r, c) = map(int,input('enter row and column:').split(','))
i=0
while(i<r):
    j=0
    while(j<c):
        print('*',end=""),
        j+=1
    print('')
    i+=1