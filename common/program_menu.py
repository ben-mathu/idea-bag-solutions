class MainMenu:
  """
    How to use:
      - Create a key<int>, value<string> pair, listing all menu options
      - When ready show options
      - then set selected option menu when user enters an input
      - check against the options what the user has entered
  """
  def __init__(self, options) -> None:
    self.menu_options = options
    self.selected_option = 1000
  
  def show_options(self):
    print('Choose an option below:')
    for k in self.menu_options:
      print(f'{k}: {self.menu_options[k]}')
    print()
  
  def set_selected_option(self, selected_option: int) -> None:
    self.selected_option = selected_option
    
  def get_selected_option(self) -> int:
    return self.selected_option
  
  def get_menu_options(self) -> dict:
    return self.menu_options