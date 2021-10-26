width = int(input("What is your width?"))
height = int(input("What is your height?"))
length = int(input("What is your length?"))

sur = int(length*width*2) + int(length*height*2) + int(height*width*2)
vol = int(length*width*height)

print("Your surface area is", sur)
print("The volume is", vol)

