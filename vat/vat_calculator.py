def main():
  '''
    Show menu for the user to add tax brackets
  '''
  
  tax_rate = 16
  cost = 0
  total_tax_inc = 0
  
  choosen_option = '1000'
  while(choosen_option != '0'):
    print('\nSelect an option by typing the number:\n 0. Exit\n 1. Enter Tax\n 2. Enter Cost\n 3. Calculate Tax\n')
    choosen_option = input()
    print()
    if (choosen_option == '1'):
      print('Enter tax rate: (16,8,...etc)')
      tax_rate = int(input())
      
      if (tax_rate > 100):
        print('Invalid tax input')
      tax_rate = 16
      continue
    elif (choosen_option == '2'):
      print('Add Cost: (This will be added to the existing amount)')
      cost += int(input())
      print(f"Total Amount: {cost}")
      continue
    elif (choosen_option == '3'):
      tax = tax_rate * cost / 100
      total_tax_inc = cost + tax
      
      print(f'Tax: {tax}, Total amount inclusive of tax: {total_tax_inc}')
      continue
    print('Invalid option')
  print('Bye!')

if __name__ == '__main__':
  main()