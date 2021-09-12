from os import system

def limpar():
    _ = system('clear')

def ver(t):
    '''
    Verificar se os numero sorteados são os 3 iguais
    param : l -> a lista de numeros sorteados
    return: sim, true ou false
    '''
    resp = t
    if resp == 3:
        print(f'\n\n{"Parabéns, você ganhou!":*^15}\n\n')
    elif resp == 2: 
        print(f'   {"Na trave!":_^15}\n')
    else:
        print(f'   {"Não foi dessa vez.":.^15}\n')
    return resp
    

def sortear(s):
    #param [s] -> speed
    from random import randint
    from time import sleep

    sort = []

    for n in range(0,3):
        num = randint(1,7)
        print(f'{num:+^5}')
        sort.append(num)
        sleep(s)
    return sort

def sortear_(s):
    #param [s] -> speed
    from random import randint
    from time import sleep

    sort = []

    for n in range(0,3):
        num = randint(1,6)
        sort.append(num)
    print(f'\n   {"  777  ":=^15}')
    print(f'   [ {sort[0]} ][ {sort[1]} ][ {sort[2]} ]\n')
    sleep(s)
    return sort

def cont():
    op = input('Deseja continuar: [S/N] ').strip().upper()
    return op

def maior(l):
    #retorna a quantidade de vezes que um numero se repetiu
    #param:l -> lista
    #retorn: sim

    m = []
    for n in range(0,len(l)):
        m.append(l.count(l[n]))
    return max(m)
