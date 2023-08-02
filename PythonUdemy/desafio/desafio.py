# num_1 = 0
# num_2 = 10
# for n in range(0, 9):
#     print(num_1, num_2)
#     num_1 += 1
#     num_2 -= 1
#
# for n, p in enumerate(range(10, 1, -1)):
#     print(n, p)

"""
Criando validador de CPF
"""

CPFdig = input("Digite um CPF: ")
CPF = CPFdig.replace('.', '').replace('-', '').replace(' ', '')
calc_dig_1 = 0
calc_dig_2 = 0
sequencia = CPF == str(CPF[0]) * len(CPF)
if not len(CPF) == 11 or not CPF.isnumeric() or sequencia:
    print(f'O valor digitado {CPFdig:"^20} foi digitado incorretamente!')
else:
    print(CPF)
    for n in range(0, 12):
        if n < 9:
            calc_dig_1 += int(CPF[n])*(10-n)
            calc_dig_2 += int(CPF[n])*(11-n)
        elif n < 10:
            calc_dig_2 += int(CPF[n]) * (11 - n)
        dig_1 = 11 - (calc_dig_1 % 11)
        dig_2 = 11 - (calc_dig_2 % 11)
    CPF_novo = CPF[:9]+str(dig_1)+str(dig_2)
    print(CPF, CPF_novo)
    if CPF_novo == CPF:
        print('Seu CPF é válido')
    else:
        print('CPF inválido')






