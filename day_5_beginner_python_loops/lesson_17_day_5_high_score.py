student_scores = input().split()
maior = 0

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  if student_scores[n] > maior:
    maior = student_scores[n]

print(f"The highest score in the class is: {maior}.")




