def check_path_valid(x, y, dep_dict, path_count, prev_x, child_index=0):
  if path_count == 2:
    print('Yes')
    return
  
  if x == y:
    path_count = path_count + 1
  
  x_list = dep_dict[x]
  if len(x_list) == 0:
    child_index = child_index + 1
    x = prev_x
  else:
    prev_x = x
    x = x_list[child_index]
  
  check_path_valid(x, y, dep_dict, path_count, prev_x, child_index,)

def main():
  with open('in/example_small.in', 'r') as file:
    t = file.readline().strip()
    
    for test in range(0, int(t)):
      n = file.readline().strip()

      dep_dict = {}

      x = ''
      y = ''
      
      for dep in range(0, int(n)):
        library = file.readline().split(' ')
        if dep == 0:
          x = library[1].strip()
        if dep == int(n) - 1:
          y = library[1].strip()
        dep_dict[library[1].strip()] = [item.strip() for item in library[2:]]
      
      print(dep_dict)
      
      check_path_valid(x, y, dep_dict, 0, x, 0)

if __name__ == '__main__':
  main()