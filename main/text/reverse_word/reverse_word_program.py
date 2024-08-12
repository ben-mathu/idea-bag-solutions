from main.common.program_menu import MainMenu
from main.text.palindrome_checker.palindrome_checker import reverse_word


def main():
    options = {
        0: "Exit",
        1: "Reverse Word"
    }
    main_menu = MainMenu(options)
    
    while main_menu.get_selected_option() != 0:
        main_menu.show_options()
        main_menu.set_selected_option(int(input()))
        
        if main_menu.get_selected_option() == 1:
            word = input("Enter Text to reverse\n >> ")
            revered_word = reverse_word(word)
            print(f"Reverse Word for {word} : {revered_word}")
            

if __name__ == "__main__":
    main()
    