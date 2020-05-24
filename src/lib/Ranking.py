import pygame
from ..Fonts import fontes
from ..Grafico import cores
from src.lib import DBConfig
from pygame.locals import *

class Rankinkg:
    def __init__(self):
        self.Rank = fontes.comicNeue40.render("Ranking Geral De teste", True, cores.White)
        self.Voltar = fontes.comicNeue25.render("Pressione ENTER para voltar ao Menu", True, cores.White)

    def desenhaRank(self, screen):
        screen.fill(cores.Black)
        screen.blit(self.Rank, (300 - self.Rank.get_width() // 2, 100 - self.Rank.get_height() // 2))
        screen.blit(self.Voltar, (300 - self.Voltar.get_width() // 2, 600 - self.Voltar.get_height() // 2))

        db = DBConfig.DBConfig()

        db.organizarTabela('Rank')
        records = db.cursor.fetchall()

        numeroDeLinhas = 125

        for row in records:
            if numeroDeLinhas > 525:
                continue

            numeroDeLinhas += 30
            self.Pos = fontes.comicNeue25.render(row[0] + " Pontos: " + str(row[1]), True, cores.White)
            screen.blit(self.Pos, (300 - self.Pos.get_width() // 2, numeroDeLinhas - self.Pos.get_height() // 2))

        db.encerrarConexao()

        pygame.display.flip()

    def evento(self):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()

            if evento.type == KEYDOWN and evento.key == K_KP_ENTER:
                return "IniciandoMenu"

        return "Ranking"