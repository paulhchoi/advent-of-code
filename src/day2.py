input_file = 'input/day2.txt'

horiz = 0
vert = 0

file_lines = open(input_file, 'r').readlines()
for value in file_lines:
  direction, amount = value.split()
  amount = int(amount.strip())

  if direction == "forward":
    horiz += amount

  if direction == "up":
    vert -= amount

  if direction == "down":
    vert += amount

print (horiz * vert)