def main():
  with open('encoded_data.txt', 'r') as file:
    res = ''

    unsorted_dict = {}
    for line in file:
      res = line.split(' ')
      unsorted_dict[int(res[0])] = res[1].strip()
    
    sorted_list = sorted(unsorted_dict)
    
    res = ''
    for key in sorted_list:
      decode_str = chr(int(unsorted_dict[key]) - 0xCafe)
      res = res + decode_str

    print(str(res))

if __name__ == "__main__":
  main()