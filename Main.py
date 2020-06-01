import pygame
from src.Grafico import cores, cenario
from src.lib import Cobrinha, sys, CaixaDeTexto, Ranking, Menu, Creditos, GameFlow, Scenes

pygame.init()

#----------- Iniciando variaveis e objetos do jogo ----------------

System = sys.System()

Rank = Ranking.Rankinkg()

intro = Menu.Intro()

menuPrincipal = Menu.MenuPrincipal()

scene = Scenes.Scene()

menuDificuldade = Menu.MenuDificuldade()

fases = Menu.MenuFases()

textBox = CaixaDeTexto.CaixaDeTexto()

creditos = Creditos.Creditos()

#Objetos e variaveis do jogo em si
GF = GameFlow.gameFlow()
snake = Cobrinha.Cobrinha(System.getDificuldade(), cores.LightRed)

# Seta do menu
seta = System.seta

# Selecionar opcoes
opcao = 1

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
            running = "Historia"
            seta = [(220, 185), (220, 215), (235, 200)]
            opcao = 1

        elif opcao == 13:
            running = "Ranking"
            opcao = 1

        elif opcao == 14:
            running = "Creditos"
            creditos.initialTime = pygame.time.get_ticks()

            # iniciando musica dos creditos

            pygame.mixer.music.load("src/Musics/snake-eater.mp3")
            pygame.mixer.music.play(0)

        elif opcao == 15:
            running = "Fim"

        elif opcao > 20:
            running = "Fim"

        # Jogador avançou ou voltou além do permitido, volta para a primeira ou última posição
        elif opcao == 6:
            seta = [(220, 185), (220, 215), (235, 200)]
            opcao = 1

        elif opcao == 0:
            seta = [(220, 385), (220, 415), (235, 400)]
            opcao = 5

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
            snake.resetCobrinha(System.dificuldade)

            GF.resetGame(System.getCenario(), snake)

    elif running == "Jogo":

        running = GF.eventoJogo(snake, running)

        GF.updateMoving(snake)

        running = GF.snakePrimalColission(snake, running, 9)

        GF.snakeOnScreen(snake)

        GF.desenhaJogo(System.screen, snake)

        if GF.cenarioAtual == cenario.BackgroundHeaven:
            running = GF.heavenColission(System.screen, running, snake)

        if GF.cenarioAtual == cenario.BackgroundHell:
            running = GF.hellColission(System.screen, running, snake)

        if running == "CaixaDeTexto":
            textBox.resetBox()

        pygame.display.flip()
        System.clock.tick(System.getDificuldade())

    elif running == "CaixaDeTexto":
        running = textBox.evento(GF.System.score, GF.cenarioAtual, System.getDificuldade())
        textBox.desenhaTexto(GF.System.score, System.screen)

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

    elif running == "Historia":
        scene.desenhaCena(System.screen, seta)

        setSeta = scene.eventoLoad()
        opcao += setSeta
        if setSeta == 1:
            for i in range(3):
                seta[i] = System.mudarPrimeiroArrayBimensional(seta[i][0], seta[i][1], 50)

        elif setSeta == -1:
            for i in range(3):
                seta[i] = System.mudarPrimeiroArrayBimensional(seta[i][0], seta[i][1], -50)

        if opcao == 4:
            seta = [(220, 185), (220, 215), (235, 200)]
            opcao = 1

        elif opcao == 0:
            seta = [(220, 285), (220, 315), (235, 300)]
            opcao = 3

        elif opcao == 11:
            scene.currentScene = "Prologo"
            running = "RunningHistoria"
            scene.initialTime = pygame.time.get_ticks()
            pygame.mixer.music.stop()

        elif opcao == 12 and scene.currentScene == "Null":
            opcao = 2

        elif opcao == 12:
            running = "RunningHistoria"
            scene.initialTime = pygame.time.get_ticks()
            pygame.mixer.music.stop()

        elif opcao == 13:
            running = "IniciandoMenu"

        elif opcao > 20:
            running = "Fim"

    elif running == "RunningHistoria":
        if scene.currentScene == "Prologo" or scene.currentScene == "Prologo, 1" or scene.currentScene == "Prologo, 2":
            scene.desenhaPrologo(System.screen)
            scene.currentScene = scene.eventoPrologo(scene.currentScene)

        elif scene.currentScene == "Capitulo 1" or scene.currentScene == "Capitulo 1, 1" or scene.currentScene == "ObjetivoCapituloUm":
            scene.desenhaCapituloUm(System.screen)
            scene.currentScene = scene.eventoCapituloUm(scene.currentScene, GF, snake)

        elif scene.currentScene == "JogoCapituloUm":

            running = GF.eventoJogo(snake, running)

            GF.updateMoving(snake)

            running = GF.snakePrimalColission(snake, running, 1)

            GF.snakeOnScreen(snake)

            GF.desenhaJogo(System.screen, snake)

            if running == "CaixaDeTexto":
                running = "RunningHistoria"
                scene.currentScene = "Capitulo 1, 1"

            if GF.System.score >= 5:
                scene.saveData("Capitulo 2")
                scene.currentScene = "Capitulo 2"
                scene.resetAlpha()
                scene.initialTime = pygame.time.get_ticks()

            pygame.display.flip()
            System.clock.tick(30)

        elif scene.currentScene == "Capitulo 2" or scene.currentScene == "Capitulo 2, 1" or scene.currentScene == "Capitulo 2, 2" or scene.currentScene == "ObjetivoCapituloDois":
            scene.desenhaCapituloDois(System.screen)
            scene.currentScene = scene.eventoCapituloDois(scene.currentScene, GF, snake)

        elif scene.currentScene == "JogoCapituloDois":

            running = GF.eventoJogo(snake, running)

            GF.updateMoving(snake)

            running = GF.snakePrimalColission(snake, running, 1)

            GF.snakeOnScreen(snake)

            GF.desenhaJogo(System.screen, snake)

            if running == "CaixaDeTexto":
                running = "RunningHistoria"
                scene.currentScene = "Capitulo 2, 1"

            if GF.System.score >= 10:
                scene.saveData("Capitulo 3")
                scene.currentScene = "Capitulo 3"
                scene.resetAlpha()
                scene.initialTime = pygame.time.get_ticks()

            pygame.display.flip()
            System.clock.tick(40)

        elif scene.currentScene == "Capitulo 3" or scene.currentScene == "Capitulo 3, 1" or scene.currentScene == "Capitulo 3, 2" or scene.currentScene == "ObjetivoCapituloTres":
            scene.desenhaCapituloTres(System.screen)
            scene.currentScene = scene.eventoCapituloTres(scene.currentScene, GF, snake)

        elif scene.currentScene == "JogoCapituloTres":

            running = GF.eventoJogo(snake, running)

            GF.updateMoving(snake)

            running = GF.snakePrimalColission(snake, running, 1)

            GF.snakeOnScreen(snake)

            GF.desenhaJogo(System.screen, snake)

            if GF.cenarioAtual == cenario.BackgroundHeaven:
                running = GF.heavenColission(System.screen, running, snake)

            if running == "CaixaDeTexto":
                running = "RunningHistoria"
                scene.currentScene = "Capitulo 3, 1"

            if GF.System.score >= 15:
                scene.saveData("Capitulo 4")
                scene.currentScene = "Capitulo 4"
                scene.resetAlpha()
                scene.initialTime = pygame.time.get_ticks()

            pygame.display.flip()
            System.clock.tick(30)

        elif scene.currentScene == "Capitulo 4" or scene.currentScene == "Capitulo 4, 1" or scene.currentScene == "Capitulo 4, 2" or scene.currentScene == "ObjetivoCapituloQuatro":
            scene.desenhaCapituloQuatro(System.screen)
            scene.currentScene = scene.eventoCapituloQuatro(scene.currentScene, GF, snake)

        elif scene.currentScene == "JogoCapituloQuatro":

            running = GF.eventoJogo(snake, running)

            GF.updateMoving(snake)

            running = GF.snakePrimalColission(snake, running, 1)

            GF.snakeOnScreen(snake)

            GF.desenhaJogo(System.screen, snake)

            if GF.cenarioAtual == cenario.BackgroundHeaven:
                running = GF.heavenColission(System.screen, running, snake)

            if running == "CaixaDeTexto":
                running = "RunningHistoria"
                scene.currentScene = "Capitulo 4, 1"

            if GF.System.score >= 20:
                scene.saveData("Capitulo 5")
                scene.currentScene = "Capitulo 5"
                scene.resetAlpha()
                scene.initialTime = pygame.time.get_ticks()

            pygame.display.flip()
            System.clock.tick(40)

        elif scene.currentScene == "Capitulo 5" or scene.currentScene == "Capitulo 5, 1" \
                or scene.currentScene == "Capitulo 5, 2" or scene.currentScene == "Capitulo 5, 3" or scene.currentScene == "ObjetivoCapituloCinco":
            scene.desenhaCapituloCinco(System.screen)
            scene.currentScene = scene.eventoCapituloCinco(scene.currentScene, GF, snake)

        elif scene.currentScene == "JogoCapituloCinco":

            running = GF.eventoJogo(snake, running)

            GF.updateMoving(snake)

            running = GF.snakePrimalColission(snake, running, 1)

            GF.snakeOnScreen(snake)

            GF.desenhaJogo(System.screen, snake)

            if GF.cenarioAtual == cenario.BackgroundHell:
                running = GF.hellColission(System.screen, running, snake)

            if running == "CaixaDeTexto":
                running = "RunningHistoria"
                scene.currentScene = "Capitulo 5, 1"

            if GF.System.score >= 25:
                scene.saveData("Capitulo 6")
                scene.currentScene = "Capitulo 6"
                scene.resetAlpha()
                scene.initialTime = pygame.time.get_ticks()

            pygame.display.flip()
            System.clock.tick(30)

        elif scene.currentScene == "Capitulo 6" or scene.currentScene == "Capitulo 6, 1" \
                or scene.currentScene == "Capitulo 6, 2" or scene.currentScene == "Capitulo 6, 3" or scene.currentScene == "ObjetivoCapituloSeis":
            print("Rodando cap 6")

        if scene.currentScene == "MusicaMenu":
            scene.resetScene()
            running = "MusicaMenu"
        elif scene.currentScene == "Fim":
            scene.resetScene()
            running = "Fim"
pygame.quit()