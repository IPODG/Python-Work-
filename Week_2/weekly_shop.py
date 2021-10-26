peach = int(input("How many peaches?"))
p = float(input("How much?"))

bean = int(input("How many peaches?"))
b = float(input("How much?"))

chick = int(input("How many peaches?"))
c = float(input("How much?"))

sock = int(input("How many peaches?"))
s = float(input("How much?"))

wat = int(input("How many peaches?"))
w = float(input("How much?"))

items = int(peach + bean + chick + sock + wat)

cost = float(p*peach + b*bean + c*chick + s*sock + w*wat)

print("Total amount of items bought",items)
print("Cost of weekly shop", cost)