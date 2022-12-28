import re
import os

class morse_code_maker:
  """
    This class generates morse code and defines its own standards for space between
    words and letters
    
    single space (' ') represents the space between letters
    three spaces ('   ') represents space between words
  """
  def __init__(self) -> None:
    self.single_space = ' '
    self.three_space = '   '
    self.morse_dict = {
      'a': '·−',
      'b': '−···',
      'c': '−·−·',
      'd': '−··',
      'e': '·',
      'f': '··−·',
      'g': '−−·',
      'h': '····',
      'i': '··',
      'j': '·−−−',
      'k': '−·−',
      'l': '·−··',
      'm': '−−',
      'n': '−·',
      'o': '−−−',
      'p': '·−−·',
      'q': '−−·−',
      'r': '·−·',
      's': '···',
      't': '−',
      'u': '··−',
      'v': '···−',
      'w': '·−−',
      'x': '−··−',
      'y': '−·−−',
      'z': '−−··',
      '1': '·−−−−',
      '2': '··−−−',
      '3': '···−−',
      '4': '····−',
      '5': '·····',
      '6': '−····',
      '7': '−−···',
      '8': '−−−··',
      '9': '−−−−·',
      '0': '−−−−−',
    }
    
  def morse_code_converter(self, val: str) -> str:
    words_arr = val.lower().split(' ')
    
    morse_code = ''
    for i in range(len(words_arr)):
      word = words_arr[i]
      for j in range(len(words_arr[i])):
        letter = word[j]
        
        if re.match('\\W', letter):
          continue
        
        if (j == len(word)-1):
          morse_code += self.morse_dict[letter]
        else:
          morse_code += self.morse_dict[letter] + ' '
      
      if (i != len(words_arr)-1):
        morse_code += '   '
    
    return morse_code
        
def make_beep_sounds(morse_code: str):
  for item in morse_code:
    if item == '·':
      print(end='\007')
    elif item == '−':
      print(end='\007')

def main():
  menu_options = 'Choose option:\n 0. Exit\n 1. Enter Text to Convert to Morse Code'
  choosen_option = 1000

  morse_coder = morse_code_maker()
  
  while(choosen_option != '0'):
    print(menu_options)
    choosen_option = input()
    if (choosen_option == '1'):
      sen = input('Enter text to be converted:\nText: ')
      morse_code_str = morse_coder.morse_code_converter(sen)
      
      make_beep_sounds(morse_code_str)
            
      print(f'Morse Code: {morse_code_str}\n')
  print('Bye!')
  
if __name__ == '__main__':
  main()