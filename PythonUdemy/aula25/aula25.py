lista = ['j', 'g', 't',1, 2, 3, 4, 5, 6, 7]

n1, n2, *outra_lista, n3, n4, n5 = lista

print(n1, n2)

print(outra_lista[0])
print(n3, n4, n5)

x = 10
y = 'Luiz'
x, y = y, x
print(x, y)

x = 10
y = 'Luiz'
z = 'Otavio'
x, y, z = z, x, y
print(x, y, z)