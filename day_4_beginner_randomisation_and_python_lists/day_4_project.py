import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choose = int(input("What do you choose? TYpe 0 for Rock, 1 for Paper or 2 for Scissors:"))

computer = random.randint(0,2)
print(computer)

if choose == 0 and computer == 0:
    print(rock)
    print("Computer chose:")
    print(rock)
    print("It's a draw.")
elif choose == 0 and computer == 1:
    print(rock)
    print("Computer chose:")
    print(paper)
    print("You lose.")
elif choose == 0 and computer == 2:
    print(rock)
    print("Computer chose:")
    print(scissors)
    print("You win.")
elif choose == 1 and computer == 0:
    print(paper)
    print("Computer chose:")
    print(rock)
    print("You win.")
elif choose == 1 and computer == 1:
    print(paper)
    print("Computer chose:")
    print(paper)
    print("It's a draw.")
elif choose == 1 and computer == 2:
    print(paper)
    print("Computer chose:")
    print(scissors)
    print("You lose.")
elif choose == 2 and computer == 0:
    print(scissors)
    print("Computer chose:")
    print(rock)
    print("You lose.")
elif choose == 2 and computer == 1:
    print(scissors)
    print("Computer chose:")
    print(paper)
    print("You win.")
elif choose == 2 and computer == 2:
    print(scissors)
    print("Computer chose:")
    print(scissors)
    print("It's a draw.")
