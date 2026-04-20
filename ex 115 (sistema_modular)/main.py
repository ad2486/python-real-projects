from funcionalidades import *
from cores import *
while True:
    op = menu_principal()
    if op == 1:
        pessoas_cadastradas()
    elif op == 2:
        cadastrar_pessoa()
    else:
        print(f'{VERDE}Obrigado por usar o programa!{RESET}')
        break