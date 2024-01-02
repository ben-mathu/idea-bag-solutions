from common.program_menu import MainMenu

class FactorialFinder:
  """
    Find the factorial of a number n
  """
  def find_factorial_rec(self, n: int) -> int:
    if n == 0:
      return 1
    return n * self.find_factorial_rec(n-1)
  
  def find_factorial_loop(self, n: int) -> int:
    if n == 0:
      return 1
    result = n
    for i in range(n-1, 0, -1):
      result *= i
    return result
  
def main():
  factorial_finder = FactorialFinder()
  menu_options = {
    0: 'Exit',
    1: 'Find factorial using Recursion',
    2: 'Find factorial using a loop'
  }
  
  main_menu = MainMenu(menu_options)

  while(main_menu.get_selected_option() != 0):
    main_menu.show_options()
    main_menu.set_selected_option(int(input()))
    
    print('\nEnter integer:')
    if main_menu.get_selected_option() == 1:
      val = int(input())
      result = factorial_finder.find_factorial_rec(val)

      print(f'The factorial of {val} is {result}')
    elif main_menu.get_selected_option() == 2:
      val = int(input())
      result = factorial_finder.find_factorial_loop(val)

      print(f'The factorial of {val} is {result}')
  print('Bye!')
  
if __name__ == '__main__':
  main()