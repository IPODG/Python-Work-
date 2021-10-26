number = float(input("Enter your number of minutes:"))
charge = 0.15*number
print("Your basic charge is",charge)

print("Current VAT is 20%")
Vat = charge*.2
print("20% of",number,"is £ {0:.2f} ".format(Vat))
total = Vat+charge
print("Total= £",total)









