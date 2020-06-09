import pygame
from src.lib import DBConfig
from src.Fonts import fonts
from src.Graphics import colors, scenario
from pygame.locals import *

pygame.init()


class CaixaDeTexto():
    def __init__(self):
        self.text = ""
        self.seuScore = fonts.comicNeue40.render("Sua potuação foi: ", True, colors.Black)
        self.pressEnter = fonts.comicNeue40.render("Pressione ENTER para salvar", True, colors.Black)
        self.image = fonts.comicNeue40.render("Qual o seu nickname?", True, colors.Black)
        self.rect = self.image.get_rect()
        self.validChars = "1234567890-=qwertyuiop[]\\asdfghjkl;zxcvbnm,./"
        self.shiftChars = '!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?'
        self.shiftDown = False

    # Coleta dos dados do jogador
    def resetBox(self):
        self.text = ""
        self.image = fonts.comicNeue40.render("Qual o seu nickname?", True, colors.Black)

    # Criação de uma caracter com letra maiuscula
    def adicionarChar(self, char):
        if char in self.validChars and not self.shiftDown:
            self.text += char
            self.update()
        elif char in self.validChars and self.shiftDown:
            self.text += self.shiftChars[self.validChars.index(char)]
            self.update()

    def update(self):
        old_rect_pos = self.rect.center
        self.image = fonts.comicNeue40.render(self.text, True, colors.Black)
        self.rect = self.image.get_rect()
        self.rect.center = old_rect_pos

    # Atualizações de display nos cenários e mudança do antigo para o novo Score
    def desenhaTexto(self, score, screen):
        screen.fill(colors.White)
        screen.blit(scenario.TextBackground, (0, 0))
        screen.blit(self.image, (300 - self.image.get_width() // 2, 250 - self.image.get_height() // 2))
        self.scoreAtual = fonts.comicNeue40.render(str(score), True, colors.Black)
        screen.blit(self.scoreAtual, (400, 100))
        screen.blit(self.pressEnter, (50, 150))
        screen.blit(self.seuScore, (100, 100))
        pygame.display.flip()

    def evento(self, score, cenarioAtual, dificuldade):

        if pygame.key.get_mods() & pygame.KMOD_LSHIFT or pygame.key.get_mods() & pygame.KMOD_RSHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS:
            self.shiftDown = True
        else:
            self.shiftDown = False

        for evento in pygame.event.get():
            if evento.type == QUIT:
                return "Fim"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                    self.update()
                if len(self.text) < 15:
                    if evento.key == 93 or evento.key == 91:
                        self.adicionarChar(pygame.key.name(evento.key))
                    else:
                        self.adicionarChar(pygame.key.name(evento.key).replace('[', '').replace(']', ''))
                    if evento.key == pygame.K_SPACE:
                        self.text += " "
                        self.update()
                if (evento.key == K_KP_ENTER or evento.key == K_RETURN) and len(self.text) > 0:

                    db = DBConfig.DBConfig()

                    if cenarioAtual == scenario.BackgroundGrass and dificuldade == 15:
                        db.insert('Jardim_Facil', self.text, score)
                    elif cenarioAtual == scenario.BackgroundGrass and dificuldade == 25:
                        db.insert('Jardim_Medio', self.text, score)
                    elif cenarioAtual == scenario.BackgroundGrass and dificuldade == 40:
                        db.insert('Jardim_Dificil', self.text, score)
                    elif cenarioAtual == scenario.BackgroundHeaven and dificuldade == 15:
                        db.insert('Ceu_Facil', self.text, score)
                    elif cenarioAtual == scenario.BackgroundHeaven and dificuldade == 25:
                        db.insert('Ceu_Medio', self.text, score)
                    elif cenarioAtual == scenario.BackgroundHeaven and dificuldade == 40:
                        db.insert('Ceu_Dificil', self.text, score)
                    elif cenarioAtual == scenario.BackgroundHell and dificuldade == 15:
                        db.insert('Inferno_Facil', self.text, score)
                    elif cenarioAtual == scenario.BackgroundHell and dificuldade == 25:
                        db.insert('Inferno_Medio', self.text, score)
                    elif cenarioAtual == scenario.BackgroundHell and dificuldade == 40:
                        db.insert('Inferno_Dificil', self.text, score)

                    db.encerrarConexao()

                    return "MusicaMenu"

        return "CaixaDeTexto"