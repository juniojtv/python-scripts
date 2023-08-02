#Ler arquivos na maquina
conteudo = open('arquivo.txt', "a")
conteudo.write("Uma linha qualquer")
print('Executado')
# R = Read
# W = Write
# X = Execute
# A = Append
# R+
# WB

# Ler arquivos na nuvempython -m pip install numpy

import requests
ler = requests.get("http://wiki.icmc.usp.br/images/9/95/BDI.txt")

print(ler)
with open('arquivo2.txt','wb') as arquivo:
    arquivo.write(ler.content)

# Tratando Erros

a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))

if b == 0:
    print("Não e possivel divisão por 0.")
else:
    c = a/b

print(c)