import pygame
from ..Fonts import fonts
from ..Graphics import colors, scenario
from pygame.locals import *

"""""
    
    # Funções desenha: Todas as funções iniciadas por desenha... tem como função
    realizar a criação, ou seja, desenhar na tela uma parte específica do menu.
    Por exmeplo: desenhaIntro, cria Intro do game; desenhaMenu, cria o Menu principal.

    # Funções evento: Todas as funções iniciadas por evento... tem como função
    a movimentação da seta dos menus.
    Por exemplo: Ao apertar a tecla "s", a seta se movimentará para baixo.
    
    OBS: A primeira função é a única que não possui um retorno que movimenta uma seta
    e sim, que é responsável por uma ação somente, sair da Intro ao apertar "Enter".
    
    """""

class Intro:
    def __init__(self):

        # Print dos textos na tela de introdução
        self.gameName = fonts.chikhenButt70.render("Jogo da cobrinha", True, colors.White)
        self.grupo = fonts.comicNeue15.render("Jogo de Gustavo Costa e Miguel Moura", True, colors.White)
        self.pressEnter = fonts.comicNeue25.render("Pressione ENTER para começar", True, colors.White)

    def desenhaIntro(self, screen):
        screen.fill(colors.Black)
        screen.blit(scenario.IntroBackground, (0, 0))
        screen.blit(self.gameName, (300 - self.gameName.get_width() // 2, 200 - self.gameName.get_height() // 2))
        screen.blit(self.pressEnter, (300 - self.pressEnter.get_width() // 2, 300 - self.pressEnter.get_height() // 2))
        screen.blit(self.grupo, (300 - self.grupo.get_width() // 2, 500 - self.grupo.get_height() // 2))

        pygame.display.flip()

    def evento(self):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                return "Fim"

            if evento.type == KEYDOWN and (evento.key == K_KP_ENTER or evento.key == K_RETURN):
                return "MusicaMenu"

        return "Intro"

class MenuPrincipal:
    def __init__(self):

        # Botões do menu principal
        self.btnJogar = fonts.comicNeue25.render("Jogar", True, colors.White)
        self.btnHistoria = fonts.comicNeue25.render("História", True, colors.White)
        self.btnRanking = fonts.comicNeue25.render("Ranking", True, colors.White)
        self.btnCreditos = fonts.comicNeue25.render("Creditos", True, colors.White)
        self.btnSair = fonts.comicNeue25.render("Sair", True, colors.White)

        # Botão de volume
        self.btnVolume = fonts.comicNeue25.render("Volume", True, colors.White)
        pygame.mixer.music.set_volume(1)
        self.volumeAtual = pygame.mixer.music.get_volume()
        self.btnVolumeAtual = fonts.comicNeue25.render("- " + str(int(pygame.mixer.music.get_volume() * 100)) + " +", True, colors.White)

    def desenhaVolume(self):
        self.btnVolumeAtual = fonts.comicNeue25.render("- " + str(int(pygame.mixer.music.get_volume() * 100)) + " +", True, colors.White)

    def desenhaMenu(self, screen, seta):

        screen.fill(colors.Black)
        screen.blit(scenario.MenuBackground, (0, 0))
        screen.blit(self.btnJogar, (300 - self.btnJogar.get_width() // 2, 200 - self.btnJogar.get_height() // 2))
        screen.blit(self.btnHistoria, (300 - self.btnHistoria.get_width() // 2, 250 - self.btnHistoria.get_height() // 2))
        screen.blit(self.btnRanking, (300 - self.btnRanking.get_width() // 2, 300 - self.btnRanking.get_height() // 2))
        screen.blit(self.btnCreditos, (300 - self.btnCreditos.get_width() // 2, 350 - self.btnCreditos.get_height() // 2))
        screen.blit(self.btnSair, (300 - self.btnSair.get_width() // 2, 400 - self.btnSair.get_height() // 2))
        screen.blit(self.btnVolume, (300 - self.btnSair.get_width() // 2, 500 - self.btnSair.get_height() // 2))
        screen.blit(self.btnVolumeAtual, (300 - self.btnSair.get_width() // 2, 550 - self.btnSair.get_height() // 2))
        pygame.draw.polygon(screen, colors.White, seta, 1)

        pygame.display.flip()

    def eventoMenu(self):

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

                elif evento.key == K_KP_PLUS:
                    if self.volumeAtual < 1:
                        self.volumeAtual += 0.1
                    pygame.mixer.music.set_volume(self.volumeAtual)
                    self.desenhaVolume()

                elif evento.key == K_KP_MINUS:
                    if self.volumeAtual > 0:
                        self.volumeAtual -= 0.10
                    pygame.mixer.music.set_volume(self.volumeAtual)
                    self.desenhaVolume()

        return 0

class MenuDificuldade:
    def __init__(self):
        # Botões de dificuldade
        self.btnFacil = fonts.comicNeue25.render("Fácil", True, colors.White)
        self.btnMedio = fonts.comicNeue25.render("Médio", True, colors.White)
        self.btnDificil = fonts.comicNeue25.render("Difícil", True, colors.White)
        self.btnVoltar = fonts.comicNeue25.render("Voltar", True, colors.White)

    def desenhaDificuldade(self, screen, seta):

        pygame.display.flip()

        screen.fill(colors.Black)
        screen.blit(scenario.DificuldadeBackground, (0, 0))
        screen.blit(self.btnFacil, (200 - self.btnFacil.get_width() // 2, 250 - self.btnFacil.get_height() // 2))
        screen.blit(self.btnMedio, (300 - self.btnMedio.get_width() // 2, 250 - self.btnMedio.get_height() // 2))
        screen.blit(self.btnDificil, (400 - self.btnDificil.get_width() // 2, 250 - self.btnDificil.get_height() // 2))
        screen.blit(self.btnVoltar, (300 - self.btnVoltar.get_width() // 2, 500 - self.btnVoltar.get_height() // 2))
        pygame.draw.polygon(screen, colors.White, seta, 1)

    def eventoDificuldade(self, opcao):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                return 20

            elif evento.type == KEYDOWN:
                if evento.key == K_KP_ENTER or evento.key == K_RETURN:
                    return 10

                elif (evento.key == K_LEFT or evento.key == K_a) and opcao != 5:
                    return -1

                elif (evento.key == K_RIGHT or evento.key == K_d) and opcao != 5:
                    return 1

                elif evento.key == K_UP or evento.key == K_w or evento.key == K_DOWN or evento.key == K_s:
                    if opcao == 5:
                        return -10

                    return 4

        return 0

class MenuFases:
    def __init__(self):

        # Botões das fases
        self.btnGarden = fonts.comicNeue25.render("Garden", True, colors.White)
        self.btnSky = fonts.comicNeue25.render("Sky", True, colors.White)
        self.btnHell = fonts.comicNeue25.render("Hell", True, colors.White)
        self.btnBack = fonts.comicNeue25.render("Voltar", True, colors.White)

        self.cenarioAtual = scenario.SelectHeaven

    def desenhaFases(self, screen, seta):
        pygame.display.flip()

        screen.fill(colors.Black)
        screen.blit(self.cenarioAtual, (0, 0))
        screen.blit(self.btnGarden, (200 - self.btnGarden.get_width() // 2, 250 - self.btnGarden.get_height() // 2))
        screen.blit(self.btnSky, (300 - self.btnSky.get_width() // 2, 250 - self.btnSky.get_height() // 2))
        screen.blit(self.btnHell, (400 - self.btnHell.get_width() // 2, 250 - self.btnHell.get_height() // 2))
        screen.blit(self.btnBack, (300 - self.btnBack.get_width() // 2, 500 - self.btnBack.get_height() // 2))
        pygame.draw.polygon(screen, colors.White, seta, 1)

    def eventoFases(self, opcao):

        if opcao == 1:
            self.cenarioAtual = scenario.SelectGarden
        if opcao == 2:
            self.cenarioAtual = scenario.SelectHeaven
        if opcao == 3:
            self.cenarioAtual = scenario.SelectHell

        for evento in pygame.event.get():
            if evento.type == QUIT:
                return 20

            elif evento.type == KEYDOWN:
                if evento.key == K_KP_ENTER or evento.key == K_RETURN:
                    return 10

                elif (evento.key == K_LEFT or evento.key == K_a) and opcao != 5:
                    return -1

                elif (evento.key == K_RIGHT or evento.key == K_d) and opcao != 5:
                    return 1

                elif evento.key == K_UP or evento.key == K_w or evento.key == K_DOWN or evento.key == K_s:
                    if opcao == 5:
                        return -10

                    return 4

        return 0