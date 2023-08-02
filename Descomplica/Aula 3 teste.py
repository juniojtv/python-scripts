nascimento = int(input("Digite seu ano de nascimento: "))
anoatual = int(input("Digite o ano atual: "))
match (anoatual - nascimento):
    case 16:
        print("Tem 16")
        documento = input("Mostre seu documento: ")
    case 18:
        print("É maior")