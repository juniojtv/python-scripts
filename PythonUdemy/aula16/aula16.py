"""
:d - Inteiros (int)
:f - Numeros de ponto flutuante (Float)
:.(numero)f - Quantidade de casas decimais (Float)
:(Caractere)(> ou < ou ^)(Quantidade)(Tipo - s, d ou f)
"""
# num_1 = 1
# num_2 = 3123
# nome = "otavio miranda"
# divisao = num_1 / num_2
# #  print('{:.4f}'.format(divisao))
# print(f'{num_1:d}')
# print(f'{num_2:1<10}')
# print(f'{nome:#^30}')

nome = 'Junior'
sobrenome = 'Vidal'
nome_formatado = '{0:9^20} {1:0>10} {1:0<20} {1}'.format(nome, sobrenome)
print(nome_formatado)
nome = nome.count("n")
print(nome)
# nome = nome.upper()
# print(nome)
# nome = nome.title()
# print(nome)