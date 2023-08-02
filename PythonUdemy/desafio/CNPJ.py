import re
import sys

CNPJ = "04.252.011/0001-10"
CNPJ = re.sub('[^0-9]','',CNPJ)
validadores = list(range(6,1,-1))+list(range(9,1,-1))
print(validadores)
print(CNPJ)
soma1 = 0
soma2 = 0

for n,c in enumerate(CNPJ[:12]):
    soma1 += int(c)*validadores[n+1]
resto1 = 11 - (soma1 % 11)

dig1 = resto1 if resto1 <= 9 else 0

if dig1 != int(CNPJ[12]):
    print('CNPJ inválido!!')

for n,c in enumerate(CNPJ[:13]):
    soma2 += int(c)*validadores[n]
resto2 = 11 - (soma2 % 11)

dig2 = resto2 if resto2 <= 9 else 0

if dig2 != int(CNPJ[13]):
    print('CNPJ inválido!!')
else:
    print('CNPJ válido!!')