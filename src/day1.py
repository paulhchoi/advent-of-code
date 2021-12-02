input_file = 'input/day1.txt'

file_lines = open(input_file, 'r').readlines()

count = 0
previous_value = 0
increased = 0

for value in file_lines:
  current_value = int(value.strip())
  if previous_value < current_value and count != 0:
    increased += 1

  previous_value = current_value
  count += 1

print('increased = {}'.format(increased))
