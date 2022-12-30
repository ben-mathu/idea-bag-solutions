from factorial_finder import FactorialFinder
from common.menu import MainMenu

class CombinationAndPermutations:
  def find_permutation(self, n: int, r: int) -> int:
    """ Calculates permutations

    Args:
        n (int): number of elements in a set
        r (int): number of elements to arrange from the set (order matters)

    Returns:
        int: number of permutations
    
    References:
        - https://byjus.com/maths/permutation-and-combination/
        - https://brilliant.org/wiki/permutations-with-repetition/
        - https://testbook.com/learn/maths-permutation-with-repetition/
    """
    factorial_finder = FactorialFinder()
    
    return factorial_finder.find_factorial_rec(n) / factorial_finder.find_factorial_rec(n-r)
  
  def find_combination(self, n, r) -> int:
    """ Calculates combination

    Args:
        n (int): number of elements in a set
        r (int): number of elements to arrange from the set (order does not matter)

    Returns:
        int: number of combinations
    """
    factorial_finder = FactorialFinder()

    return factorial_finder.find_factorial_rec(n) / (factorial_finder.find_factorial_rec(r) * factorial_finder.find_factorial_rec(n-r))
  
def main():
  combinations_and_permutations = CombinationAndPermutations()
  menu_options = {
    0: 'Exit',
    1: 'Find permutations',
    2: 'Find combinations'
  }
  
  main_menu = MainMenu(menu_options)
  
  while(main_menu.get_selected_option() != 0):
    main_menu.show_options()
    main_menu.set_selected_option(int(input()))
    
    prompt_set_length = 'Enter number of elements in a set:'
    prompt_choice_length = 'Enter number of elements to find'
    if main_menu.get_selected_option() == 1:
      print(prompt_set_length)
      n = int(input())
      print(f'{prompt_choice_length} permutations:')
      r = int(input())
      result = combinations_and_permutations.find_permutation(n, r)
      
      print(f'\nNumber of elements in set: {n}\nNumber of elements to find permutations: {r}\nPermutations: {result}\n')
    elif main_menu.get_selected_option() == 2:
      print(prompt_set_length)
      n = int(input())
      print(f'{prompt_choice_length} combinations:')
      r = int(input())
      result = combinations_and_permutations.find_combination(n, r)
      
      print(f'\nNumber of elements in set: {n}\nNumber of elements to find combinations: {r}\nCombinations: {result}\n')
  print('Bye!')
  
if __name__ == '__main__':
  main()