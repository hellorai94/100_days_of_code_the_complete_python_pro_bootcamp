print("WELCOME TO THE TIP CALCULATOR!!")
total_bill = input("What was the total bill?")
tip = input("How much tip would you lije to give?, 10, 12 or 15?")
people = input("How many people to split the bill?")

bill_with_tip = (float(total_bill) * (1 + (int(tip) / 100)))
pay = (float(bill_with_tip) / int(people))

print(f"Each person shoud pay: $ {round(pay,2)}")