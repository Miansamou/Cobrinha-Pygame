import pygame
from ..Fonts import fontes
from ..Grafico import cores, cenario
from pygame.locals import *

class Intro:
    def __init__(self):
        self.gameName = fontes.chikhenButt70.render("Jogo da cobrinha", True, cores.White)
        self.grupo = fontes.comicNeue15.render("Jogo de Gustavo Costa e Miguel Moura", True, cores.White)
        self.pressEnter = fontes.comicNeue25.render("Pressione ENTER para começar", True, cores.White)

    def desenhaIntro(self, screen):
        screen.fill(cores.Black)
        screen.blit(cenario.IntroBackground, (0, 0))
        screen.blit(self.gameName, (300 - self.gameName.get_width() // 2, 200 - self.gameName.get_height() // 2))
        screen.blit(self.pressEnter, (300 - self.pressEnter.get_width() // 2, 300 - self.pressEnter.get_height() // 2))
        screen.blit(self.grupo, (300 - self.grupo.get_width() // 2, 500 - self.grupo.get_height() // 2))

        pygame.display.flip()

    def evento(self):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                return "Fim"

            if evento.type == KEYDOWN and evento.key == K_KP_ENTER:
                return "MusicaMenu"

        return "Intro"

class MenuPrincipal:
    def __init__(self):

        # botoes do menu principal
        self.btnJogar = fontes.comicNeue25.render("Jogar", True, cores.White)
        self.btnRanking = fontes.comicNeue25.render("Ranking", True, cores.White)
        self.btnCreditos = fontes.comicNeue25.render("Creditos", True, cores.White)
        self.btnSair = fontes.comicNeue25.render("Sair", True, cores.White)

        self.btnVolume = fontes.comicNeue25.render("Volume", True, cores.White)
        pygame.mixer.music.set_volume(1)
        self.volumeAtual = pygame.mixer.music.get_volume()
        self.btnVolumeAtual = fontes.comicNeue25.render("- " + str(int(pygame.mixer.music.get_volume() * 100)) + " +", True, cores.White)

    def updateVolume(self):
        self.btnVolumeAtual = fontes.comicNeue25.render("- " + str(int(pygame.mixer.music.get_volume() * 100)) + " +", True, cores.White)

    def desenhaMenu(self, screen, seta):

        pygame.draw.polygon(screen, cores.White, seta, 1)

        pygame.display.flip()

        screen.fill(cores.Black)
        screen.blit(cenario.MenuBackground, (0, 0))
        screen.blit(self.btnJogar, (300 - self.btnJogar.get_width() // 2, 200 - self.btnJogar.get_height() // 2))
        screen.blit(self.btnRanking, (300 - self.btnRanking.get_width() // 2, 250 - self.btnRanking.get_height() // 2))
        screen.blit(self.btnCreditos, (300 - self.btnCreditos.get_width() // 2, 300 - self.btnCreditos.get_height() // 2))
        screen.blit(self.btnSair, (300 - self.btnSair.get_width() // 2, 350 - self.btnSair.get_height() // 2))
        screen.blit(self.btnVolume, (300 - self.btnSair.get_width() // 2, 500 - self.btnSair.get_height() // 2))
        screen.blit(self.btnVolumeAtual, (300 - self.btnSair.get_width() // 2, 550 - self.btnSair.get_height() // 2))
        pygame.draw.polygon(screen, cores.White, seta, 1)

    def eventoMenu(self):

        for evento in pygame.event.get():
            if evento.type == QUIT:
                return 20

            elif evento.type == KEYDOWN:
                if evento.key == K_KP_ENTER:
                    return 10

                elif evento.key == K_UP:
                    return -1

                elif evento.key == K_DOWN:
                    return 1

                elif evento.key == K_KP_PLUS:
                    if self.volumeAtual < 1:
                        self.volumeAtual += 0.1
                    pygame.mixer.music.set_volume(self.volumeAtual)
                    self.updateVolume()

                elif evento.key == K_KP_MINUS:
                    if self.volumeAtual > 0:
                        self.volumeAtual -= 0.10
                    pygame.mixer.music.set_volume(self.volumeAtual)
                    self.updateVolume()

        pygame.display.flip()

        return 0

class MenuDificuldade:
    def __init__(self):
        # botoes da dificuldade
        self.btnFacil = fontes.comicNeue25.render("Fácil", True, cores.White)
        self.btnMedio = fontes.comicNeue25.render("Médio", True, cores.White)
        self.btnDificil = fontes.comicNeue25.render("Difícil", True, cores.White)
        self.btnVoltar = fontes.comicNeue25.render("Voltar", True, cores.White)

    def selecionarDificuldade(self, screen, seta):

        pygame.display.flip()

        screen.fill(cores.Black)
        screen.blit(cenario.DificuldadeBackground, (0, 0))
        screen.blit(self.btnFacil, (200 - self.btnFacil.get_width() // 2, 250 - self.btnFacil.get_height() // 2))
        screen.blit(self.btnMedio, (300 - self.btnMedio.get_width() // 2, 250 - self.btnMedio.get_height() // 2))
        screen.blit(self.btnDificil, (400 - self.btnDificil.get_width() // 2, 250 - self.btnDificil.get_height() // 2))
        screen.blit(self.btnVoltar, (300 - self.btnVoltar.get_width() // 2, 500 - self.btnVoltar.get_height() // 2))
        pygame.draw.polygon(screen, cores.White, seta, 1)

    def eventoDificuldade(self, opcao):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                return 20

            elif evento.type == KEYDOWN:
                if evento.key == K_KP_ENTER:
                    return 10

                elif evento.key == K_LEFT and opcao != 5:
                    return -1

                elif evento.key == K_RIGHT and opcao != 5:
                    return 1

                elif evento.key == K_UP or evento.key == K_DOWN:
                    if opcao == 5:
                        return -10

                    return 4

        return 0

class MenuFases:
    def __init__(self):

        #botões das fases
        self.btnGarden = fontes.comicNeue25.render("Garden", True, cores.White)
        self.btnSky = fontes.comicNeue25.render("Sky", True, cores.White)
        self.btnHell = fontes.comicNeue25.render("Hell", True, cores.White)
        self.btnBack = fontes.comicNeue25.render("Voltar", True, cores.White)

        self.cenarioAtual = cenario.SelectHeaven

    def desenhaFases(self, screen, seta):
        pygame.display.flip()

        screen.fill(cores.Black)
        screen.blit(self.cenarioAtual, (0, 0))
        screen.blit(self.btnGarden, (200 - self.btnGarden.get_width() // 2, 250 - self.btnGarden.get_height() // 2))
        screen.blit(self.btnSky, (300 - self.btnSky.get_width() // 2, 250 - self.btnSky.get_height() // 2))
        screen.blit(self.btnHell, (400 - self.btnHell.get_width() // 2, 250 - self.btnHell.get_height() // 2))
        screen.blit(self.btnBack, (300 - self.btnBack.get_width() // 2, 500 - self.btnBack.get_height() // 2))
        pygame.draw.polygon(screen, cores.White, seta, 1)

    def eventoFases(self, opcao):

        if opcao == 1:
            self.cenarioAtual = cenario.SelectGarden
        if opcao == 2:
            self.cenarioAtual = cenario.SelectHeaven
        if opcao == 3:
            self.cenarioAtual = cenario.SelectHell

        for evento in pygame.event.get():
            if evento.type == QUIT:
                return 20

            elif evento.type == KEYDOWN:
                if evento.key == K_KP_ENTER:
                    return 10

                elif evento.key == K_LEFT and opcao != 5:
                    return -1

                elif evento.key == K_RIGHT and opcao != 5:
                    return 1

                elif evento.key == K_UP or evento.key == K_DOWN:
                    if opcao == 5:
                        return -10

                    return 4

        return 0