# 777_game

Este é um projeto de jogo 777, famoso nas máquinas caça níqueis.
O propósito da criação desse jogo foi praticar alguns conceitos e funções do Python que venho estudando ultimamente.

Criando este jogo comecei a entender a importância da documentação
e como acessar esta mesma através do Python (que diga-se de passagem, é um recurso ótimo incluso na própria linguagem, o help()).
Experienciei a necessidade e o motivo que se deve criar módulos antes de sair digitando linhas e linhas de código: isso
facilita o processo de criação! Criar módulos e funções que possam ser integrados ao sistema principal, além de facilitar
a criação do mesmo, nos permite ir testando cada funcionalidade, cada trecho do programa, isso diminui os erros e ajuda
a manter um código mais otimizado, além disso esse processo acabou me lembrando as aulas sobre Scrum e metodologias ágeis,
como os sprints backlogs. Eu poderia criar as histórias de usuário para cada função e/ou módulo desse projeto, dando assim
uma idéia de tempo que seria utilizado para criar cada uma e dando uma noção do tempo para a execução.

É um projeto micro, uma tentativa pessoal de ir levando aos poucos a prática dos aprendizados para um outro patamar. Com os
aprendizados desse micro projeto com certeza vou pensar melhor antes de sair criando um sistema, melhorar minhas técnicas de
metodologias ágeis como o Scrum e Kanban, além da economia de tempo e esforço para cada projeto.

Para jogar, basta inicializar o arquivo game.py no terminal através do comando python game.py no windows ou python3 game.py no mac.
O jogo começa com 10 créditos, sendo que a cada tentativa ele consome um ponto, caso nenhum número tenha se repetido. Caso pelo menos dois números tenham se repetido, é incrementado 1 ponto nos créditos e caso os três números sejam iguais (independente se os três deram 7 ou não) o usuário ganha 10 pontos que serão somados aos créditos que já existem. Ao final, caso tenha zerado os créditos, o jogo é fechado precisando ser inicializado novamente.