usuario = input("Digite seu usuario: ")
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres,  type(qtd_caracteres))
if qtd_caracteres < 6:
    print("Precisa de pelo menos 6 caracteres")
else:
    print("voce foi cadastrado")