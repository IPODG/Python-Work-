names=[]
names = input("Enter your name: ").split()
for i in names:
    if "-" in i:
        name1, name2 = i.split("-")  #Find the dash and print both starts of nane
        print(name1[0], "-", name2[0], ".", sep="", end="")
    else:
        print(i[0],".",sep="",end="")