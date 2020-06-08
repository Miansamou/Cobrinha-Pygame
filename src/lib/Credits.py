import pygame
from ..Fonts import fonts
from ..Graphics import colors, scenario
from pygame.locals import *

class Creditos:
    def __init__(self):

        self.initialTime = 0
        self.timer = 0

        #nomes
        self.Gustavo = fonts.comicNeue15.render("Gustavo Almeida Costa", True, colors.White)
        self.GustavoJesus = fonts.comicNeue15.render("Gustavo ~Jesus~ Costa", True, colors.White)
        self.Miguel = fonts.comicNeue15.render("Miguel Ângelo Santiago Moura", True, colors.White)
        self.Miguelito = fonts.comicNeue15.render("Miguelito ~Anjo~ Moura", True, colors.White)
        self.MiguelitValsa = fonts.comicNeue15.render("Miguelito Pés de Valsa", True, colors.White)
        self.Vagas = fonts.comicNeue15.render("Há vagas", True, colors.White)
        self.stack = fonts.comicNeue15.render("Stack Overflow", True, colors.White)
        self.caelum = fonts.comicNeue15.render("Apostila da Caelum", True, colors.White)
        self.blogs = fonts.comicNeue15.render("Blogs de Programação", True, colors.White)
        self.google = fonts.comicNeue15.render("São Google", True, colors.White)
        self.Familia = fonts.comicNeue15.render("Família", True, colors.White)

        # 0 ~ 60
        self.gameName = fonts.chikhenButt70.render("Jogo da cobrinha", True, colors.White)
        self.pressEnter = fonts.comicNeue15.render("Pressione ENTER para voltar", True, colors.White)
        self.pressEnterBlack = fonts.comicNeue15.render("Pressione ENTER para voltar", True, colors.Black)

        self.faculdade = fonts.comicNeue25.render("Centro Universitário Senac", True, colors.White)
        self.estudio = fonts.comicNeue25.render("ANACONDA 5", True, colors.White)

        self.diretorGeral = fonts.comicNeue15.render("Diretor do Jogo / Designer Líder", True, colors.White)
        self.produtor = fonts.comicNeue15.render("Produtor", True, colors.White)
        self.programadorLider = fonts.comicNeue15.render("Líder de Programação", True, colors.White)
        self.diretorArte = fonts.comicNeue15.render("Diretor de Arte", True, colors.White)
        self.produtorCordenador = fonts.comicNeue15.render("Produtor de Cordenação", True, colors.White)
        self.produtorAssociado = fonts.comicNeue15.render("Produtores Associados", True, colors.White)

        self.fraseGailDeversPt1 = fonts.comicNeue25.render("TODA CONQUISTA", True, colors.White)
        self.fraseGailDeversPt2 = fonts.comicNeue25.render("COMEÇA", True, colors.White)
        self.fraseGailDeversPt3 = fonts.comicNeue25.render("COM A DECISÃO", True, colors.White)
        self.fraseGailDeversPt4 = fonts.comicNeue25.render("DE TENTAR!", True, colors.White)
        self.fraseGailDeversPt5 = fonts.comicNeue15.render("~ Gail Devers", True, colors.White)

        # 60 ~ 120
        self.Programadores = fonts.comicNeue15.render("Programadores", True, colors.White)
        self.designerPersonagem = fonts.comicNeue15.render("Designer de Personagem", True, colors.White)
        self.designerItens = fonts.comicNeue15.render("Designer de Itens", True, colors.White)
        self.designerCenarios = fonts.comicNeue15.render("Designer de Cenários", True, colors.White)
        self.testers = fonts.comicNeue15.render("Testadores", True, colors.White)
        self.soundTrack = fonts.comicNeue15.render("Diretor de áudio", True, colors.White)
        self.roteiro = fonts.comicNeue15.render("Roteirista", True, colors.White)

        self.music1 = fonts.comicNeue15.render("Cannon In B", True, colors.White)
        self.music1Artist = fonts.comicNeue15.render("Pachelbel/Jerry C", True, colors.White)
        self.music2 = fonts.comicNeue15.render("Snake Eater", True, colors.White)
        self.music2Artist = fonts.comicNeue15.render("Cynthia Harrell", True, colors.White)
        self.music3 = fonts.comicNeue15.render("Our Moutain", True, colors.White)
        self.music3Artist = fonts.comicNeue15.render("Sound Image", True, colors.White)

        # 60 ~ 180
        self.patrocinadores = fonts.comicNeue15.render("Patrocinadores", True, colors.White)
        self.tecnologia = fonts.comicNeue25.render("Tecnologias Usadas", True, colors.White)

        self.fabricaDoce = fonts.comicNeue15.render("Doce Fábrica de sonhos", True, colors.White)
        self.instaFabricaDoce = fonts.comicNeue15.render("Insta: @doce_fabricadesonhos", True, colors.White)

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
        screen.fill(colors.Black)

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

            screen.blit(scenario.jesusKidTaca, (0, self.provYn1 + 610))
            screen.blit(scenario.jesusTaca, (400, self.provYn1 + 610))

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

            screen.blit(scenario.MiguelitoPesValsa, (300 - scenario.MiguelitoPesValsa.get_width() // 2, self.provYn2 + 280))

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

            screen.blit(scenario.FabricaSonho, (300 - scenario.FabricaSonho.get_width() // 2, self.provYn3))

            screen.blit(self.patrocinadores, (50, self.provYn3 + 130))
            screen.blit(self.fabricaDoce, (350, self.provYn3 + 130))
            screen.blit(self.instaFabricaDoce, (350, self.provYn3 + 160))

            screen.blit(self.tecnologia, (300 - self.tecnologia.get_width() // 2, self.provYn3 + 210))
            screen.blit(scenario.PythonImg, (50, self.provYn3 + 260))
            screen.blit(scenario.PygameImg, (350, self.provYn3 + 260))
            screen.blit(scenario.Photoshop, (50, self.provYn3 + 400))
            screen.blit(scenario.MysqlImg, (350, self.provYn3 + 400))

            if self.timer > 155:
                self.alpha = min(self.alpha + (self.deltaTime * 2), 255)
                self.alphaSurface.set_alpha(self.alpha)
                screen.blit(self.alphaSurface, (0, 0))

            self.provYn3 -= self.deltaTime

        if self.timer > 161:
            screen.blit(scenario.SnakeBite, (0, 0))

            if self.timer % 2 == 0 and self.timer > 164:
                screen.blit(self.pressEnterBlack, (450 - self.pressEnter.get_width() // 2, 690 - self.pressEnter.get_height() // 2))

        pygame.display.flip()

        self.clock.tick(60)

    def evento(self):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                return "Fim"

            if evento.type == KEYDOWN:
                if evento.key == K_KP_ENTER or evento.key == K_RETURN:
                    self.timer = 0
                    return "MusicaMenu"

        return "Creditos"