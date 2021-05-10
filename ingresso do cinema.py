# Escolhendo um filme (básico)
def comprando_ingresso(idade):
    if idade < 18:
        print(f'Que pena {nome} você ainda não pode comprar sozinha(o) ')
        return False
    else:
        print('Ótimo vamos passar os FILMES que temos para você')
        return True

def escolher_filme():
    print('Escolha qual filme gostaria de assistir')
    print('1 - Van hellsing  2 \n2 - Veloses e furiosos \n3 - A lagoa azul\n4 - Procurando nemo')

    return int(input())

def preco_do_filme(escolher):
    vanhelsin = 35.00
    velosesefuriosos = 50.00
    alagoaazul =  10.00
    procurandonemo = 30.00

    if escolher ==  1:
        return vanhelsin
    elif escolher == 2:
        return velosesefuriosos
    elif escolher == 3:
        return alagoaazul
    elif escolher == 4:
        return procurandonemo


nome = str(input('Digite seu nome: '))
idade = int(input('Digite a sua idade: '))

if comprando_ingresso(idade):
    escolher = escolher_filme()


    print('Ótima escolha vou calcular o valor do seu ingresso')
    valor = (preco_do_filme(escolher))

    print(f'O valor do filme será R${preco_do_filme(escolher)}')
