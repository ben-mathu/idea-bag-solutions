# Happy Numbers
# Eventually evaluates to 1 when the number is replaced by the square
# of its digits. eg. 13 evaluates 1^2 + 3^2 = 10, 1^2 + 0^2 = 1

from common.program_menu import MainMenu

def find_happy_number(val: int) -> bool:
  if (val < 0):
    return False
  
  num_list = []
  
  digits_sum = 0
  temp_val = val
  while (digits_sum != 1):
    digits_sum = sum([pow(int(item), 2) for item in str(temp_val)])
    if (num_list.__contains__(digits_sum)):
      return False
    else:
      num_list.append(digits_sum)
    temp_val = digits_sum
    
  if (digits_sum == val):
    return False
  elif (digits_sum == 1):
    return True
  else:
    return False

def find_list_of_happy_numbers(n: int) -> []:
  number_list = []
  num = 1
  while (len(number_list) < n):
    if (find_happy_number(num)):
      number_list.append(num)
    num += 1
      
  return number_list

def main():
  menu_options = {
    0: 'Exit',
    1: 'Enter A Number',
    2: 'Get list of happy numbers'
  }
  
  main_menu = MainMenu(menu_options)

  while(main_menu.get_selected_option() != 0):
    main_menu.show_options()
    main_menu.set_selected_option(int(input()))
    
    if main_menu.get_selected_option() == 1:
      print('\nEnter any number:')
      val = int(input())
      result = find_happy_number(val)

      print()
      if (not result):
        print(f'{val} is an Unhappy Number.')
      else:
        print(f'{val} is a Happy Number.')
    elif (main_menu.get_selected_option() == 2):
      print('\nEnter the range of happy numbers:')
      val_range = int(input())
      result = find_list_of_happy_numbers(val_range)
      
      print(f'{val_range} Happy Numbers are: {result}.')
    else:
      print('Invalid option! Please try again.')
    print()
  print('Bye!')
  
if __name__ == '__main__':
  main()