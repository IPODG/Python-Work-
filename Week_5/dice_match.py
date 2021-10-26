


import random
count=0
while(True):
    die1=random.randint(1,6)
    die2 = random.randint(1,6)
    count+=1
    print("die1={0},die2={1}".format(die1,die2))
    if die1==die2:
        break
print("Number of throw={0}".format(count))



