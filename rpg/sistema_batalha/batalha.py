from sistema_batalha.habilidades import Habilidade
from sistema_entidades.entidades import *
from funções import *
from interface_grafica.cores import *
import shutil
largura = shutil.get_terminal_size().columns

def inicia(personagem, inimigo):
    if personagem.speed > inimigo.speed:
        return personagem
    else:
        return inimigo

def turno(atacante, defensor):
    if isinstance(atacante, Personagem):
        while True:
            ataque_ou_habilidade = input(f'{AMARELO}{'Deseja atacar ou usar uma habilidade? [a/h]\n'}{RESET}')
            if ataque_ou_habilidade == 'a':
                dano = atacante.atacar()
                defensor.receber_dano(dano)
                return dano
            elif ataque_ou_habilidade == 'h':
                habilidade = escolha_habilidade(atacante, f'{AMARELO}{'Escolha: '}{RESET}')
                return habilidade.usar(atacante, defensor)
            else:
                print(f'{VERMELHO}{'Escolha uma opção válida!'}{RESET}')
    else:
        dano = atacante.atacar()
        defensor.receber_dano(dano)
        return dano







def batalha(personagem, inimigo):
    quem_inicia = inicia(personagem, inimigo)
    while personagem.esta_vivo() and inimigo.esta_vivo():
        if quem_inicia == personagem:
            turno(personagem, inimigo)
            if inimigo.esta_vivo():
                turno(inimigo, personagem)
        else:
            turno(inimigo, personagem)
            if personagem.esta_vivo():
                turno(personagem, inimigo)
    if inimigo.esta_vivo():
        vencedor = inimigo
        return vencedor
    elif personagem.esta_vivo():
        vencedor = personagem
        return vencedor, inimigo.morreu()

def escolha_habilidade(personagem, texto):
    for c, habilidade in enumerate(personagem.habilidades):
        custo = f'MP: {habilidade.custo_mp}'
        print(f'{c+1:<{largura//3}}{habilidade.nome:^{largura//3}}{custo:>{largura//3}}')
    escolha = leia_Int_mm(1, 4, f'{AMARELO}{'Escolha uma habilidade:'}{RESET}')
    return personagem.habilidades[escolha - 1]




