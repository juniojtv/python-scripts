texto = 'Python'

# for n, letra in enumerate(texto):
#     print(n, letra)

# for n in range(0, 9, 1):
#     print(n)
# print('##################')
# for n in range(100):
#     if n % 8 == 0:
#         print(n)

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra
print(nova_string)