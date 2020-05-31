import pygame, pickle
from src.Fonts import fontes
from src.Grafico import cores
from pygame.locals import *


class Scene:
    def __init__(self):
        try:
            self.currentScene = pickle.load( open("Save/savefile.dat", "rb"))
        except:
            self.currentScene = "Null"

        self.btnNewGame = fontes.comicNeue25.render("Novo Jogo", True, cores.White)
        self.btnLoad = fontes.comicNeue25.render("Carregar", True, cores.White)
        self.btnVoltar = fontes.comicNeue25.render("Voltar", True, cores.White)

    def eventoLoad(self):

        for evento in pygame.event.get():
            if evento.type == QUIT:
                return 20

            elif evento.type == KEYDOWN:
                if evento.key == K_KP_ENTER or evento.key == K_RETURN:
                    return 10

                elif evento.key == K_UP or evento.key == K_w:
                    return -1

                elif evento.key == K_DOWN or evento.key == K_s:
                    return 1

        return 0

    def desenhaCena(self, screen, seta):
        if self.currentScene == "Null" or "Prologo, 1":
            self.btnLoad = fontes.comicNeue25.render("Carregar", True, cores.Gray)
        else:
            self.btnLoad = fontes.comicNeue25.render("Carregar", True, cores.White)

        screen.fill(cores.Black)
        screen.blit(self.btnNewGame, (300 - self.btnNewGame.get_width() // 2, 200 - self.btnNewGame.get_height() // 2))
        screen.blit(self.btnLoad, (300 - self.btnLoad.get_width() // 2, 250 - self.btnLoad.get_height() // 2))
        screen.blit(self.btnVoltar, (300 - self.btnVoltar.get_width() // 2, 300 - self.btnVoltar.get_height() // 2))
        pygame.draw.polygon(screen, cores.White, seta, 1)

        pygame.display.flip()