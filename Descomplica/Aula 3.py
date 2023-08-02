# Condicionais
# Conceito: Para uma acao ser executada uma condição precisa ser atingida

#IF/ ELSE

idade = int(input("Digite sua idade: "))

if idade > 18:
    print("É maior de idade")
elif idade == 18:
    print("Tem 18 anos")
else:
    print("É menor de idade.")
# é preciso fazer identação para o código funcionar

# Ternários
idade = 18
print("É MAIOR") if idade >= 18 else print("É MENOR")

# Match(Switch case)
a = "Marcio"
match a:
    case "Antonio":
        print("Não é Marcio")
    case "Pedro":
        print("É Pedro e não Marcio")
    case "Marcio":
        sobrenome = input("Digite seu Sobrenome: ")
        print(f"É o Marcio {sobrenome}")