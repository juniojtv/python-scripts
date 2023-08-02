string = "0123456789"*5
print(string)
n = 10
# lista = [num for num in string]
# print(lista)
lista = [string[i:i+n] for i in range(0,len(string),n)]
print(lista)
retorno = '.'.join(lista)
print(retorno)
