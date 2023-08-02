# def saudacao(msg='Olá', nome='usuario'):
#     nome = nome.replace('e', '3')
#     msg = msg. replace('e', '3')
#     return f'{msg} {nome}'
#
# variavel = saudacao('ole', 'zeca')

# print(variavel)

# def funcao(var):
#      return var
#
# variavel = funcao('Oi tudo bem')
# print(variavel)

# def divisao(n1, n2):
#     if n2 == 0:
#         return
#     return n1 / n2
# divide = divisao(8,-2)
#
# if divide:
#     print(divide)
# else:
#     print('Conta inválida.')

def soma(n1, n2, n3):
    return n1 + n2 + n3

print(soma(1, 2, 3))

def fizzbuzz(n1):
    if not n1 % 15:
        return 'fizzbuzz'
    elif not n1 % 5:
        return 'buzz'
    elif not n1 % 3:
        return 'fizz'
    else:
        return n1
from random import randint
num = ''
while num != 0:
    num = randint(0,46)
    print(fizzbuzz(int(num)),num)