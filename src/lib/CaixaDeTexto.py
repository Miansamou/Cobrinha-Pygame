import pygame
from src.lib import DBConfig
from src.Fonts import fontes
from src.Grafico import cores, cenario
from pygame.locals import *

pygame.init()


class CaixaDeTexto():
    def __init__(self):
        self.text = ""
        self.seuScore = fontes.comicNeue40.render("Sua potuação foi: ", True, cores.Black)
        self.pressEnter = fontes.comicNeue40.render("Pressione ENTER para salvar", True, cores.Black)
        self.image = fontes.comicNeue40.render("Qual o seu nickname?", True, cores.Black)
        self.rect = self.image.get_rect()
        self.validChars = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
        self.shiftChars = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
        self.shiftDown = False

    def resetBox(self):
        self.text = ""
        self.image = fontes.comicNeue40.render("Qual o seu nickname?", True, cores.Black)

    def adicionarChar(self, char):
        if char in self.validChars and not self.shiftDown:
            self.text += char
            self.update()
        elif char in self.validChars and self.shiftDown:
            self.text += self.shiftChars[self.validChars.index(char)]
            self.update()

    def update(self):
        old_rect_pos = self.rect.center
        self.image = fontes.comicNeue40.render(self.text, True, cores.Black)
        self.rect = self.image.get_rect()
        self.rect.center = old_rect_pos

    def desenhaTexto(self, score, screen):
        screen.fill(cores.White)
        screen.blit(cenario.TextBackground, (0, 0))
        screen.blit(self.image, (300 - self.image.get_width() // 2, 250 - self.image.get_height() // 2))
        self.scoreAtual = fontes.comicNeue40.render(str(score), True, cores.Black)
        screen.blit(self.scoreAtual, (400, 100))
        screen.blit(self.pressEnter, (50, 150))
        screen.blit(self.seuScore, (100, 100))
        pygame.display.flip()

    def evento(self, score):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                return "Fim"
            if evento.type == pygame.KEYUP:
                if evento.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                    self.shiftDown = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    self.update()
                if len(self.text) < 15:
                    self.adicionarChar(pygame.key.name(evento.key))
                    if evento.key == pygame.K_SPACE:
                        self.text += " "
                        self.update()
                    if evento.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                        self.shiftDown = True
                if evento.key == pygame.K_KP_ENTER and len(self.text) > 0:

                    db = DBConfig.DBConfig()

                    db.insert('Rank', self.text, score)

                    db.encerrarConexao()

                    return "MusicaMenu"

        return "CaixaDeTexto"