import pygame, random
from src.Fonts import fontes
from src.Grafico import cores, cenario
from src.lib import Cobrinha, sys, CaixaDeTexto, Ranking, Menu, Creditos
from pygame.locals import *

pygame.init()

#----------- Iniciando variaveis e objetos do jogo ----------------

System = sys.System()

Rank = Ranking.Rankinkg()

intro = Menu.Intro()

menuPrincipal = Menu.MenuPrincipal()

menuDificuldade = Menu.MenuDificuldade()

fases = Menu.MenuFases()

textBox = CaixaDeTexto.CaixaDeTexto()

creditos = Creditos.Creditos()

# Seta do menu
seta = System.seta

# Selecionar opcoes
opcao = 1

#Cenario Jogado
cenarioAtual = cenario.BackgroundHeaven

#cria um valor aleatório e faz uma divisão exata para que posteriormente a maçã fique no mesmo nível da cobra
def on_grid_random():
    x = random.randint(10, 590)
    y = random.randint(10, 590)
    return (x//10 * 10, y//10 * 10)

#cria a função de colição entre duas posições
def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

# Tocar musica inicial
pygame.mixer.music.load("src/Musics/Our-Mountain_v003_Looping.mp3")
pygame.mixer.music.play(-1)

running = "Intro"

while running != "Fim":

    if running == "Intro":
        intro.desenhaIntro(System.screen)
        running = intro.evento()

    elif running == "MusicaMenu":
        running = "IniciandoMenu"
        pygame.mixer.music.load("src/Musics/Canon-In-B.mp3")
        pygame.mixer.music.play(-1)

    elif running == "IniciandoMenu":
        running = "MenuPrincipal"
        seta = [(220, 185), (220, 215), (235, 200)]
        opcao = 1

    elif running == "MenuPrincipal":

        """""
        Opções:
        
        Entre 1 a 10:
            São opções disponiveis dentro da tela do jogo
            
            ex: Quando a seta estiver sobre o botão Jogar, a opção será 1
            
        Entre 11 a 20:
            São as opções da tela do jogo ao pressionar o botão Enter
            
            ex: Quando a seta estiver sobre o botão Jogar e o jogador pressionar Enter, a opção será 11
            
        De 20 em diante:
            São opções selecionadas fora do campo de visão das opções na tela
            
            ex: Ao clicar na opção de fechar a janela do aplicativo
        """""

        menuPrincipal.desenhaMenu(System.screen, seta)
        setSeta = menuPrincipal.eventoMenu()
        opcao += setSeta
        if setSeta == 1:
            for i in range(3):
                seta[i] = System.mudarPrimeiroArrayBimensional(seta[i][0], seta[i][1], 50)

        elif setSeta == -1:
            for i in range(3):
                seta[i] = System.mudarPrimeiroArrayBimensional(seta[i][0], seta[i][1], -50)

        if opcao == 11:
            running = "MenuDificuldade"
            opcao = 2
            seta = [(240, 235), (240, 265), (255, 250)]

        elif opcao == 12:
            running = "Ranking"
            opcao = 1

        elif opcao == 13:
            running = "Creditos"
            creditos.initialTime = pygame.time.get_ticks()

            # iniciando musica dos creditos

            pygame.mixer.music.load("src/Musics/snake-eater.mp3")
            pygame.mixer.music.play(0)

        elif opcao == 14:
            running = "Fim"

        elif opcao > 20:
            running = "Fim"

        # Jogador avançou ou voltou além do permitido, volta para a primeira ou última posição
        elif opcao == 5:
            seta = [(220, 185), (220, 215), (235, 200)]
            opcao = 1

        elif opcao == 0:
            seta = [(220, 335), (220, 365), (235, 350)]
            opcao = 4

    elif running == "MenuDificuldade":

        """""
        As opções seguem quase o mesmo parâmetro da tela anterior, com alguns pequenos detalhes
        
        Quando a opção for negativa ela volta para a posição padrão, no caso como opção sendo igual a 2
        
        Pelo botão de voltar ser em uma posição diferente das demais ela possui o valor correspondente de 5, pois ao jogador
        ir além do permitido pressionando os botões para os lados, ele irá para os numeros 0 e 4, indo para a primeira e última posição
        da parte de cima do menu respectivamente
        """""
        menuDificuldade.selecionarDificuldade(System.screen, seta)
        setSeta = menuDificuldade.eventoDificuldade(opcao)
        opcao += setSeta

        #Indica a movimentação da seta caso o jogador pressione as setas para o lado
        if setSeta == -1:
            for i in range(3):
                seta[i] = System.mudarSegundoArrayBimensional(seta[i][1], seta[i][0], -100)

        elif setSeta == 1:
            for i in range(3):
                seta[i] = System.mudarSegundoArrayBimensional(seta[i][1], seta[i][0], 100)

        if opcao < 0:
            opcao = 2
            seta = [(240, 235), (240, 265), (255, 250)]

        elif opcao == 0:
            seta = [(340, 235), (340, 265), (355, 250)]
            opcao = 3

        elif opcao == 4:
            seta = [(140, 235), (140, 265), (155, 250)]
            opcao = 1

        # Verifica se o jogador pressionou a seta para baixo para ir na direção do botão de voltar

        elif opcao >= 5 and opcao <= 8:
            seta = [(240, 485), (240, 515), (255, 500)]
            opcao = 5

        elif opcao >= 10 and opcao <= 13:
            if opcao == 11:
                System.setDificuldade(15)

            elif opcao == 12:
                System.setDificuldade(25)

            elif opcao == 13:
                System.setDificuldade(40)

            running = "MenuFases"
            opcao = -1

        elif opcao == 15:
            running = "IniciandoMenu"

        elif opcao > 20:
            running = "Fim"

    elif running == "MenuFases":
        fases.desenhaFases(System.screen, seta)
        setSeta = fases.eventoFases(opcao)
        opcao += setSeta
        if setSeta == -1:
            for i in range(3):
                seta[i] = System.mudarSegundoArrayBimensional(seta[i][1], seta[i][0], -100)

        elif setSeta == 1:
            for i in range(3):
                seta[i] = System.mudarSegundoArrayBimensional(seta[i][1], seta[i][0], 100)

        if opcao < 0:
            opcao = 2
            seta = [(240, 235), (240, 265), (255, 250)]

        elif opcao == 0:
            seta = [(340, 235), (340, 265), (355, 250)]
            opcao = 3

        elif opcao == 4:
            seta = [(140, 235), (140, 265), (155, 250)]
            opcao = 1

        elif opcao >= 5 and opcao <= 8:
            seta = [(240, 485), (240, 515), (255, 500)]
            opcao = 5

        if opcao >= 11 and opcao <= 13:
            if opcao == 11:
                System.setCenario("Garden")

            elif opcao == 12:
                System.setCenario("Sky")

            elif opcao == 13:
                System.setCenario("Hell")

            running = "Jogo"

        elif opcao == 15:
            running = "MenuDificuldade"
            opcao = -1

        elif opcao > 20:
            running = "Fim"

        # Inicializar as variaveis antes do jogo começar

        if running == "Jogo":

            # ---------------- Variaveis do jogo ---------------------
            # cria a cobra com três posições
            snake = Cobrinha.Cobrinha(System.getDificuldade(), cores.LightRed)

            if System.getCenario() == "Garden":
                cenarioAtual = cenario.BackgroundGrass
                itemAtual = cenario.MacaSprite
                snake.mudarCor(cores.LightRed)
            elif System.getCenario() == "Sky":
                cenarioAtual = cenario.BackgroundHeaven
                itemAtual = cenario.MacaSprite
                snake.mudarCor(cores.HardBlue)
            elif System.getCenario() == "Hell":
                cenarioAtual = cenario.BackgroundHell
                itemAtual = cenario.MacaSprite
                snake.mudarCor(cores.LightGreen)

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
                running = "Fim"

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
                textBox.resetBox()
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
        System.screen.blit(cenarioAtual, (0, 0))
        System.screen.blit(cenario.Score, (0, 600))
        scoreAtual = fontes.comicNeue90.render(str(score), True, cores.Black)
        System.screen.blit(scoreAtual, (350, 600))
        System.screen.blit(itemAtual, posicao_da_maca)

        for posicao in snake.getCobrinha():
            snake.desenhaCobrinha(System.screen, posicao)

        pygame.display.flip()

    elif running == "CaixaDeTexto":
        running = textBox.evento(score, cenarioAtual, System.getDificuldade())
        textBox.desenhaTexto(score, System.screen)

    elif running == "Ranking":
        Rank.desenhaRank(System.screen)
        opcao += Rank.evento()
        Rank.setRank(opcao)

        if opcao == 0:
            opcao = 3

        if opcao == 4:
            opcao = 1

        elif opcao >= 11 and opcao <= 13:
            running = "IniciandoMenu"

        elif opcao > 20:
            running = "Fim"

    elif running == "Creditos":
        creditos.desenhaCreditos(System.screen)
        running = creditos.evento()

pygame.quit()