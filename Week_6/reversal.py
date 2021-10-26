
numlist= []
for i in range(5):
    alist.append(int(input("num[{}]:".format(i+1))))
n = len(alist)-1
for num in range(n, -1, -1) :
    print ("{}".format(numlist[num]), end = " ")



