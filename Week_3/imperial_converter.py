feet = float(input("What is your height in feet?"))
inches = float(input("What is your height in inches"))

hinch = float(inches/39.37)
hfeet = float(feet/3.281)

mme = hinch+hfeet

km = mme/1000
cm = mme*100
mm = mme*1000

print("Your height in Metres is","{0:.3f}" .format(mme),"m")
print("Your height in Kilometres","{0:.6f}" .format(km),"km")
print("Your height in Centimetres","{0:.1f}" .format(cm),"cm")
print("Your height in Millimetres","{0:.0f}" .format(mm),"mm")