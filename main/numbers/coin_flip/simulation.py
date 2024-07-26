from common.program_menu import MainMenu
from random import randrange

def flip_coin():
  return randrange(2)

def main():
  menu_options = {
    0: 'Exit',
    1: 'Flip Coin',
    2: 'Show Outcomes'
  }
  
  main_menu = MainMenu(menu_options)
  
  results = {
    'heads': 0,
    'tails': 0,
    'flips': 0
  }

  while(main_menu.get_selected_option() != 0):
    main_menu.show_options()
    main_menu.set_selected_option(int(input()))
    
    if main_menu.get_selected_option() == 1:
      result = flip_coin()
      print(f'Result: {result}')
      
      if (result == 0):
        results['heads'] = results['heads'] + 1
      else:
        results['tails'] = results['tails'] + 1
      
      results['flips'] = results['flips'] + 1
    elif (main_menu.get_selected_option() == 2):
      print(f'Results for {results["flips"]} flips:')
      
      print(f'Heads: {results["heads"]}')
      print(f'Tails: {results["tails"]}')
    elif (main_menu.get_selected_option() > 2 or main_menu.get_selected_option() < -1):
      print('Invalid option! Please try again.')
    print()
  print('Bye!')

if __name__ == '__main__':
  main()