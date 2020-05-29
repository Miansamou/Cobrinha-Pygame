import pygame
from ..Grafico import cores

class InimigoCeu:
    def __init__(self):
        self.inimigos = [
            pygame.Rect(0, 0, 10, 600),
            pygame.Rect(0, 0, 10, 600),
            pygame.Rect(0, 0, 10, 600),
            pygame.Rect(0, 0, 10, 600)
        ]

    def desenhaInimigo(self, screen):
        for i in range(len(self.inimigos)):
            pygame.draw.rect(screen, cores.Black, self.inimigos[i])

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