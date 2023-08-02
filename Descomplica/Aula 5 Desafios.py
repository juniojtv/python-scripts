# Desafio 1

def maioridade(idade):
    n = int(idade)
    if n >= 18:
        return "éMaior"
    else:
        return "éMenor"

idade = input("Digite sua idade: ")
print(maioridade(idade))

# Desafio 2

def contagem(n):
    if n >= 10:
        return 10
    print(n)
    return contagem(n+1)
print(contagem(0))

def contagem(n):
    if n <= 0:
        return 0
    print(n)
    return contagem(n-1)
print(contagem(10))