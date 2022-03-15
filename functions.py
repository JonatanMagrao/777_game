from os import system
from sys import platform

def limpar_prompt():
    #limpar o terminal para não ficar acumulando um monte de jogadas, deixa mais organizado
    if platform == "win32":
        return system("cls")
    else:
        return system("clear")

def mensagem_sistema(numeros_acertados):
    '''
    mensagem enviada para o jogador após a jogada conforme a quantidade de números acertados
    param : numeros_acertados -> os numeros randomicos pelo sistema
    return: sim, true ou false
    '''
    if numeros_acertados == 3:
        print(f'{"Parabéns, você ganhou 20 pontos!":*^15}\n')
    elif numeros_acertados == 2: 
        print(f'{"Na trave! Você ganhou 1 ponto.":_^15}\n')
    else:
        print(f'{"Não foi dessa vez.":.^15}\n')
    return numeros_acertados
    
def sortear_numeros(segundos_espera):
    #param [segundos_espera] -> segundos de esperao
    from random import randint
    from time import sleep

    numeros_sorteados = []

    for _ in range(0,3):
        numeros_randomicos_sorteio = randint(1,6)
        numeros_sorteados.append(numeros_randomicos_sorteio)
    print(f'\n   {"  777  ":=^15}')
    print(f'   [ {numeros_sorteados[0]} ][ {numeros_sorteados[1]} ][ {numeros_sorteados[2]} ]\n')
    sleep(segundos_espera)
    return numeros_sorteados

def continuar():
    #resposta se o jogador deseja continuar jogando após a última jogada
    opcao_continuar = input('Deseja continuar: [S/N] ').strip().upper()
    return opcao_continuar

def numeros_repetidos(numeros_sorteados):
    #retorna a quantidade de vezes que um numero se repetiu
    #param:numeros_sorteados -> números gerados automaticamente
    #retorn: sim

    lista_numeros_sorteados = []
    for numero in range(0,len(numeros_sorteados)):
        lista_numeros_sorteados.append(numeros_sorteados.count(numeros_sorteados[numero]))
    return max(lista_numeros_sorteados)
