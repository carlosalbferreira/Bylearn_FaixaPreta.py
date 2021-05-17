def divisao(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Número não pode ser dividido por ZERO'


num1 = input('Digite um número para dividir : ')
num2 = input('Digite outro número para dividir: ')

print(divisao(num1, num2))

# Outra Forma de fazer a correção é:
# Já informando os dois erros em uma só linha 

def divisao(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError):
        return 'Ocorreu um problema verifique suas informações'


num1 = input('Digite um número para dividir : ')
num2 = input('Digite outro número para dividir: ')

print(divisao(num1, num2))
