import pygame
from ..Grafico import cores

class InimigoCeu:
    def __init__(self):
        self.inimigos = [
            pygame.Rect(10, 10, 10, 60),
            pygame.Rect(10, 580, 60, 10),
            pygame.Rect(520, 10, 60, 10),
            pygame.Rect(580, 520, 10, 60)
        ]

        self.movimento = 1
        self.movimentoTotal = 0

    def updateInimigos(self):
        self.inimigos[0] = self.inimigos[0].move(0, self.movimento)
        self.inimigos[1] = self.inimigos[1].move(self.movimento, 0)
        self.inimigos[2] = self.inimigos[2].move(-self.movimento, 0)
        self.inimigos[3] = self.inimigos[3].move(0, -self.movimento)

        self.movimentoTotal += abs(self.movimento)

        if self.movimentoTotal >= 520:
            self.movimento *= -1
            self.movimentoTotal = 0

    def desenhaInimigo(self, screen):
        for i in range(len(self.inimigos)):
            pygame.draw.rect(screen, cores.Black, self.inimigos[i])

    def colisao(self, snake):
        for i in range(len(self.inimigos)):
            for j in range(len(snake.getCobrinha())):
                if self.inimigos[i].collidepoint(snake.getCobrinha()[j][0], snake.getCobrinha()[j][1]):
                    return "CaixaDeTexto"

        return "Jogo"

class InimigoInferno:
    def __init__(self):
        self.inimigos = [
            pygame.Rect(0, 0, 10, 600),
            pygame.Rect(10, 0, 580, 10),
            pygame.Rect(10, 590, 580, 10),
            pygame.Rect(590, 0, 10, 600)
        ]

    def desenhaInimigo(self, screen):
        for i in range(len(self.inimigos)):
            pygame.draw.rect(screen, cores.Black, self.inimigos[i])

    def colisao(self, snake):
        for i in range(len(self.inimigos)):
            if self.inimigos[i].collidepoint(snake.getCobrinha()[0][0], snake.getCobrinha()[0][1]):
                return "CaixaDeTexto"

        return "Jogo"