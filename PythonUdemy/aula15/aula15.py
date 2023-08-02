num = input('Digite um numero inteiro')

if not num.isdigit():
    print('Nao é numero inteiro')
else:
    num = float(num)
    if not num % 2 == 0:
        print(f'{num} é impar')
    else:
        print('{} é par'.format(num))

if num <=11:
    print("bom dia")
elif num<=17:
    print("boa tarde")
else:
    print("boanoite")
