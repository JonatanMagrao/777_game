from os import system
from functions import *


def game(creditos):
    total_creditos = creditos
    while total_creditos > 0:
        limpar_prompt()
        print(f'Vc está com {total_creditos} créditos.')
        ganhou = mensagem_sistema(numeros_repetidos(sortear_numeros(.5)))

        if ganhou == 1:
            total_creditos -= 1
            if continuar() == 'N':
                ganhou
                break
        elif ganhou == 2:
            total_creditos += 1
            ganhou
            if continuar() == 'N':
                break
        else:
            total_creditos += 10
            ganhou
            if continuar() == 'N':
                break

game(10)
limpar_prompt()