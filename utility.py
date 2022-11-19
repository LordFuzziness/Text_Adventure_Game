from os import system, name

def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')