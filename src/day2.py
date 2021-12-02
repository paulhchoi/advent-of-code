input_file = 'input/day2.txt'

horiz = 0
vert = 0
aim = 0

file_lines = open(input_file, 'r').readlines()
for value in file_lines:
  direction, amount = value.split()
  amount = int(amount.strip())

  if direction == "down":
    aim += amount

  if direction == "up":
    aim -= amount

  if direction == "forward":
    horiz += amount
    vert += aim * amount

print (horiz * vert)