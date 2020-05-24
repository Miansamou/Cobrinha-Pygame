import pygame, random
from src.Fonts import fontes
from src.Grafico import cores, cenario
from src.lib import Cobrinha, sys, Intro, CaixaDeTexto, Ranking, Menu, Creditos
from pygame.locals import *

pygame.init()

#----------- Iniciando variaveis e objtos do jogo ----------------

System = sys.System()

intro = Intro.Intro()

Rank = Ranking.Rankinkg()

menu = Menu.Menu()

creditos = Creditos.Creditos()

# Seta do menu
seta = System.seta

# Selecionar opcoes
opcao = 1

#cria um valor aleatório e faz uma divisão exata para que posteriormente a maçã fique no mesmo nível da cobra
def on_grid_random():
    x = random.randint(10, 590)
    y = random.randint(10, 590)
    return (x//10 * 10, y//10 * 10)

#cria a função de colição entre duas posições
def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

# Tocar musica inicial
pygame.mixer.music.load("src/Musics/CattleDrive.mp3")
pygame.mixer.music.play(-1)

running = "Intro"

while running != "Fim":

    if running == "Intro":
        intro.desenhaIntro(System.screen)
        running = intro.evento()

    elif running == "MenuPrincipal":
        menu.desenhaMenu(System.screen, seta)
        setSeta = menu.eventoMenu(opcao)
        opcao += setSeta
        if setSeta == 1:
            for i in range(3):
                seta[i] = System.mudarPrimeiroArrayBimensional(seta[i][0], seta[i][1], 50)

        elif setSeta == -1:
            for i in range(3):
                seta[i] = System.mudarPrimeiroArrayBimensional(seta[i][0], seta[i][1], -50)

        if opcao == 6:
            running = "MenuDificuldade"
            opcao = 2
            seta = [(240, 235), (240, 265), (255, 250)]


        elif opcao == 7:
            running = "Ranking"

        elif opcao == 8:
            running = "Creditos"
            creditos.initialTime = pygame.time.get_ticks()

            #iniciando musica dos creditos

            pygame.mixer.music.load("src/Musics/snake-eater.mp3")
            pygame.mixer.music.play(0)

        elif opcao == 5:
            seta = [(220, 185), (220, 215), (235, 200)]
            opcao = 1

        elif opcao < 1:
            seta = [(220, 335), (220, 365), (235, 350)]
            opcao = 4


    elif running == "MenuDificuldade":
        menu.selecionarDificuldade(System.screen, seta)
        setSeta = menu.eventoDificuldade(opcao)
        opcao += setSeta
        if setSeta == -1:
            for i in range(3):
                seta[i] = System.mudarSegundoArrayBimensional(seta[i][1], seta[i][0], -100)

        elif setSeta == 1:
            for i in range(3):
                seta[i] = System.mudarSegundoArrayBimensional(seta[i][1], seta[i][0], 100)

        if opcao > 10:
            running = "Jogo"

        elif opcao < -1:
            running = "MenuPrincipal"

        elif opcao > 5:
            seta = [(240, 485), (240, 515), (255, 500)]
            opcao = 6

        elif opcao == -1:
            opcao = 2
            seta = [(240, 235), (240, 265), (255, 250)]

        elif opcao > 3:
            seta = [(140, 235), (140, 265), (155, 250)]
            opcao = 1

        elif opcao < 1:
            seta = [(340, 235), (340, 265), (355, 250)]
            opcao = 3

        #Inicializar as variaveis antes do jogo começar

        if running == "Jogo":

            if opcao == 11:
                System.setDificuldade(15)

            elif opcao == 12:
                System.setDificuldade(25)

            elif opcao == 13:
                System.setDificuldade(40)

            # ---------------- Variaveis do jogo ---------------------
            # cria a cobra com três posições
            snake = Cobrinha.Cobrinha(System.getDificuldade(),cores.LightRed)

            # movimentação inicial
            direcao = "direita"

            # utiliza a função para delimitar a posição da maçã
            posicao_da_maca = on_grid_random()

            # pontuação
            score = 0

            mudouMovimento = False

            pygame.mixer.music.stop()

    elif running == "Jogo":
        System.clock.tick(System.getDificuldade())
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()

            if evento.type == KEYDOWN:
                if evento.key == K_UP and direcao != "baixo":
                    direcao = "cima"
                    snake.movimentaCobrinha(direcao)
                    mudouMovimento = True
                if evento.key == K_DOWN and direcao != "cima":
                    direcao = "baixo"
                    snake.movimentaCobrinha(direcao)
                    mudouMovimento = True
                if evento.key == K_LEFT and direcao != "direita":
                    direcao = "esquerda"
                    snake.movimentaCobrinha(direcao)
                    mudouMovimento = True
                if evento.key == K_RIGHT and direcao != "esquerda":
                    direcao = "direita"
                    snake.movimentaCobrinha(direcao)
                    mudouMovimento = True

        # resposável por fazer a cobra se movimentar para todas as direções
        # snake.movimentaCobrinha(direcao)
        if mudouMovimento == False:
            snake.movimentaCobrinha(direcao)
        else:
            mudouMovimento = False

        # responsável pela colisão entre a cobra e a maçã
        if colisao(snake.getCobrinha()[0], posicao_da_maca):
            posicao_da_maca = on_grid_random()
            pygame.mixer.music.load("src/Musics/ColetarFruta.mp3")
            pygame.mixer.music.play(0)
            score += 9

            # Aumentar cobrinha com base na dificuldade

            for i in range(System.getDificuldade() // 10 + 1):
                snake.getCobrinha().append((-250, -250))

        # Cobra colidir com ela mesmo
        for i in range(len(snake.getCobrinha()) - 1):
            if colisao(snake.getCobrinha()[0], snake.getCobrinha()[i + 1]):
                textBox = CaixaDeTexto.CaixaDeTexto()
                textBox.rect.center = [300, 250]
                running = "CaixaDeTexto"

        # Não sair da tela
        if snake.getCobrinha()[0][1] > 590:
            snake.setCobrinha(System.mudarPrimeiroArrayBimensional(snake.getCobrinha()[0][0], snake.getCobrinha()[0][1], -600))
        if snake.getCobrinha()[0][1] < 0:
            snake.setCobrinha(System.mudarPrimeiroArrayBimensional(snake.getCobrinha()[0][0], snake.getCobrinha()[0][1], 600))
        if snake.getCobrinha()[0][0] > 590:
            snake.setCobrinha(System.mudarSegundoArrayBimensional(snake.getCobrinha()[0][1], snake.getCobrinha()[0][0], -600))
        if snake.getCobrinha()[0][0] < 0:
            snake.setCobrinha(System.mudarSegundoArrayBimensional(snake.getCobrinha()[0][1], snake.getCobrinha()[0][0], 600))

        # Atulizações de tela
        System.screen.fill(cores.Black)
        System.screen.blit(cenario.BackgroundGrass, (0, 0))
        System.screen.blit(cenario.Score, (0, 600))
        scoreAtual = fontes.comicNeue90.render(str(score), True, cores.Black)
        System.screen.blit(scoreAtual, (350, 600))
        System.screen.blit(cenario.MacaSprite, posicao_da_maca)

        for posicao in snake.getCobrinha():
            snake.desenhaCobrinha(System.screen, posicao)

        pygame.display.flip()

    elif running == "CaixaDeTexto":
        running = textBox.evento(score)
        textBox.desenhaTexto(score, System.screen)

    elif running == "Ranking":
        Rank.desenhaRank(System.screen)
        running = Rank.evento()

    elif running == "Creditos":
        creditos.desenhaCreditos(System.screen)
        running = creditos.evento()

    elif running == "MusicaMenu":
        running = "IniciandoMenu"
        pygame.mixer.music.load("src/Musics/CattleDrive.mp3")
        pygame.mixer.music.play(-1)

    elif running == "IniciandoMenu":
        running = "MenuPrincipal"
        seta = [(220, 185), (220, 215), (235, 200)]
        opcao = 1