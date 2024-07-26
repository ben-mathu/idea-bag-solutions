class WordCounter:
  def count_words(self, sen: str) -> list:
    if len(sen) == 0:
      return 0, 0
    
    paragraphs = sen.split('\n')
    word_count = 0
    for para in paragraphs:
      word_count += len(para.split(' '))
    return word_count, len(paragraphs)
  
def main():
  counter = WordCounter()

  menu_options = 'Choose option:\n 0. Exit\n 1. Enter text to count'
  choosen_option = 1000
  
  while(choosen_option != '0'):
    print(menu_options)
    choosen_option = input()
    if (choosen_option == '1'):
      # sentence = input('Enter text to be checked:\nText: ')
      text = input("Input Text (For new lines add '\\n' to the end of the sentence): ")
      print()
      text = text.replace('\\n', '\n')
      word_count, paragraph_count = counter.count_words(text)
      print(f'Number of paragraphs: {paragraph_count}\nNumber of words: {word_count}\n' + (f'in {text}\n' if word_count > 0 else ''))
  print('Bye!')
  
if __name__ == '__main__':
  main()