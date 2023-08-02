
#Os objetos no python nada mais são que instancias de classes
# Importando arquivos

from Pessoa import Pessoa

pessoa = Pessoa("Andre",31)
# print(pessoa.nome)
# print(pessoa.idade)

pessoa.exibir()

pessoa.exibir2("Marcio",38)

pessoa1 = Pessoa("Julio",32)

pessoa.nome = 'Matheus'
print(pessoa.nome)