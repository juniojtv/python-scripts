#Funcoes
def funcao():
    txt = "Imprimindo funcao"
    return txt
print(funcao())

#Funcoes Exemplos
def soma(a, b):
    return (a+b)

print(soma(1,2))

def parouimpar(a):
    if a%2 == 0:
        return 'Par'
    else:
        return 'Impar'

print(parouimpar(1))

#Uso prático da funcao recursiva

#Funcao fatorial

def Fatorial(n):
    if n == 1:
        return 1
    return n * Fatorial(n-1)

print(Fatorial(5))