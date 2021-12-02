input_file = 'input/day1.txt'

file_lines = open(input_file, 'r').readlines()
values = []
for value in file_lines:
  current_value = int(value.strip())
  values.append(current_value)

sums = values + values[:3]
window_sums = [sum(sums[i:i+3]) for i in range(len(values))]

count = 0
previous_value = 0
increased = 0

for value in window_sums:
  current_value = value
  if previous_value < current_value and count != 0:
    increased += 1

  previous_value = current_value
  count += 1

print('increased = {}'.format(increased))
