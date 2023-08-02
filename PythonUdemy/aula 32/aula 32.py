lista = [
    ('chave','valor'),
    ('chave2','valor2'),
]
print(type(lista[0]))
d1 = {x for x in range(5)}
print(d1,type(d1))
d1 = {f'chave_{x}':x**2 for x in range(5)}
# d1 = dict(lista)
print(d1,type(d1))
