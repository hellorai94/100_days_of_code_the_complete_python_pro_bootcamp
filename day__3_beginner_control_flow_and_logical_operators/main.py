print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $ 7.")
    elif age < 44 and age > 55:
        bill = 12
        print("Adulto tickets are $ 12.")
    else:
        print("Everything is going to be ok. Have a free ride on us!")
    whants_photo = input("Do you want a photo taken? Y or N.")
    if whants_photo == "Y":
        bill += 3
        print(f"Your total bill is {bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")





