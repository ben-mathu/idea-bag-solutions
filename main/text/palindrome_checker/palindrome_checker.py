class PalindromeChecker:
  def reverse_word(self, word: str) -> str:
    reversed_str = ''
    for i in range(len(word)-1, -1, -1):
      reversed_str += word[i]
      
    return reversed_str
  
  def check_if_palindrome(self, word: str) -> bool:
    if word == self.reverse_word(word):
      return True
    else:
      return False
    
def main():
  menu_options = 'Choose option:\n 0. Exit\n 1. Enter Text to Check'
  choosen_option = 1000
  
  checker = PalindromeChecker()
  
  while(choosen_option != '0'):
    print(menu_options)
    choosen_option = input()
    if (choosen_option == '1'):
      word = input('Enter text to be checked:\nText: ')
            
      print(word + ' is ' + ('' if  checker.check_if_palindrome(word) else 'not ') + 'a palindrome.\n')
  print('Bye!')
  
if __name__ == '__main__':
  main()