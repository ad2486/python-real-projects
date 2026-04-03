from random import choice
jogadas = ['pedra', 'papel', 'tesoura',]
ganha = {
            'pedra': 'tesoura',
            'tesoura': 'papel',
             'papel': 'pedra'
             }
nome = input('Digite o nome do jogador:')
nomeformatado = nome.capitalize()
pontos_jogador = 0
pontos_pc = 0
         
#Bloco de verificação do número de rodadas
while True:
    rounds = int(input('Digite quantas rodadas você deseja, por favor apenas números ímpares:'))
    if rounds % 2 != 0 and rounds > 0:
        break
    else:
        print('Erro, por favor digite um número ímpar/valor válido!')
meta = (rounds + 1)//2 #Variável pra verificação de vitória em cada rodada 
contador_rounds = 1
while rounds > 0:
    print(f'Rodada {contador_rounds}')
    print(f'Placar: Você {pontos_jogador} - {pontos_pc} Computador')
    
    #Bloco de verificação da jogada do usuário
    while True:
        jg = input('Qual jogada você deseja fazer? (pedra, papel ou tesoura)').strip().lower()
        if jg not in jogadas:
            print('Jogada Inválida!')
        elif jg in jogadas:
            break
    
    
    #Bloco de decisão do vencedor
    pc = choice(jogadas)
    print(f'Computador escolheu {pc}')
    if jg == pc:
        print('Empate')
        contador_rounds = contador_rounds + 1
    elif ganha[jg] == pc:
        print(f'{nomeformatado} ganhou!')
        pontos_jogador = pontos_jogador + 1
        rounds = rounds - 1
        contador_rounds = contador_rounds + 1
    else:
        print('Computador ganhou!')
        pontos_pc = pontos_pc + 1
        rounds = rounds - 1
        contador_rounds = contador_rounds + 1
    
    
    #Bloco de verificação da meta de rodadas
    if pontos_jogador == meta:
        print(f'{nomeformatado} venceu o jogo!')
        print(f'Placar final: Você {pontos_jogador} - {pontos_pc} Computador')
        break
    elif pontos_pc == meta:
        print('Computador venceu o jogo!')
        print(f'Placar final: Você {pontos_jogador} - {pontos_pc} Computador')
        break
    
    
    

       

    