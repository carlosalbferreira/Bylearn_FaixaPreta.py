def divisao(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Número não pode ser dividido por ZERO'


num1 = int(input('Digite um número para dividir : '))
num2 = int(input('Digite outro número para dividir: '))

print(divisao(num1, num2))
