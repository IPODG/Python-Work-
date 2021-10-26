
neg_sum = 0
pos_sum = 0

for i in range(4):
    print("Enter num {0}:".format(i+1),end="")
    num=int(input())
    if num > 0:
        pos_sum += num
    else:
        neg_sum += num
    print("Negative sum={0},Positive sum={1}".format(neg_sum,pos_sum))



pos = 1

for i in range(4):
    print("Enter number {0}".format(i+1,end=""))
    num1 = int(input())
    pos *= num1

print(pos)