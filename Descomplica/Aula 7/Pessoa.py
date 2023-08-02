#POO Programação Orientada a Objetos.
class Pessoa:
    # Possui metodos e atributos
    # atributos são caracteristicas dos objetos
    # metodos são ações desses objetos, ou seja, funções
    # método = função
    
    nome = "Marcio"
    # encapsulamento usando o underline 2x permite apenas o uso da variavel dentro da classe
    idade = 38

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def exibir(self, ):
        print(self.nome)
    # self = use o valor da propria classe

    def exibir2(self, nome, idade):
        print(nome, idade)
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    # def adicionar(self, tamanho, cor):
    #     pass
    
    # def adicionar(self,voltagem, cor, dimensoes):
    #     pass    
    # Não existe sobreposição de metodos no python


    
