import pygame
from ..Fonts import fontes
from ..Grafico import cores
from pygame.locals import *

class Intro:
    def __init__(self):
        self.gameName = fontes.chikhenButt70.render("Jogo da cobrinha", True, cores.White)
        self.grupo = fontes.comicNeue15.render("Jogo de Gustavo Costa e Miguel Moura", True, cores.White)
        self.pressEnter = fontes.comicNeue25.render("Pressione ENTER para começar", True, cores.White)

    def desenhaIntro(self, screen):
        screen.fill(cores.Black)
        screen.blit(self.gameName, (300 - self.gameName.get_width() // 2, 200 - self.gameName.get_height() // 2))
        screen.blit(self.pressEnter, (300 - self.pressEnter.get_width() // 2, 300 - self.pressEnter.get_height() // 2))
        screen.blit(self.grupo, (300 - self.grupo.get_width() // 2, 500 - self.grupo.get_height() // 2))

        pygame.display.flip()

    def evento(self):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()

            if evento.type == KEYDOWN and evento.key == K_KP_ENTER:
                return "MenuPrincipal"

        return "Intro"