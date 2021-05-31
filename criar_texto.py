with open('Frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Digite uma fruta ou "sair" Para sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
# Usamos para criar um arquivo e fora da indentação ele ja mostra arquivo como fechado
# Sem precisar o close para fechar o mesmo
# e o arquivo ja fica criado com o nome que deu a ele no caso 'frutas'
# Mas tenha cuidado ao usar ele sobscreve o que ja tem...
# Abrir somente como leitura ai não seria alterado nada.
