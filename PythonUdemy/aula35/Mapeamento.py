from Dados import produtos


def aumenta_preco(p):
    newprod = p.copy()
    newprod['preco'] = newprod['preco']/3
    return newprod

novos_prod = map(lambda p: p['preco']+1,produtos)
print(list(novos_prod))
novos_produtos = map(aumenta_preco, produtos)
print(list(novos_produtos))


produtos_filtrados = filter(lambda p: p['preco']>11,produtos)

print(list(produtos_filtrados))
from functools import reduce

soma_precos_prod = reduce(lambda acumulador, p: acumulador + p['preco'],produtos,0)
print(produtos)
print(soma_precos_prod)

