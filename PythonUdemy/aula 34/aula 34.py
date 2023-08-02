from itertools import zip_longest, count, combinations, permutations, product
contador = count()
lista = [1, 2, 3, 4, 5, 6]
lista2 = [10, 9, 8, 7, 6]
lista3 = list(zip(
    contador,
    lista,
    lista2
))
print(lista3)
lista3 = list(zip_longest(
    lista,
    lista2,
    fillvalue="abc"
))
print(lista3)
for x in product(lista2, repeat = 2):
    print(x)

