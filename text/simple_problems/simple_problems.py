from common.program_menu import MainMenu

class SimpleProlems:
  def fizz_buzz(self, n: int) -> None:
    for i in range(1, n):
      if i % 3 == 0:
        print("Fizz", end="")
        if i % 5 == 0:
          print("Buzz", end="")
      elif i % 5 == 0:
        print("Buzz", end="")
      else:
        print(i, end="")
      print()
        
def main() -> None:
  simple_problems = SimpleProlems()
  
  menu_options = {
    0: 'Exit',
    1: 'FizzBuzz'
  }
  main_menu = MainMenu(menu_options)
  
  while main_menu.get_selected_option() != 0:
    main_menu.show_options()
    main_menu.set_selected_option(int(input()))
    
    if main_menu.get_selected_option() == 1:
      n = int(input('Enter number to print to:\n'))
      simple_problems.fizz_buzz(n)
      print()
  
if __name__ == '__main__':
  main()
