# Sistemas de notas para diretor da escola
lista_alunos = []

while True:
    aluno = input("Digite o nome do aluno: ")
    notas = []
    if aluno not in lista_alunos:
        lista_alunos.append(aluno)
        soma = 0
    for n in range(3):
        nota = int(input(f'Digite a {n+1}º nota do aluno: '))
        notas.append(nota)
    for n in notas:
        soma = soma + n
    media = soma/len(notas)
    if media >= 6:
        print (f'Aluno {aluno} aprovado com média = {media}!')
    else:
        nota_final = int(input('Digite nota de recuperação: '))
        media_final = (media+nota_final)/2
        if media_final >= 6:
            print(f'Aluno {aluno} aprovado com média = {media_final}!')
        else:
            print(f'Aluno {aluno} reprovado com média = {media_final}!')