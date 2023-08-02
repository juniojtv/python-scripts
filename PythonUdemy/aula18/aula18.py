# x = 0
# y = 0
# while x < 6:
#    if x==3:
#       x = x + 1
#       break
#    x += 1
#    print(x)
#    y += 6300
#    print(y)
# print('Acabou')
while True:
   num_1 = input('Digite um número: ')
   num_2 = input('Digite outro número: ')
   operador = input('Digite um operador: ')



   if not num_1.isnumeric() or not num_2.isnumeric():
      print('Voce precisa digitar um numero')
      continue
   if operador == '+':
      print('O resultado é {n}'.format(n=int(num_1)+int(num_2)))
   if operador == '-':
      print('O resultado é {n}'.format(n=int(num_1)-int(num_2)))
   if operador == '*':
      print('O resultado é {n}'.format(n=int(num_1)*int(num_2)))
   if operador == '/':
      print('O resultado é {n}'.format(n=int(num_1)/int(num_2)))

   sair = input('Deseja sair? [s]im ou [n]ao: ')
   if sair == "s":
      print('Acabou.')
      break