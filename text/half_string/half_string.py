from common.menu import MainMenu

class HalfString:
  def half_string(self, val: str):
    if len(val) % 2 == 0:
      return True, val[:int(len(val)/2)]
    else:
      return False, "Invalid String"

def main():
  half_string = HalfString()
  menu_options = {
    0: 'Exit',
    1: 'Enter text to half'
  }
  main_menu = MainMenu(menu_options)
  
  while(main_menu.get_selected_option() != 0):
    main_menu.show_options()
    main_menu.set_selected_option(int(input()))
    
    if (main_menu.get_selected_option() == 1):
      text = input('Enter text to be halved:\nText: ')

      is_valid, half_text = half_string.half_string(text)
      print(f'Half string: {half_text}\n' if is_valid else f'{half_text}\n')
  print('Bye!')

if __name__ == "__main__":
  main()