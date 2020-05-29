import pygame
from ..Fonts import fontes
from ..Grafico import cores, cenario
from pygame.locals import *

class Creditos:
    def __init__(self):

        self.initialTime = 0
        self.timer = 0

        #nomes
        self.Gustavo = fontes.comicNeue15.render("Gustavo Almeida Costa", True, cores.White)
        self.GustavoJesus = fontes.comicNeue15.render("Gustavo ~Jesus~ Costa", True, cores.White)
        self.Miguel = fontes.comicNeue15.render("Miguel Ângelo Santiago Moura", True, cores.White)
        self.Miguelito = fontes.comicNeue15.render("Miguelito ~Anjo~ Moura", True, cores.White)
        self.MiguelitValsa = fontes.comicNeue15.render("Miguelito Pés de Valsa", True, cores.White)
        self.Vagas = fontes.comicNeue15.render("Há vagas", True, cores.White)
        self.stack = fontes.comicNeue15.render("Stack Overflow", True, cores.White)
        self.caelum = fontes.comicNeue15.render("Apostila da Caelum", True, cores.White)
        self.blogs = fontes.comicNeue15.render("Blogs de Programação", True, cores.White)
        self.google = fontes.comicNeue15.render("São Google", True, cores.White)
        self.Familia = fontes.comicNeue15.render("Família", True, cores.White)

        # 0 ~ 60
        self.gameName = fontes.chikhenButt70.render("Jogo da cobrinha", True, cores.White)
        self.pressEnter = fontes.comicNeue15.render("Pressione ENTER para voltar", True, cores.White)
        self.pressEnterBlack = fontes.comicNeue15.render("Pressione ENTER para voltar", True, cores.Black)

        self.faculdade = fontes.comicNeue25.render("Centro Universitário Senac", True, cores.White)
        self.estudio = fontes.comicNeue25.render("ANACONDA 5", True, cores.White)

        self.diretorGeral = fontes.comicNeue15.render("Diretor do Jogo / Designer Líder", True, cores.White)
        self.produtor = fontes.comicNeue15.render("Produtor", True, cores.White)
        self.programadorLider = fontes.comicNeue15.render("Líder de Programação", True, cores.White)
        self.diretorArte = fontes.comicNeue15.render("Diretor de Arte", True, cores.White)
        self.produtorCordenador = fontes.comicNeue15.render("Produtor de Cordenação", True, cores.White)
        self.produtorAssociado = fontes.comicNeue15.render("Produtores Associados", True, cores.White)

        self.fraseGailDeversPt1 = fontes.comicNeue25.render("TODA CONQUISTA", True, cores.White)
        self.fraseGailDeversPt2 = fontes.comicNeue25.render("COMEÇA", True, cores.White)
        self.fraseGailDeversPt3 = fontes.comicNeue25.render("COM A DECISÃO", True, cores.White)
        self.fraseGailDeversPt4 = fontes.comicNeue25.render("DE TENTAR!", True, cores.White)
        self.fraseGailDeversPt5 = fontes.comicNeue15.render("~ Gail Devers", True, cores.White)

        # 60 ~ 120
        self.Programadores = fontes.comicNeue15.render("Programadores", True, cores.White)
        self.designerPersonagem = fontes.comicNeue15.render("Designer de Personagem", True, cores.White)
        self.designerItens = fontes.comicNeue15.render("Designer de Itens", True, cores.White)
        self.designerCenarios = fontes.comicNeue15.render("Designer de Cenários", True, cores.White)
        self.testers = fontes.comicNeue15.render("Testadores", True, cores.White)
        self.soundTrack = fontes.comicNeue15.render("Diretor de áudio", True, cores.White)
        self.roteiro = fontes.comicNeue15.render("Roteirista", True, cores.White)

        self.music1 = fontes.comicNeue15.render("Cannon In B", True, cores.White)
        self.music1Artist = fontes.comicNeue15.render("Pachelbel/Jerry C", True, cores.White)
        self.music2 = fontes.comicNeue15.render("Snake Eater", True, cores.White)
        self.music2Artist = fontes.comicNeue15.render("Cynthia Harrell", True, cores.White)
        self.music3 = fontes.comicNeue15.render("Our Moutain", True, cores.White)
        self.music3Artist = fontes.comicNeue15.render("Sound Image", True, cores.White)

        # 60 ~ 180
        self.patrocinadores = fontes.comicNeue15.render("Patrocinadores", True, cores.White)
        self.tecnologia = fontes.comicNeue25.render("Tecnologias Usadas", True, cores.White)

        self.fabricaDoce = fontes.comicNeue15.render("Doce Fábrica de sonhos", True, cores.White)
        self.instaFabricaDoce = fontes.comicNeue15.render("Insta: @doce_fabricadesonhos", True, cores.White)

        # Essentials
        self.provYGameName = 200
        self.provYn1 = 710
        self.provYn2 = 730
        self.provYn3 = 770
        self.alphaSurface = pygame.Surface((600, 700))
        self.alphaSurface.set_alpha(0)
        self.alpha = 0
        self.deltaTime = 0.3
        self.clock = pygame.time.Clock()

    def desenhaCreditos(self, screen):
        screen.fill(cores.Black)

        self.timer = (pygame.time.get_ticks() - self.initialTime) / 1000
        self.timer = int(self.timer)

        if self.timer % 2 == 0 and self.timer < 10:
            screen.blit(self.pressEnter, (450 - self.pressEnter.get_width() // 2, 690 - self.pressEnter.get_height() // 2))

        if self.timer > 3 and self.timer < 8:
            screen.blit(self.gameName, (300 - self.gameName.get_width() // 2, self.provYGameName - self.gameName.get_height() // 2))

        elif self.timer >= 8:
            screen.blit(self.gameName,(300 - self.gameName.get_width() // 2, self.provYGameName - self.gameName.get_height() // 2))
            self.provYGameName -= self.deltaTime

        if self.timer >= 13 and self.timer < 120:
            screen.blit(self.faculdade, (300 - self.faculdade.get_width() // 2, self.provYn1 - self.faculdade.get_height() // 2))
            screen.blit(self.estudio, (300 - self.estudio.get_width() // 2, (self.provYn1 + 100) - self.estudio.get_height() // 2))

            screen.blit(self.diretorGeral, (50, self.provYn1 + 200))
            screen.blit(self.Gustavo, (350, self.provYn1 + 200))
            screen.blit(self.Miguel, (350, self.provYn1 + 230))

            screen.blit(self.produtor, (50, self.provYn1 + 280))
            screen.blit(self.Gustavo, (350, self.provYn1 + 280))

            screen.blit(self.programadorLider, (50, self.provYn1 + 330))
            screen.blit(self.Miguel, (350, self.provYn1 + 330))

            screen.blit(self.diretorArte, (50, self.provYn1 + 380))
            screen.blit(self.Vagas, (350, self.provYn1 + 380))

            screen.blit(self.produtorCordenador, (50, self.provYn1 + 430))
            screen.blit(self.Miguel, (350, self.provYn1 + 430))

            screen.blit(self.produtorAssociado, (50, self.provYn1 + 480))
            screen.blit(self.stack, (350, self.provYn1 + 480))
            screen.blit(self.caelum, (350, self.provYn1 + 510))
            screen.blit(self.blogs, (350, self.provYn1 + 540))
            screen.blit(self.google, (350, self.provYn1 + 570))

            screen.blit(cenario.jesusKidTaca, (0, self.provYn1 + 610))
            screen.blit(cenario.jesusTaca, (400, self.provYn1 + 610))

            screen.blit(self.fraseGailDeversPt1, (300 - self.fraseGailDeversPt1.get_width() // 2, self.provYn1 + 810))
            screen.blit(self.fraseGailDeversPt2, (300 - self.fraseGailDeversPt2.get_width() // 2, self.provYn1 + 830))
            screen.blit(self.fraseGailDeversPt3, (300 - self.fraseGailDeversPt3.get_width() // 2, self.provYn1 + 860))
            screen.blit(self.fraseGailDeversPt4, (300 - self.fraseGailDeversPt4.get_width() // 2, self.provYn1 + 890))
            screen.blit(self.fraseGailDeversPt5, (300 - self.fraseGailDeversPt4.get_width() // 2, self.provYn1 + 950))

            self.provYn1 -= self.deltaTime

        if self.timer > 75 and self.timer < 170:
            screen.blit(self.Programadores, (50, self.provYn2))
            screen.blit(self.GustavoJesus, (350, self.provYn2))
            screen.blit(self.Miguelito, (350, self.provYn2 + 30))

            screen.blit(self.designerPersonagem, (50, self.provYn2 + 80))
            screen.blit(self.GustavoJesus, (350, self.provYn2 + 80))

            screen.blit(self.designerCenarios, (50, self.provYn2 + 130))
            screen.blit(self.Miguelito, (350, self.provYn2 + 130))

            screen.blit(self.designerItens, (50, self.provYn2 + 180))
            screen.blit(self.GustavoJesus, (350, self.provYn2 + 180))

            screen.blit(self.testers, (50, self.provYn2 + 230))
            screen.blit(self.Familia, (350, self.provYn2 + 230))

            screen.blit(cenario.MiguelitoPesValsa, (300 - cenario.MiguelitoPesValsa.get_width() // 2, self.provYn2 + 280))

            screen.blit(self.soundTrack, (50, self.provYn2 + 720))
            screen.blit(self.MiguelitValsa, (350, self.provYn2 + 720))

            screen.blit(self.music1, (50, self.provYn2 + 770))
            screen.blit(self.music1Artist, (350, self.provYn2 + 770))
            screen.blit(self.music2, (50, self.provYn2 + 800))
            screen.blit(self.music2Artist, (350, self.provYn2 + 800))
            screen.blit(self.music3, (50, self.provYn2 + 830))
            screen.blit(self.music3Artist, (350, self.provYn2 + 830))

            screen.blit(self.roteiro, (50, self.provYn2 + 880))
            screen.blit(self.Gustavo, (350, self.provYn2 + 880))
            screen.blit(self.Miguel, (350, self.provYn2 + 910))

            self.provYn2 -= self.deltaTime

        if self.timer > 127:

            screen.blit(cenario.FabricaSonho, (300 - cenario.FabricaSonho.get_width() // 2, self.provYn3))

            screen.blit(self.patrocinadores, (50, self.provYn3 + 130))
            screen.blit(self.fabricaDoce, (350, self.provYn3 + 130))
            screen.blit(self.instaFabricaDoce, (350, self.provYn3 + 160))

            screen.blit(self.tecnologia, (300 - self.tecnologia.get_width() // 2, self.provYn3 + 210))
            screen.blit(cenario.PythonImg, (50, self.provYn3 + 260))
            screen.blit(cenario.PygameImg, (350, self.provYn3 + 260))
            screen.blit(cenario.Photoshop, (50, self.provYn3 + 400))
            screen.blit(cenario.MysqlImg, (350, self.provYn3 + 400))

            if self.timer > 155:
                self.alpha = min(self.alpha + (self.deltaTime * 2), 255)
                self.alphaSurface.set_alpha(self.alpha)
                screen.blit(self.alphaSurface, (0, 0))

            self.provYn3 -= self.deltaTime

        if self.timer > 161:
            screen.blit(cenario.SnakeBite, (0, 0))

            if self.timer % 2 == 0 and self.timer > 164:
                screen.blit(self.pressEnterBlack, (450 - self.pressEnter.get_width() // 2, 690 - self.pressEnter.get_height() // 2))

        pygame.display.flip()

        self.clock.tick(60)

    def evento(self):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                return "Fim"

            if evento.type == KEYDOWN and evento.key == K_KP_ENTER:
                self.timer = 0
                return "MusicaMenu"

        return "Creditos"