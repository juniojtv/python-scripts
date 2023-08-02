# texto = ('Valor')
# #        0   1  2  3  4
# lista = ['A','B','C','D','E', 10.5]
# #       -5  -4 -3 -2 -1
# String = 'ABCDE'
#
# print(lista[::-1])
#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l1.extend(l2)
# print(l2)
# # l2.append('b')
# l2.insert(0, 'banana')
# print(l2)
# l2.pop(1)
# # l3 = l1 + l2
# print(l2)

l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l2.insert(0,'Banana')
# del(l2[0])
# print(l2)

# l2 = list(range(0,100,2))
# print(max(l2), min(l2))
# print(l2)

# soma = 0
# for valor in l2:
#     print(valor)
#     soma += valor
# print(f'A soma de todos os valores da lista 2 é {soma}')
#
# l2 = ('String', True, 10, -20.5)
#
# for elem in l2:
#     print('Para {0}, o tipo de {0} é {1}'.format(elem,type(elem)))

secreto = 'perfume'
digitadas = []
while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso nao vale, digite apenas uma letra.')
        continue
    digitadas.append(letra)
    print(digitadas)
    if letra in secreto:
        print(f'UHULLL, a letra "{letra:#^3}" existe na palavra secreta')
    else:
        print(f'AFFFFF, a letra "{letra:*^4}" NAO EXISTE na palavra secreta')
        digitadas.pop()
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario+= '*'
    if secreto_temporario == secreto:
        print(f'Que legal você ganhou! Sua palavra era {secreto}')
        break
    if
    print(f'A sua palavra secreta está assim: {secreto_temporario}')

