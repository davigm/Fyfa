# import os
import random

def inicial():
    # os.system('clear') or None
    tam = 70
    print(tam * "*")
    print("|" + (tam - 2) * " " + "|")
    print("|                       Seja bem vindo ao FyFa                       |")
    print("|" + (tam - 2) * " " + "|")
    print("|" + (tam - 2) * " " + "|")
    print("|   Este é um gerador de campeonato para os aficcionados por FIFA!   |")
    print("|" + (tam - 2) * " " + "|")
    print("|" + (tam - 2) * " " + "|")
    print("|        1-Cadastrar jogadores    2-Cadastrar Equipes   3-Sair       |")
    print("|        4-Jogadores Cadastrados  5-Equipes Cadastradas              |")
    print("|        6-Tabela                 7-Gera Partidas                    |")
    print("|        8-Inserir Resultados                                        |")
    print("|" + (tam - 2) * " " + "|")
    print(tam * "*")


def cadastra_player(players):

    sair = True
    while sair:
        players.append(input("Insira o nome do jogador: "))

        sai = input("Deseja sair? [S/N]")

        if sai.upper() == 'S':
            sair = False

    return players


def cadastra_equipe(teams):
    sair = True
    while sair:
        teams.append(input("Insira o nome da Equipe: "))
        sai = input('Deseja sair? [S/N]')
        if sai.upper() == 'S':
            sair = False
    return teams


def exibe_players(players):
    for player in players:
        print(player)

    random.shuffle(players)
    for player in players:
        print(player)


def exibe_equipes(teams):
    for team in teams:
        print(team)


def gera_confrontos(players):
    players_cp = players[:]
#    random.shuffle(players_cp)
    jogos = []
    for i in range(len(players)):
        for j in range(len(players_cp)):
            if i != j:
                print(players[i]+' x '+players_cp[j])
                jogos.append([players[i], players_cp[j]])
#    print(jogos)
    return jogos


def gerenciador_jogos(jogos):
    campeonato = []
    novo_jogo = {}
    tam = range(len(jogos))
    for i in tam:
        novo_jogo['jogo' + str(i+1)] = [jogos[i],[0,0],'vazio',False]
    #print(novo_jogo)
    for key, value in novo_jogo.items():
        print(key.title())
        print(str(value[0][0]) + ' x ' + str(value[0][1]) + '\n')
    return novo_jogo

def inserir_resultados(tabela):
    jogo = input('Qual jogo deseja alterar? ')
    tabela['jogo' + str(jogo)][1][0] = input('Gols do ' + tabela['jogo' + str(jogo)][0][0])
    tabela['jogo' + str(jogo)][1][1] = input('Gols do ' + tabela['jogo' + str(jogo)][0][1])
    print(tabela['jogo'+str(jogo)])
    return tabela

    '''if tabela['jogo' + str(jogo)[1][0]] > tabela['jogo' + str(jogo)[1][1]]:
        tabela['jogo' + str(jogo)[2]] = tabela['jogo' + str(jogo)[0][0]]

    elif tabela['jogo' + str(jogo)[1][0]] < tabela['jogo' + str(jogo)[1][1]]:
        tabela['jogo' + str(jogo)[2]] = tabela['jogo' + str(jogo)[0][1]]

    else:
        tabela['jogo' + str(jogo)[3]] = True

    print(tabela['jogo'+str(jogo)])'''


sair = True
jogadores = ['Jr', 'Isaac', 'Davi', 'Daniel']
equipes = []
jogos = []
tabela = {}

while sair:

    inicial()
    opc = input("Digite uma opção: ")

    if opc == "1":
        jogadores = cadastra_player(jogadores)
    elif opc == "2":
        equipes = cadastra_equipe(equipes)
    elif opc == "4":
        exibe_players(jogadores)
    elif opc == '5':
        exibe_equipes(equipes)
    elif opc == '6':
        jogos = gera_confrontos(jogadores)
#        campeonato = {'jogo' + '1': jogos}
#       print(campeonato)
    elif opc == '7':
        '''campeonato = '''
        tabela = gerenciador_jogos(jogos)
    elif opc == '8':
        tabela = inserir_resultados(tabela)
    elif opc == "3":
        sair = False
