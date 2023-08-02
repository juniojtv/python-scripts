lista_numeros = [1, 2, 3, 3, 2, 1]
def duplicados(lista_num):
    g1 = []
    g2 = set()
    for n in lista_num:
        if n in g1:
            g2.add(n)
        g1.append(n)
    return g2
print('Os números:', list(duplicados(lista_numeros)), 'são duplicados')




