from main.common.program_menu import MainMenu


def reverse_word(word: str) -> str:
    reversed_str = ''
    for i in range(len(word) - 1, -1, -1):
        reversed_str += word[i]

    return reversed_str


def check_if_palindrome(word: str) -> bool:
    if word == reverse_word(word):
        return True
    else:
        return False


def main():
    options = {
        0: 'Exit',
        1: 'Enter Text to Check'
    }
    main_menu = MainMenu(options)

    while main_menu.get_selected_option() != 0:
        main_menu.show_options()
        main_menu.set_selected_option(int(input()))
        
        if main_menu.get_selected_option() == 1:
            word = input('Enter text to be checked:\nText: ')
            print(word + ' is ' + ('' if check_if_palindrome(word) else 'not ') + 'a palindrome.\n')


if __name__ == '__main__':
    main()
