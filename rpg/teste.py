from sistema_batalha.batalha import *
from sistema_entidades.classes import *
from sistema_entidades.inimigos import *
from random import *
arthur = Guerreiro('Arthur')
inimigo = Goblin()
print(arthur.hp, arthur.speed)
print(inimigo.hp, inimigo.speed)
print(arthur.esta_vivo(), inimigo.esta_vivo())
resultado = batalha(arthur, inimigo)
vencedor, drops = batalha(arthur, inimigo)
print(vencedor)
print(drops)