#As bibliotecas random e time são importadas para gerar números aleatórios e introduzir pausas no jogo
import random
import time

#Essas linhas exibem uma mensagem de boas-vindas e as regras do jogo
largura = 60
enchimento = '━'
print()
print(f' Olá, seja bem vindo ao Batalha Naval  (￣▽￣)ノ  '.center(largura, enchimento))
print(f'Feito por Leonardo Chung, Guilherme Ferraz, Artur Pandolfo e Lucas Fernandes.'.center(largura))
print(f' Regras '.center(largura, enchimento))
print()
print(f'Nesse jogo você precisa acertar navios inimigos utilizando coordenadas correspondentes no tabuleiro. Você precisa acertar as posições inimigas escolhidas aleatoriamente pelo randomizador de posições. '.center(largura))
print()
print(f'N: posições escolhidas')
print(f'X: acerto dos tiros')
print(f'O: erro dos tiros')
print()
print(f'O usuário que acertar todos os navios primeiro vence. (ᵔ ᵕ ᵔ).'.center(largura))
print(f' Boa sorte (＾_＾）'.center(largura, enchimento))
print()
time.sleep(1)
#Essas variáveis representam o número de colunas e linhas do tabuleiro do jogo
colunas = 10
linhas = 5

#Essa função tabuleiro cria uma matriz representando o tabuleiro do jogo, preenchida com o caractere "-"
def tabuleiro(linhas, colunas):
    tabuleiro = []
    for _ in range(linhas):
        linha = ['-'] * colunas
        tabuleiro.append(linha)
    return tabuleiro

#Essa função mostrar_tabuleiro exibe o tabuleiro na saída do console
def mostrar_tabuleiro(tabuleiro):
    print('======BATALHA NAVAL======')
    print('    1 2 3 4 5 6 7 8 9 10')
    for i, linha in enumerate(tabuleiro):
        print(f'{i + 1} | {" ".join(linha)} |')

#Aqui são criadas três matrizes para representar o tabuleiro do jogador, do computador e os acertos do jogador. O tabuleiro do jogador é exibido na tela
meu_tabuleiro = tabuleiro(linhas, colunas)
tabuleiro_pc = tabuleiro(linhas, colunas)
tabuleiro_acertos = tabuleiro(linhas, colunas)
mostrar_tabuleiro(meu_tabuleiro)

#Essa função permite que o jogador posicione seus navios no tabuleiro
def navios_jogador(tabuleiro):
    print("Posicione 5 navios!")
    print()
    for _ in range(5):
        linha = int(input("Escolha uma linha (1-5): ")) - 1
        while linha < 0 or linha >= linhas:
            print('Linha inválida. Digite novamente.')
            linha = int(input("Escolha uma linha (1-5): ")) - 1
        coluna = int(input("Escolha uma coluna (1-10): ")) - 1
        while coluna < 0 or coluna >= colunas:
            print('Coluna inválida. Digite novamente.')
            coluna = int(input("Escolha uma coluna (1-10): ")) - 1
        while tabuleiro[linha][coluna] == 'N':
            print("Nesse lugar já tem um navio. Escolha outra posição.")
            linha = int(input("Escolha uma linha (1-5): ")) - 1
            coluna = int(input("Escolha uma coluna (1-10): ")) - 1
        tabuleiro[linha][coluna] = 'N'
    print()
    print('    1 2 3 4 5 6 7 8 9 10')
    for i, linha in enumerate(tabuleiro):
        print(f'{i + 1} | {" ".join(linha)} |')
    print()

#Essa função posiciona os navios do computador de forma aleatória no tabuleiro
def navios_computador(tabuleiro):
    print("Aguarde o computador posicionar os navios!!")
    for _ in range(5):
        linha = random.randint(0, 4)
        coluna = random.randint(0, 9)
        while tabuleiro[linha][coluna] == 'N':
            linha = random.randint(0, 4)
            coluna = random.randint(0, 9)
        tabuleiro[linha][coluna] = 'N'
    time.sleep(2)
    print("Computador escolheu!!")
    print()

#Essas duas chamadas de função são responsáveis por posicionar os navios do jogador e do computador nos respectivos tabuleiros
navios_jogador(meu_tabuleiro)
navios_computador(tabuleiro_pc)


#Essas variáveis controlam a quantidade de navios restantes para cada jogador e a pontuação de cada um
navios = 5
navios_pc = 5
pontuacao_jogador = 0
pontuacao_pc = 0
time.sleep(1)

print('           SE PREPARE')
print('           VAMOS COMEÇAR O JOGO!!!')
print('           Tente acertar o navio do computador.')
print()
print('         -VOCÊ-')
mostrar_tabuleiro(meu_tabuleiro)
print()
print(f'Navios do jogador: {navios}')
print()
print('         -SEUS TIROS-')
mostrar_tabuleiro(tabuleiro_acertos)
print()
print(f'Navios restantes do computador: {navios_pc}')
print()
time.sleep(1)
print('      -PLACAR-')
print(f'Você:{pontuacao_jogador} PC:{pontuacao_pc}')
print()

#Essa função permite que o jogador escolha uma posição para atirar no tabuleiro do computador
def atirar_jogador():
    global navios_pc
    global pontuacao_jogador

    atirar_linha = int(input("Escolha uma linha para atirar (1-5): ")) - 1
    while atirar_linha < 0 or atirar_linha >= linhas:
        print('Linha inválida. Digite novamente.')
        atirar_linha = int(input("Escolha uma linha para atirar (1-5): ")) - 1

    atirar_coluna = int(input("Escolha uma coluna para atirar (1-10): ")) - 1
    while atirar_coluna < 0 or atirar_coluna >= colunas:
        print('Coluna inválida. Digite novamente.')
        atirar_coluna = int(input("Escolha uma coluna para atirar (1-10): ")) - 1

    if tabuleiro_acertos[atirar_linha][atirar_coluna] == 'X' or tabuleiro_acertos[atirar_linha][atirar_coluna] == 'O':
        print('Você já atacou essa posição. Vez perdida.')
    elif tabuleiro_pc[atirar_linha][atirar_coluna] == 'N':
        navios_pc -= 1
        pontuacao_jogador += 1
        print('VOCÊ ACERTOU!!!!')
        tabuleiro_acertos[atirar_linha][atirar_coluna] = 'X'
    else:
        print('VOCÊ ERROU!!!!')
        tabuleiro_acertos[atirar_linha][atirar_coluna] = 'O'
    print()
    mostrar_tabuleiro(tabuleiro_acertos)

#Essa função faz o computador escolher uma posição para atirar no tabuleiro do jogador
def atirar_computador():
    global navios
    global pontuacao_pc
    linha_computador = random.randint(0, 4)
    coluna_computador = random.randint(0, 9)
    while tabuleiro_acertos[linha_computador][coluna_computador] == 'X' or tabuleiro_acertos[linha_computador][coluna_computador] == 'O':
        linha_computador = random.randint(0, 4)
        coluna_computador = random.randint(0, 9)
    if meu_tabuleiro[linha_computador][coluna_computador] == 'N':
        navios -= 1
        pontuacao_pc += 1
        print('O COMPUTADOR ACERTOU!!!!')
        meu_tabuleiro[linha_computador][coluna_computador] = 'X'
    else:
        print('O COMPUTADOR ERROU!!!!')
        meu_tabuleiro[linha_computador][coluna_computador] = 'O'
    mostrar_tabuleiro(meu_tabuleiro)
    print()

#O jogo é executado em um loop enquanto ainda houver navios para ambos os jogadores
while navios != 0 and navios_pc != 0:
    print('SUA VEZ DE ATIRAR')
    atirar_jogador()
    print()

    print()
    print('VEZ DO COMPUTADOR')
    time.sleep(3)
    atirar_computador()
    print()

    print()
    print('         -VOCÊ-')
    mostrar_tabuleiro(meu_tabuleiro)
    print()
    print(f'Navios do jogador: {navios}')
    print()
    print('         -SEUS TIROS-')
    mostrar_tabuleiro(tabuleiro_acertos)
    print()
    print(f'Navios restantes do computador: {navios_pc}')
    print()
    time.sleep(3)

#Placar
    print('      -PLACAR-')
    print(f'Você:{pontuacao_jogador} PC:{pontuacao_pc}')
    print()

if navios_pc == 0:
    print('Você venceu! Parabéns!!! ＼(＾▽＾)／')
elif navios == 0:
    print('O computador venceu! Tente novamente. (；一_一)')
