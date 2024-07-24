print("The Love Calculator is calculating your score...")
name1 = input("What is your name?").lower()
name2 = input("What is their name?").lower()

two_names = name1 + name2
first_number = 0
second_number = 0

t = two_names.count("t")
first_number += t
r = two_names.count("r")
first_number += r
u = two_names.count("u")
first_number  += u
e = two_names.count("e")
first_number += e

l = two_names.count("l")
second_number += l
o = two_names.count("o")
second_number += o
v = two_names.count("v")
second_number += v
second_number  += e

percet = str(first_number) + str(second_number)
percet_int = int(percet)

if (percet_int < 10) or (percet_int > 90):
    print(f"Your score is {percet_int}, you go together like coke and mentos.")
elif (percet_int >= 40) and (percet_int <= 50):
    print(f"Your score is {percet_int}, you are alright together.")
else:
    print(f"Your score is {percet_int}.")