import json

from cores import *
from menu_utilities import *
from json import *


def erro(texto):
    print(f'{VERMELHO}ERRO: {texto}{RESET}')


def menu_principal():
    estilização('MENU PRINCIPAL')
    print(f'{AMARELO}1{RESET} - {AZUL}Ver pessoas cadastradas{RESET}')
    print(f'{AMARELO}2{RESET} - {AZUL}Cadastrar nova pessoa{RESET}')
    print(f'{AMARELO}3{RESET} - {AZUL}Sair do sistema{RESET}')
    while True:
        try:
            op = int(input(f'{AMARELO}Sua Opção:{RESET} '))
        except (ValueError, TypeError):
            erro('DIGITE UMA OPÇÃO VÁLIDA')
        else:
            if 1 <= op <= 3:
                return op
            else:
                erro('DIGITE UMA OPÇÃO VÁLIDA')


def pessoas_cadastradas():
    estilização('PESSOAS CADASTRADAS')
    with open('pessoas.json', 'r') as arquivo:
        dados = json.load(arquivo)
    for pessoa in dados:
        nome = (f'{pessoa['Nome']}')
        idade = (f'{pessoa["Idade"]} Anos')
        print(f'{VERDE}{nome:<45}{idade:>45}{RESET}')



def cadastrar_pessoa():
    estilização('NOVO CADASTRO')
    nome = str(input(f'{VERDE}Nome:{RESET} '))
    while True:
        try:
            idade = int(input(f'{VERDE}Idade:{RESET} '))
        except (ValueError, TypeError):
            erro('DIGITE UMA IDADE VÁLIDA')
        else:
            break
    dados_usuario = {
        'Nome': nome,
        'Idade': idade,
    }
    with open('pessoas.json', 'r') as arquivo:
        dados = json.load(arquivo)
    dados.append(dados_usuario)
    with open('pessoas.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            erro('DIGITE UM NÚMERO INTEIRO')
        else:
            return num













