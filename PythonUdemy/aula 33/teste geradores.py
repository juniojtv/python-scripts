nome = 'junior vidal'
def gerar(**kwargs):
    iteravel = kwargs['iteravel']
    for i in iteravel:
        yield i

gerador = gerar(iteravel=nome)
print(type(gerador))
for g in gerador:
    print(g)
