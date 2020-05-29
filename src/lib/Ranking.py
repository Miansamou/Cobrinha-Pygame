import pygame
from ..Fonts import fontes
from ..Grafico import cores, cenario
from src.lib import DBConfig
from pygame.locals import *

class Rankinkg:
    def __init__(self):
        self.Rank = fontes.comicNeue40.render("< Ranking Jardim >", True, cores.White)
        self.Facil = fontes.comicNeue25.render("Fácil", True, cores.White)
        self.Medio = fontes.comicNeue25.render("Médio", True, cores.White)
        self.Difil = fontes.comicNeue25.render("Difícil", True, cores.White)
        self.Voltar = fontes.comicNeue25.render("Pressione ENTER para voltar ao Menu", True, cores.White)

        self.fase = 'Jardim_'
        self.cenarioAtual = cenario.SelectGarden

    def setRank(self, opcao):
        if opcao == 1:
            self.Rank = fontes.comicNeue40.render("< Ranking Jardim >", True, cores.White)
            self.fase = 'Jardim_'
            self.cenarioAtual = cenario.SelectGarden
        elif opcao == 2:
            self.Rank = fontes.comicNeue40.render("< Ranking Céu >", True, cores.White)
            self.fase = 'Ceu_'
            self.cenarioAtual = cenario.SelectHeaven
        elif opcao == 3:
            self.Rank = fontes.comicNeue40.render("< Ranking Inferno >", True, cores.White)
            self.fase = 'Inferno_'
            self.cenarioAtual = cenario.SelectHell

    def impressaoBanco(self, screen, db, dificuldade, posX, posY, posFinal):
        db.organizarTabela(self.fase + dificuldade)

        records = db.cursor.fetchall()

        for row in records:
            if posY > posFinal:
                continue

            posY += 30
            self.Pos = fontes.comicNeue15.render(row[0] + " Pontos: " + str(row[1]), True, cores.White)
            screen.blit(self.Pos, (posX - self.Pos.get_width() // 2, posY))

    def desenhaRank(self, screen):
        screen.fill(cores.Black)
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
                if evento.key == K_LEFT:
                    return -1

                elif evento.key == K_RIGHT:
                    return 1

                elif evento.key == K_KP_ENTER:
                    return 10

        return 0