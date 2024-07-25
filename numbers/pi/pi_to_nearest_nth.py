from common.menu import MainMenu

class PrintPiToNearestNthDecimal:
  """A Program that allows the user to enter a number,
  then it prints out PI to nearest nth, number, decimal places
  """
  def __init__(self):
    self.limit = 1000
  
  def pi_to_nearest_nth(self, remainder, index, n, pi):
    if index == n or index >= self.limit:
      print('Value at n:', pi)
    else:
      div = int(remainder / 7)
      rem =  int(str(remainder % 7) + '0')
      if index == 0:
        pi += str(div) + '.'
      else:
        pi += str(div)
      
      self.pi_to_nearest_nth(rem, index+1, n, pi)


  def main(self):
    menu_options = {
      0: 'Exit',
      1: 'Enter number of decimal places.'
    }
    
    main_menu = MainMenu(menu_options)
    
    print('This program print the PI to the nearest nth decimal point.\nThe limit is', self.limit, '.')
    while main_menu.get_selected_option != 0:
      main_menu.show_options()
      main_menu.set_selected_option(int(input()))
      
      print('\nEnter a number: ')
      if main_menu.get_selected_option() == 1:
        val = int(input())
        result = self.pi_to_nearest_nth(val)
        
        print('PI to', val, 'is:', result)
    
    n = int(input('Enter a number n where n is the nth digit of PI:'))
    pi_printer.pi_to_nearest_nth(22, 0, n, '')

if __name__ == '__main__':
  
  pi_printer = PrintPiToNearestNthDecimal()
  pi_printer.main()