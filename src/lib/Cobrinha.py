import pygame

class Cobrinha:
    def __init__(self, dificuldade, color):
        #Esse contrutor definirá os principais parametros da cobrinha: Corpo, tamanho, cor e velocidade
        self.snake = [(200, 200), (200 + dificuldade, 200), (200 + (dificuldade * 2), 200)]
        self.tamanhoPixel = pygame.Surface((10, 10))
        self.tamanhoPixel.fill(color)
        self.velocidade = 10

    def getCobrinha(self):
        return self.snake

    def setCobrinha(self, array):
        self.snake[0] = array

    def reiniciarEstruturaDaCobrinha(self):
        self.snake = [(200, 200), (200 + dificuldade, 200), (200 + (dificuldade * 2), 200)]

    def mudarCor(self, color):
        self.tamanhoPixel.fill(color)

    def movimentaCobrinha(self, direcao):

        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i] = (self.snake[i - 1][0], self.snake[i - 1][1])

        if direcao == "cima":
            self.snake[0] = (self.snake[0][0], self.snake[0][1] - self.velocidade)
        if direcao == "baixo":
            self.snake[0] = (self.snake[0][0], self.snake[0][1] + self.velocidade)
        if direcao == "direita":
            self.snake[0] = (self.snake[0][0] + self.velocidade, self.snake[0][1])
        if direcao == "esquerda":
            self.snake[0] = (self.snake[0][0] - self.velocidade, self.snake[0][1])

    def desenhaCobrinha(self, screen, posicao):
        screen.blit(self.tamanhoPixel, posicao)