from sistema_entidades.entidades import *
class Habilidade:
    def __init__(self, nome, dano, custo_mp, descricao, dano_proprio=0):
        self.nome = nome
        self.dano = dano
        self.custo_mp = custo_mp
        self.descricao = descricao
        self.self_dano = dano_proprio
    def usar(self, atacante, defensor):
        if atacante.mp >= self.custo_mp:
            atacante.mp -= self.custo_mp
            defensor.receber_dano(self.dano)
            return self.dano
        else:
            return False


