line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

position = input("Number:").upper()
position_one = position[0]
position_two = position[1]
position_two_int = int(position_two)

valor = "X"

if position_one == "A":
   position_one = 1
elif position_one == "B":     
   position_one = 2
elif position_one == "C":
   position_one = 3

position_one_int = int(position_one)

if position_one_int == 1 and position_two_int == 1:
    line1[0] = valor
elif position_one_int == 1 and position_two_int == 2:
    line2[0] = valor
elif position_one_int == 1 and position_two_int == 3:
    line3[0] = valor


if position_one_int == 2 and position_two_int == 1:
    line1[1] = valor
elif position_one_int == 2 and position_two_int == 2:
    line2[1] = valor
elif position_one_int == 2 and position_two_int == 3:
    line3[1] = valor

if position_one_int== 3 and position_two_int == 1:
    line1[2] = valor
elif position_one_int == 3 and position_two_int == 2:
    line2[2] = valor
elif position_one_int == 3 and position_two_int == 3:
    line3[2] = valor
print(f"{line1}\n{line2}\n{line3}")

