nome = 'Luiz'
idade = 32  # int
altura = 1.23  # float
e_maior = idade > 18
data_1 = True  # bool
peso = 80.5
ano = 2019
nascimento = ano-idade
imc = peso / (altura ** 2)
# print(nome, 'tem', idade, 'anos,', altura, 'metros de altura, e seu imc é:', imc)
# print(f'o {nome} tem {idade} anos')
print('{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')
print('{0} coisa {1}, que coisa {2}'.format("asd", "asdf", "gasdf"))
