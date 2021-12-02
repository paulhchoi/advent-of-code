import sys
import os.path

def input_to_array(input_filepath):
  values = []
  full_filepath = os.path.dirname(__file__) + '/' + input_filepath

  file_lines = open(full_filepath, 'r').readlines()
  for value in file_lines:
    values.append(value)
  
  return list(map(parse_array_elements, values))


def parse_array_elements(n):
  parsed = int(n.strip())
  return parsed


def part1(values):
  
  return 


def part2(values):

  return 

if __name__ == "__main__":
  input_filepath = 'input.txt'
  values = input_to_array(input_filepath)

  if(len(sys.argv) > 1 and sys.argv[1] == '2'):
    answer = part2(values)
    print('== part 2 ==')
  else:
    answer = part1(values)
    print('== part 1 ==')

  print(answer)