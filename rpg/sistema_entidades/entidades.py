from random import *
class Entity:
    def __init__(self, hp, hp_max, level, atk, atk_max, defense, nome, speed, mp, mp_max):
        self.hp = hp
        self.hp_max = hp_max
        self.level = level
        self.atk = atk
        self.atk_max = atk_max
        self.defense = defense
        self.nome = nome
        self.speed = speed
        self.mp = mp
        self.mp_max = mp_max

    def __str__(self):
        return f'{self.nome}'

    def esta_vivo(self):
        return self.hp > 0

    def atacar(self):
        ataque = randint(self.atk, self.atk_max)
        return ataque

    def retornar_status(self):
        return self.hp, self.hp_max, self.level, self.atk, self.atk_max, self.defense, self.nome

    def receber_dano(self, dano):
        dano_real = max(0, dano - self.defense)
        self.hp = max(0, self.hp - dano_real)



class Personagem(Entity):
    def __init__(self, hp, hp_max, level, atk, atk_max, defense, nome, speed, mp, mp_max):
        super().__init__(hp, hp_max, level, atk, atk_max, defense, nome, speed, mp, mp_max)
        self.xp = 0
        self.xp_max = 100
        self.gold = 0
        self.inventario = []


    def ganhar_xp(self, xp_ganho):
        self.xp += xp_ganho
        while self.xp > self.xp_max:
            self.level += 1
            self.xp = self.xp - self.xp_max

    def ganhar_gold(self, gold_ganho):
        self.gold += gold_ganho

    def curar(self, cura):
        self.hp = min(self.hp_max, self.hp + cura)




class Inimigo(Entity):
    def __init__(self, hp, hp_max, level, atk, atk_max, defense, nome, speed, mp, mp_max):
        super().__init__(hp, hp_max, level, atk, atk_max, defense, nome, speed, mp, mp_max)
        self.xp_drop = 0
        self.gold_drop = 0
        self.item_drop = None
    def morreu(self):
        return self.xp_drop, self.gold_drop, self.item_drop

