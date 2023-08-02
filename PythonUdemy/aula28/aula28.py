def funcao1(arg):
    arg += 1
    return arg


def funcao2(arg):
    return funcao1(arg)


print(funcao2(3))

# -----------------------
def mestre(funcao,*args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando =mestre(saudacao, 'Luiz', saudacao='Bom dia!')
print(executando)

