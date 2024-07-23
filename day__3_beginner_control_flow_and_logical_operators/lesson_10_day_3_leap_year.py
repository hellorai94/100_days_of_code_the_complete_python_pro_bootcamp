year = int(input())

if year % 4 != 0:
    print("Not leap year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 != 0:
    print("Not leap year")
else:
    print("Leap year")
            

# Se não for divisível por 4, não é bissexto.
# Se for divisível por 4, mas não por 100, é bissexto.
# Se for divisível por 100, mas não por 400, não é bissexto.
# Se for divisível por 400, é bissexto.

