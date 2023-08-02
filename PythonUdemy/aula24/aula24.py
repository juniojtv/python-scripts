string = "O Brasil é o país do futebol, o Brasil é penta"
lista_1 = string.split(' ')
lista_2 = string.split(',')
# print(lista_1)
# print(lista_2)
#
# contagem = 0
# palavra = ''
#
# for valor in lista_1:
#     # print(f'A palavra {valor} apareceu {lista.count(valor)}x na frase')
#     qtd_vezes = lista_1.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#     elif qtd_vezes == contagem and not valor in palavra.split(', ')  :
#             palavra = palavra+', '+valor
#
# print(palavra, type(palavra), f'{contagem}x')

string = 'O Brasil é penta.'
listad = string.split(' ')
#
# for indice, valor in enumerate(lista):
#     print(indice)



lista = [[1, 2], [3, 4], [5, 6]]

# for v1,v2 in enumerate(listad):
#     print(listad[v1])
listatop = list(enumerate(listad))
print(listatop[2][1])