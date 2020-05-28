import pygame
from ..Fonts import fontes
from ..Grafico import cores
from pygame.locals import *

class Fases:
    def __init__(self):

        #botões das fases
        self.btnGarden = fontes.comicNeue25.render("Garden", True, cores.White)
        self.btnSky = fontes.comicNeue25.render("Sky", True, cores.White)
        self.btnHell = fontes.comicNeue25.render("Hell", True, cores.White)
        self.btnBack = fontes.comicNeue25.render("Voltar", True, cores.White)

    def desenhaFases(self, screen, seta):
        pygame.display.flip()

        screen.fill(cores.Black)
        screen.blit(self.btnGarden, (200 - self.btnGarden.get_width() // 2, 250 - self.btnGarden.get_height() // 2))
        screen.blit(self.btnSky, (300 - self.btnSky.get_width() // 2, 250 - self.btnSky.get_height() // 2))
        screen.blit(self.btnHell, (400 - self.btnHell.get_width() // 2, 250 - self.btnHell.get_height() // 2))
        screen.blit(self.btnBack, (300 - self.btnBack.get_width() // 2, 500 - self.btnBack.get_height() // 2))
        pygame.draw.polygon(screen, cores.White, seta, 1)

    def eventoFases(self, opcao):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()

            elif evento.type == KEYDOWN and evento.key == K_KP_ENTER:
                if opcao == 1:
                    return 10

                elif opcao == 2:
                    return 10

                elif opcao == 3:
                    return 10

                elif opcao == 6:
                    return -8

            elif evento.type == KEYDOWN:
                if evento.key == K_LEFT:
                    return -1

                elif evento.key == K_RIGHT:
                    return 1

                elif evento.key == K_UP or evento.key == K_DOWN:
                    if opcao == 6:
                        return -7

                    return 5

        pygame.display.flip()

        return 0
