"""
Operadores relacionais
"""
nome = input("Qual seu nome? ")
idade = input("Qual a sua idade? ")
idade_limite = 18
if int(idade)>=idade_limite:
    print(f'{nome} com idade {idade} pode pegar empréstimo')
else:
    print(f'{nome} é de menor pode nao meu fi')
