
list1 = []
list2 = []
vote = " "

while vote != "1":
    print("*" * 10)
    print("Candidate A")
    print("Candidate B")
    print("Candidate C")
    print("Candidate D")
    print("Candidate E")
    print("Exit: 1")
    print("*" * 10)
    vote = input("Please enter the letter of the candidate you want to vote for: ").upper()
    list1.append(vote)

list2.append(("A:", list1.count("A")))
list2.append(("B:", list1.count("B")))
list2.append(("C:", list1.count("C")))
list2.append(("D:", list1.count("D")))
list2.append(("E:", list1.count("E")))

i = (sorted(list2, key=lambda x: x[1], reverse=True))
print(*i[0][0][0], "is the winner!")
print("Results: ")
for j in range(len(i)):
    print(*i[j])