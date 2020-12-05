print("What is the bill amount?")
bill_amount = float(input("Enter the bill amount"))
print("$", bill_amount)

print("What is the tip rate?")
tip_rate = float(input("Enter tip rate?"))
print(tip_rate,"%")

tip = round(bill_amount * (tip_rate / 100), 2)

total_amount = bill_amount + tip

print("Your Tip is: $ ", tip)
print("Your Total is: $ ",  total_amount)
