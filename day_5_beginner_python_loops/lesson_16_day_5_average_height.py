student_heights = input().split()
number_of_students = 0
total_height = 0

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  number_of_students += 1
  total_height += student_heights[n]

average_height = total_height / number_of_students
print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height:.0f}")

