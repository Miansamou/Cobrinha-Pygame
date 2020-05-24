import pygame
from ..Fonts import fontes
from ..Grafico import cores
from pygame.locals import *

class Menu:
    def __init__(self):

        # botoes do menu principal
        self.btnJogar = fontes.comicNeue25.render("Jogar", True, cores.White)
        self.btnRanking = fontes.comicNeue25.render("Ranking", True, cores.White)
        self.btnCreditos = fontes.comicNeue25.render("Creditos", True, cores.White)
        self.btnSair = fontes.comicNeue25.render("Sair", True, cores.White)

        # botoes da dificuldade
        self.btnFacil = fontes.comicNeue25.render("Fácil", True, cores.White)
        self.btnMedio = fontes.comicNeue25.render("Médio", True, cores.White)
        self.btnDificil = fontes.comicNeue25.render("Difícil", True, cores.White)
        self.btnVoltar = fontes.comicNeue25.render("Voltar", True, cores.White)

    def desenhaMenu(self, screen, seta):

        pygame.draw.polygon(screen, cores.White, seta, 1)

        pygame.display.flip()

        screen.fill(cores.Black)
        screen.blit(self.btnJogar, (300 - self.btnJogar.get_width() // 2, 200 - self.btnJogar.get_height() // 2))
        screen.blit(self.btnRanking, (300 - self.btnRanking.get_width() // 2, 250 - self.btnRanking.get_height() // 2))
        screen.blit(self.btnCreditos, (300 - self.btnCreditos.get_width() // 2, 300 - self.btnCreditos.get_height() // 2))
        screen.blit(self.btnSair, (300 - self.btnSair.get_width() // 2, 350 - self.btnSair.get_height() // 2))
        pygame.draw.polygon(screen, cores.White, seta, 1)

    def eventoMenu(self, opcao):

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()

            elif evento.type == KEYDOWN and evento.key == K_KP_ENTER:
                if opcao == 4:
                    pygame.quit()

                return 5

            elif evento.type == KEYDOWN:
                if evento.key == K_UP:
                    return -1

                elif evento.key == K_DOWN:
                    return 1

        pygame.display.flip()

        return 0

    def selecionarDificuldade(self, screen, seta):

        pygame.display.flip()

        screen.fill(cores.Black)
        screen.blit(self.btnFacil, (200 - self.btnFacil.get_width() // 2, 250 - self.btnFacil.get_height() // 2))
        screen.blit(self.btnMedio, (300 - self.btnMedio.get_width() // 2, 250 - self.btnMedio.get_height() // 2))
        screen.blit(self.btnDificil, (400 - self.btnDificil.get_width() // 2, 250 - self.btnDificil.get_height() // 2))
        screen.blit(self.btnVoltar, (300 - self.btnVoltar.get_width() // 2, 500 - self.btnVoltar.get_height() // 2))
        pygame.draw.polygon(screen, cores.White, seta, 1)

    def eventoDificuldade(self, opcao):
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