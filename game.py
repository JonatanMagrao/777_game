from os import system
from functions import *


def game(creditos):
    c = creditos
    while c > 0:
        limpar()
        print(f'Vc está com {c} créditos.')
        ganhou = ver(maior(sortear_(.5)))

        if ganhou == 1:
            c -= 1
            res = cont()
            if res == 'N':
                break
        elif ganhou == 2:
            c += 1
            print('Você ganhou mais 1 crédito!')
            res = cont()
            if res == 'N':
                break
        else:
            c += 10
            print('Você recebeu mais 10 créditos!')
            res = cont()
            if res == 'N':
                break

game(10)
system('clear')