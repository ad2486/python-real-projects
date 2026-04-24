import shutil

from interface_grafica.cores import *
from os import *
from random import *
from time import *

largura = shutil.get_terminal_size().columns

def formatar_texto(texto, fundo=RESET, cor=RESET):
    print(f'{fundo}{cor}{'-'*largura}{RESET}')
    print(f'{fundo}{texto:^{largura}}{RESET}')
    print(f'{fundo}{cor}{'-'*largura}{RESET}')


def limpar_tela():
    system('cls' if name == 'nt' else 'clear')

def leiaInt(val='<sem mensagem>'):
    while True:
        valor = input(f'{val}')
        try:
            int(valor)
            return int(valor)
        except:
            print('Digite um valor válido!')

def pausar():
    input('Pressione Enter para continuar...')

def rolar_dado(dados, lados):
    total = 0
    for dado in range(dados):
        final = randint(1, lados)
        total += final
    return total

def texto_suspense_vertical(texto, fundo=RESET, cor=RESET):
    for caractere in texto:
        print(f'{fundo}{cor}{caractere:^{largura}}{RESET}')
        sleep(0.35)

def texto_suspense_horizontal(texto, fundo=RESET, cor=RESET):
    espacos = ' ' * ((largura - len(texto)) // 2)
    print(f'{fundo}{cor}{espacos}{RESET}', end='', flush=True)
    for caractere in texto:
        print(f'{fundo}{cor}{caractere}{RESET}', end='', flush=True)
        sleep(0.35)
    print()

def leia_Int_mm(minimo, maximo, texto):
    while True:
        try:
            entrada = int(input(texto))
            if minimo <= entrada <= maximo:
                return entrada
            else:
                print(f"{VERMELHO}{'Digite um valor entre os oferecidos!':^180}{RESET}")
        except (ValueError, TypeError):
                print(f"{VERMELHO}{'Digite uma opção válida!':^180}{RESET}")



