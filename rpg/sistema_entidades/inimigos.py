from sistema_entidades.entidades import *
from random import choice
nomes_esqueleto = ['Esqueleto', 'Papyrus', 'Sans', 'Ainz Oaal Goon', 'Momonga']


class Goblin(Inimigo):
    def __init__(self):
        super().__init__(hp=55, hp_max=55, atk=8, atk_max=15, defense=5, speed=15, level=1, mp=0, mp_max=0, nome='Goblin')
        self.xp_drop = 25
        self.gold_drop = 8
        self.item_drop = None

class Esqueleto(Inimigo):
    def __init__(self):
        super().__init__(hp=80, hp_max=80, atk= 12, atk_max=20, defense=7, speed=8, level=1, mp=0, mp_max=0, nome=choice(nomes_esqueleto))
        self.xp_drop = 30
        self.gold_drop = 10
        self.item_drop = None

class Ogro(Inimigo):
    def __init__(self):
        super().__init__(hp=200, hp_max=200, atk=15, atk_max=35, defense=10, speed=2, level=1, mp=0, mp_max=0, nome='Ogro')
        self.xp_drop = 70
        self.gold_drop = 15
        self.item_drop = None

class Mago_Sombrio(Inimigo):
    def __init__(self):
        super().__init__(hp=70, hp_max=70, atk=25, atk_max=50, defense=5, speed=8, level=1, mp=0, mp_max=0, nome='Mago Sombrio')
        self.xp_drop = 40
        self.gold_drop = 50
        self.item_drop = None


'''
Goblin — fraco, rápido, fácil de matar, pouco XP
Esqueleto — médio, equilibrado
Ogro — lento, muito HP e defesa, difícil de matar
Mago Sombrio — frágil mas causa muito dano
'''