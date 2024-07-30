import random

names = ["Raissa", "Juci", "Hellen", "Hello"]
randon_lengh = len(names)

pay_bill = random.randint(1, randon_lengh - 1)
print(pay_bill)
print(f"{names[pay_bill]} is going to buy the meal today")