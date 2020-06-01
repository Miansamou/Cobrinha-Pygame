import pygame
from ..Fonts import fontes
from ..Grafico import cores, cenario
from src.lib import sys, Inimigo
from pygame.locals import *

class gameFlow:
    def __init__(self):
        self.mudouMovimento = False
        self.direcao = "direita"
        self.System = sys.System()
        self.posicao_item = self.System.on_grid_random(10, 590)
        self.cenarioAtual = cenario.BackgroundGrass
        self.itemAtual = cenario.MacaSprite
        self.inimigoInferno = Inimigo.InimigoInferno()
        self.inimigoCeu = Inimigo.InimigoCeu()

    def resetGame(self, sceneSelected, snake):
        self.direcao = "direita"

        self.System.score = 0

        self.mudouMovimento = False

        pygame.mixer.music.stop()

        if sceneSelected == "Garden":
            self.cenarioAtual = cenario.BackgroundGrass
            self.itemAtual = cenario.MacaSprite
            snake.mudarCor(cores.LightRed)


        elif sceneSelected == "Sky":
            self.cenarioAtual = cenario.BackgroundHeaven
            self.itemAtual = cenario.AngelSprite
            snake.mudarCor(cores.HardBlue)


        elif sceneSelected == "Hell":
            self.cenarioAtual = cenario.BackgroundHell
            self.itemAtual = cenario.DemonSprite
            snake.mudarCor(cores.LightGreen)
            self.posicao_item = self.System.on_grid_random(20, 580)

    def eventoJogo(self, snake, currentScene):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                return "Fim"

            if evento.type == KEYDOWN:
                if (evento.key == K_UP or evento.key == K_w) and self.direcao != "baixo":
                    self.direcao = "cima"
                    snake.movimentaCobrinha(self.direcao)
                    self.mudouMovimento = True
                if (evento.key == K_DOWN or evento.key == K_s) and self.direcao != "cima":
                    self.direcao = "baixo"
                    snake.movimentaCobrinha(self.direcao)
                    self.mudouMovimento = True
                if (evento.key == K_LEFT or evento.key == K_a) and self.direcao != "direita":
                    self.direcao = "esquerda"
                    snake.movimentaCobrinha(self.direcao)
                    self.mudouMovimento = True
                if (evento.key == K_RIGHT or evento.key == K_d) and self.direcao != "esquerda":
                    self.direcao = "direita"
                    snake.movimentaCobrinha(self.direcao)
                    self.mudouMovimento = True

        return currentScene

    def updateMoving(self, snake):
        if self.mudouMovimento == False:
            snake.movimentaCobrinha(self.direcao)
        else:
            self.mudouMovimento = False

    def snakeOnScreen(self, snake):
        if snake.getCobrinha()[0][1] > 590:
            snake.setCobrinha(self.System.mudarPrimeiroArrayBimensional(snake.getCobrinha()[0][0], snake.getCobrinha()[0][1], -600))
        if snake.getCobrinha()[0][1] < 0:
            snake.setCobrinha(self.System.mudarPrimeiroArrayBimensional(snake.getCobrinha()[0][0], snake.getCobrinha()[0][1], 600))
        if snake.getCobrinha()[0][0] > 590:
            snake.setCobrinha(self.System.mudarSegundoArrayBimensional(snake.getCobrinha()[0][1], snake.getCobrinha()[0][0], -600))
        if snake.getCobrinha()[0][0] < 0:
            snake.setCobrinha(self.System.mudarSegundoArrayBimensional(snake.getCobrinha()[0][1], snake.getCobrinha()[0][0], 600))

    def colission(self, c1, c2):
        return (c1[0] == c2[0]) and (c1[1] == c2[1])

    def snakePrimalColission(self, snake, currentScreen, number):
        if self.colission(snake.getCobrinha()[0], self.posicao_item):
            if self.cenarioAtual == cenario.BackgroundHell:
                self.posicao_item = self.System.on_grid_random(20, 580)
            else:
                self.posicao_item = self.System.on_grid_random(10, 590)
            pygame.mixer.music.load("src/Musics/ColetarFruta.mp3")
            pygame.mixer.music.play(0)
            self.System.score += number

            # Aumentar cobrinha com base na dificuldade

            for i in range(self.System.getDificuldade() // 10 + 1):
                snake.getCobrinha().append((-250, -250))

        # Cobra colidir com ela mesmo
        for i in range(len(snake.getCobrinha()) - 1):
            if self.colission(snake.getCobrinha()[0], snake.getCobrinha()[i + 1]):
                return "CaixaDeTexto"

        return currentScreen

    def heavenColission(self, screen, currentScreen, snake):
        self.inimigoCeu.updateInimigos()
        self.inimigoCeu.desenhaInimigo(screen)
        if currentScreen == "Jogo":
            currentScreen = self.inimigoCeu.colisao(snake)

        return currentScreen

    def hellColission(self, screen, currentScreen, snake):
        self.inimigoInferno.desenhaInimigo(screen)
        if currentScreen == "Jogo":
            currentScreen = self.inimigoInferno.colisao(snake)

        return currentScreen

    def desenhaJogo(self, screen, snake):
        screen.fill(cores.Black)
        screen.blit(self.cenarioAtual, (0, 0))
        screen.blit(cenario.Score, (0, 600))
        scoreAtual = fontes.comicNeue90.render(str(self.System.score), True, cores.Black)
        screen.blit(scoreAtual, (350, 600))
        screen.blit(self.itemAtual, self.posicao_item)

        for posicao in snake.getCobrinha():
            snake.desenhaCobrinha(screen, posicao)