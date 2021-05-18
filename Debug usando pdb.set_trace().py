# Para utilizar o python debugger precisamos importar a biblioteca PDB ,
# e então utilizar a função set_trace()

# Comandos básicos do PDB
# l Para listar onde estamos no codigo
# n Proxima linha
# p Imprime Variavel
# c Continua a execução - Finaliza o debugging

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + 'Faz o curso ' + curso
print(final)
