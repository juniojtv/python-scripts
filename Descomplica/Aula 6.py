#Avançando na programação

#tuplas
tupla = (1,2,3,4,5,6,7)
if 18 in tupla:
    print("Existe")
else:
    print("Não existe")

#dicionário
lista = [0,1,2]
#indice de forma oculta na estrutura
dicionario = {"N1":0,"N2":1,"N3":2}
print(dicionario)

#set
a = {1,3,5}
b = {2,4,6}

print(set(a.union(b)))
print('')
print('')

#Casos reais com tuplas e conjuntos
lista = []

for a in range(5):
    lista.append(input("Nome: "))

print(lista)

#Processamento
#O processador só faz uma tarefa por vez

a = 1
b = 2
c = 3
d = 4

e = a + b + c + d # Forma mais lenta para usar um processador apenas

e = a + b # dessa forma ele usa mais de 1 processador
f = c + d
g = e + f

