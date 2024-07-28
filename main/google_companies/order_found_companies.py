import os

with open(f'{os.path.dirname(os.path.realpath(__file__))}/companies_found.txt', 'r') as f:
  sorted_list = f.readlines()
  sorted_list = sorted(sorted_list, reverse=True)
  
  file = open(f'{os.path.dirname(os.path.realpath(__file__))}/companies_found.txt', 'w')

  for item in sorted_list:
    file.write(item)
  file.close()