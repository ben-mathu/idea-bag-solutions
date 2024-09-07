# Command Line Application Menu (Interface)

A python module that contains a class to that help manage command line application menu.
An Example of a commang line menu:

```
    Application to generate the fibonacci sequence
    
    Choose an option below:
    0. Exit
    1. Recursive Function
    2. For Loop
```
## Usage

Install the package
```shell
    pip install commons-benatt @ git+ssh://git@github.com/ben-mathu/idea-bag-solutions/@ba19c1c9f8c41a023d48da3dbfb27aecb564e521#subdirectory=common
```

Import the package

```python
    from program_menu import MainMenu
```

```python
    options = {
      0: "Exit",
      1: "Recursive Function",
      2: "For Loop"
    }
    menu = MainMenu(options=options)

    while (menu.get_selected_option() != 0):
      menu.show_options()
      menu.set_selected_option(int(input('\n>> ')))

      if menu.get_selected_option() == 1:
        use_recursive()
      elif menu.get_selected_option() == 2:
        use_for_loop()
    print('Bye')
```
