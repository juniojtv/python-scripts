log = False
msg = 'OK' if log else 'NOT OK'
# print(msg)

nome = input('Qual o seu nome? ')

print(nome or None or False or 0 or '' or 'Voce nao digitou nada')

a = 0
b = None
c = False
d = 22

variavel = a or b or c or d

print(variavel)