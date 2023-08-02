carrinho = []

carrinho = [(f'Produto {x}',(x+5)*2) for x in range(5)]

soma_total_carrinho = sum((y for x,y in carrinho))
print(soma_total_carrinho)