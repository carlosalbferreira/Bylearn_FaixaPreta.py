# randint() -> Gera valores pseudo-aleatórios entre os valores estabelecidos.
from random import randint

# Gerador de apostas para a mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')
 # escolhe 6 números aleatório de 1 á 60 como se escolhesse os numero para mega-sena
