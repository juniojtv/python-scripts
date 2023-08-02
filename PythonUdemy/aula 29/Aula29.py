lista = [
    ['P1', 2],
    ['P2', 0],
    ['P3', 3],
]
lambda item: item[1]
lista.sort(key=lambda item: item[1])

print(lista)

# lista = 1,2,3
# lista2 = 4,5,6
# l3 = lista + lista2
# print(l3)
# n1, n2, *oi, nult = l3
# print(n1, n2, oi, nult, sep='$$')