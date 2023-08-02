class Pessoa:
    def __init__(self,nome):
        self._nome = nome
    def falar(self):
        print(f'{self._nome} está falando.')
    def __

class Cliente(Pessoa):
    pass

p1 = Pessoa('Joao')
p2 = Cliente('Maria')
p1.falar()
p2.falar()