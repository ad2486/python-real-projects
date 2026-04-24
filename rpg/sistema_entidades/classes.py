from sistema_entidades.entidades import *
from sistema_batalha.habilidades import *
class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(hp=250, hp_max=250, level=1, atk=10, atk_max=35, defense=25, nome=nome, speed=8, mp=30,
                         mp_max=30)
        self.habilidades = [
            Habilidade('Corte Duplo', 30, 10, 'Um corte extremamente rápido!'),
            Habilidade('Golpe do Sgt.Fahur', 75, 25, 'Herde o poder da Lenda!'),
            Habilidade('Golpe Fofo', 25, 5, 'Fofo não quer dizer não perigoso...'),
            Habilidade('Raivinha', 40, 18, '50/50 irmão', 20)
        ]

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(hp=175, hp_max=175, level=1, atk=15, atk_max=20, defense=15, nome=nome, speed=10, mp=50, mp_max=50)
        self.habilidades = [
            Habilidade('Bola de Fogo', 38, 15, 'Bola de fogo clássica de Mago!'),
            Habilidade('Hipinose de OnlyFans', 85, 45, 'Brutal, sobra nada pro Betinha...'),
            Habilidade('Jatinho de Água', 28, 10, 'Jatinho Broxa'),
            Habilidade('Libertação do Betinha', 50, 25, 'Libertários não Morrem...')
        ]

class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(hp=210, hp_max=210, level=1, atk=25, atk_max=30, defense=20, nome=nome, speed=12, mp=40, mp_max=40)
        self.habilidades = [
            Habilidade('Flechada Venenosa', 35, 18, 'Veneno extraído diretamente daquela tua amiga..'),
            Habilidade('Facadinha do Carioca', 40, 20, 'Cuidado ao atravessar o RJ...'),
            Habilidade('Flechada do Cupido', 25, 10, 'Não viaja, ela não te ama.'),
            Habilidade('Roleta Russa', 60, 20, 'Ou tu se dá bem ou tu se ferra, não tem', 30)
        ]