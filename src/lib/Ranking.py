import pygame
from ..Fonts import fonts
from ..Graphics import colors, scenario
from src.lib import DBConfig
from pygame.locals import *

"""""

    # Função setRank: Tem como função recolher as informações passadas como parâmetro
    e executa-las dependendo da opção.
    
    # Função impressaoBanco: Tem como função desenhar e ordenar a pontuação de acordo
    com as anteriores, deixando o Ranking em ordem crescente

    # Função desenha: Tem como função realizar a criação, ou seja, desenhar na tela 
    todas as informações do Ranking para o jogador.

    # Função evento: Tem como função realizar realizar a ação desejada pelo jogador
    dependendo da tecla selecionada, por exemplo: Apertar "D" para ir para a página
    da direita. 

"""""

class Rankinkg:
    def __init__(self):
        self.Rank = fonts.comicNeue40.render("< Ranking Jardim >", True, colors.White)
        self.Facil = fonts.comicNeue25.render("Fácil", True, colors.White)
        self.Medio = fonts.comicNeue25.render("Médio", True, colors.White)
        self.Difil = fonts.comicNeue25.render("Difícil", True, colors.White)
        self.Voltar = fonts.comicNeue25.render("Pressione ENTER para voltar ao Menu", True, colors.White)

        self.fase = 'Jardim_'
        self.cenarioAtual = scenario.SelectGarden

    def setRank(self, opcao):
        if opcao == 1:
            self.Rank = fonts.comicNeue40.render("< Ranking Jardim >", True, colors.White)
            self.fase = 'Jardim_'
            self.cenarioAtual = scenario.SelectGarden
        elif opcao == 2:
            self.Rank = fonts.comicNeue40.render("< Ranking Céu >", True, colors.White)
            self.fase = 'Ceu_'
            self.cenarioAtual = scenario.SelectHeaven
        elif opcao == 3:
            self.Rank = fonts.comicNeue40.render("< Ranking Inferno >", True, colors.White)
            self.fase = 'Inferno_'
            self.cenarioAtual = scenario.SelectHell

    def impressaoBanco(self, screen, db, dificuldade, posX, posY, posFinal):
        db.organizarTabela(self.fase + dificuldade)

        records = db.cursor.fetchall()

        for row in records:
            if posY > posFinal:
                continue

            posY += 30
            self.Pos = fonts.comicNeue15.render(row[0] + " Pontos: " + str(row[1]), True, colors.White)
            screen.blit(self.Pos, (posX - self.Pos.get_width() // 2, posY))

    def desenhaRank(self, screen):
        screen.fill(colors.Black)
        screen.blit(self.cenarioAtual, (0, 0))
        screen.blit(self.Rank, (300 - self.Rank.get_width() // 2, 50 - self.Rank.get_height() // 2))
        screen.blit(self.Voltar, (300 - self.Voltar.get_width() // 2, 600 - self.Voltar.get_height() // 2))
        screen.blit(self.Facil, (150 - self.Facil.get_width() // 2, 100))
        screen.blit(self.Medio, (450 - self.Facil.get_width() // 2, 100))
        screen.blit(self.Difil, (300 - self.Facil.get_width() // 2, 325))

        try:
            db = DBConfig.DBConfig()

            self.impressaoBanco(screen, db, 'Facil', 150, 125, 300)
            self.impressaoBanco(screen, db, 'Medio', 450, 125, 300)
            self.impressaoBanco(screen, db, 'Dificil', 300, 350, 550)

            db.encerrarConexao()

        except:
            print("Não foi possível se conectar com o banco de dados")

        pygame.display.flip()

    def evento(self):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                return 20

            if evento.type == KEYDOWN:
                if evento.key == K_LEFT or evento.key == K_a:
                    return -1

                elif evento.key == K_RIGHT or evento.key == K_d:
                    return 1

                elif evento.key == K_KP_ENTER or evento.key == K_RETURN:
                    return 10

        return 0