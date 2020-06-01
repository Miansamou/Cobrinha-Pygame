import pygame, pickle
from src.Fonts import fontes
from src.Grafico import cores, cenario
from pygame.locals import *


class Scene:
    def __init__(self):

        self.initialTime = 0
        self.timer = 0
        self.deltaTime = 0.5
        self.clock = pygame.time.Clock()

        self.alphaSurface = pygame.Surface((600, 700))
        self.alphaSurface.set_alpha(0)
        self.alphaZero = 0
        self.alphaMax = 245

        self.espacoEntreLinhas = 0

        try:
            self.currentScene = pickle.load(open("Save/savefile.dat", "rb"))
        except:
            self.currentScene = "Null"

        self.btnNewGame = fontes.comicNeue25.render("Novo Jogo", True, cores.White)
        self.btnLoad = fontes.comicNeue25.render("Carregar", True, cores.White)
        self.btnVoltar = fontes.comicNeue25.render("Voltar", True, cores.White)
        self.btnEnter = fontes.comicNeue15.render("Pressione ENTER para avançar", True, cores.White)
        self.btnEsc = fontes.comicNeue15.render("Pressione ESC para voltar ao menu", True, cores.White)

        # Prologo
        self.estudio = fontes.comicNeue40.render("Anaconda 5 apresenta", True, cores.White)
        self.nomeJogo = fontes.chikhenButt70.render("Jogo da Cobrinha", True, cores.White)
        self.prologo = fontes.comicNeue40.render("Prólogo", True, cores.White)

        self.prologoTextoUm = "Esta é uma história de algum lugar num tempo futuro, no qual\n" \
                              "a  compreensão  sobre  o  mundo  se  tornou  mais  densa, e a\n" \
                              "interação  entre  os  povos  completamente interconectada, a\n" \
                              "ponto  da natureza e o espaço ao redor da sociedade importar\n" \
                              "cada  vez   menos.  Com   isso,  o  mundo   terreno   foi  sendo\n" \
                              "usurpado,  animais  e  plantas foram  deixando  de  existir,  e  a\n" \
                              "humanidade  em nada se  importava, já que naquele momento,\n" \
                              "com  a  potência  tecnológica,  era  possível  redefinir as leis da\n" \
                              "cadeia alimentar da forma que bem entendessem."

        self.prologoParagrafoUm = self.separaLinhas(self.prologoTextoUm)

        self.prologoTextoDois = "Cientistas, biólogos e religiosos não viam aquilo com bons olhos,\n" \
                                "a  ciência  buscou  no  abrigo  divino  a  última esperança para a\n" \
                                "salvação do planeta, e  começaram a  disseminar que mais cedo\n" \
                                "ou  mais  tarde  a  punição  divina   iria  cair  sobre  a  população\n" \
                                "pecadora, caso  aquela  louca aceleração continuasse. Como um\n" \
                                "milagre,  o mundo deu ouvidos a esses avisos, esses três grupos,\n" \
                                "uma vez  tão  contrários,  juntos ganharam força e popularidade,\n" \
                                "e  se  uniram  para  montar um grandioso lugar, que abrigaria as\n" \
                                "principais criaturas vítimas do avanço da humanidade, este lugar\n" \
                                "foi construído e batizado de Jardim do Éden. Nele, cada criatura,\n" \
                                "planta  ou  animal,  recebeu  um  nome  pelos sacerdotes, e isso\n" \
                                "prometia  ser  o  início  de  uma  nova  era,  na  qual  natureza  e\n" \
                                "tecnologia pudessem dialogar entre si."

        self.prologoParagrafoDois = self.separaLinhas(self.prologoTextoDois)

        # Capitulo Um

        self.capituloUm = fontes.comicNeue40.render("Capítulo 1 – As maçãs do Jardim", True, cores.White)

        self.textoCapituloUm = "Numa toca,  suja e  úmida do  Jardim, habitava uma pequena e\n" \
                               "jovem   cobra,   era   uma   python,   uma   das   espécies  mais\n" \
                               "ameaçadas, lhe foi dado o nome de chamada Caillou. Certa vez,\n" \
                               "ela  acabou  confundindo  uma  maçã  do  Jardim  com  uma de\n" \
                               "suas  presas, e a comeu de uma vez, e mesmo sendo carnívora,\n" \
                               "ela  apreciou  a  janta  daquela  tarde, e foi em busca de outras\n" \
                               "maçãs para comer..."

        self.capituloUmParagrafo = self.separaLinhas(self.textoCapituloUm)

        self.objetivoCapituloUm = fontes.comicNeue25.render("Objetivo: Coma 5 maças", True, cores.White)

    def resetScene(self):
        try:
            self.currentScene = pickle.load(open("Save/savefile.dat", "rb"))
        except:
            self.currentScene = "Null"

    def resetAlpha(self):
        self.alphaZero = 0
        self.alphaMax = 255

    def separaLinhas(self, texto):
        texto = texto.split("\n")
        paragrafo = [fontes.calibri14.render(linhas, True, cores.White) for linhas in texto]
        return paragrafo

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
        if self.currentScene == "Null" or self.currentScene == "Prologo" or self.currentScene == "Prologo, 1" or self.currentScene == "Prologo, 2":
            self.btnLoad = fontes.comicNeue25.render("Carregar", True, cores.Gray)
        else:
            self.btnLoad = fontes.comicNeue25.render("Carregar", True, cores.White)

        screen.fill(cores.Black)
        screen.blit(self.btnNewGame, (300 - self.btnNewGame.get_width() // 2, 200 - self.btnNewGame.get_height() // 2))
        screen.blit(self.btnLoad, (300 - self.btnLoad.get_width() // 2, 250 - self.btnLoad.get_height() // 2))
        screen.blit(self.btnVoltar, (300 - self.btnVoltar.get_width() // 2, 300 - self.btnVoltar.get_height() // 2))
        pygame.draw.polygon(screen, cores.White, seta, 1)

        pygame.display.flip()

    def desenhaPrologo(self, screen):
        screen.fill(cores.Black)

        self.timer = (pygame.time.get_ticks() - self.initialTime) / 1000
        self.timer = int(self.timer)

        if self.currentScene == "Prologo":
            if self.timer < 12:
                screen.blit(self.estudio, (300 - self.estudio.get_width() // 2, 350 - self.estudio.get_height() // 2))

                if self.timer < 6:
                    self.alphaMax = max(self.alphaMax - (self.deltaTime * 1.25), 0)
                    self.alphaSurface.set_alpha(self.alphaMax)
                    screen.blit(self.alphaSurface, (0, 0))

                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.load("src/Musics/windEffect.mp3")
                        pygame.mixer.music.play(0)

                else:
                    self.alphaZero = min(self.alphaZero + (self.deltaTime * 1.25), 255)
                    self.alphaSurface.set_alpha(self.alphaZero)
                    screen.blit(self.alphaSurface, (0, 0))

            elif self.timer < 17:
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.load("src/Musics/outonoValsaAlegre.mp3")
                    pygame.mixer.music.play(-1)

                screen.blit(self.nomeJogo,
                            (300 - self.nomeJogo.get_width() // 2, 350 - self.nomeJogo.get_height() // 2))

            elif 18 < self.timer < 21:
                screen.blit(self.prologo, (300 - self.prologo.get_width() // 2, 350 - self.prologo.get_height() // 2))

            elif self.timer > 21:
                self.currentScene = "Prologo, 1"
                self.resetAlpha()
                self.initialTime = pygame.time.get_ticks()

        elif self.currentScene == "Prologo, 1":
            screen.blit(cenario.godTouch, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.prologoParagrafoUm:
                self.espacoEntreLinhas += 30
                screen.blit(linhas, (50, 180 + self.espacoEntreLinhas))

            if self.timer % 2 == 0:
                screen.blit(self.btnEnter,
                            (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                screen.blit(self.btnEsc, (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

            if self.timer < 10:
                self.alphaMax = max(self.alphaMax - (self.deltaTime * 5), 0)
                self.alphaSurface.set_alpha(self.alphaMax)
                screen.blit(self.alphaSurface, (0, 0))

        elif self.currentScene == "Prologo, 2":
            screen.blit(cenario.godTouch, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.prologoParagrafoDois:
                self.espacoEntreLinhas += 30
                screen.blit(linhas, (50, 120 + self.espacoEntreLinhas))

            if self.timer % 2 == 0:
                screen.blit(self.btnEnter,
                            (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                screen.blit(self.btnEsc, (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

        pygame.display.flip()

        self.clock.tick(60)

    def eventoPrologo(self, currentScene):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                return "Fim"

            if self.currentScene == "Prologo, 1" or self.currentScene == "Prologo, 2":
                if evento.type == KEYDOWN:
                    if evento.key == K_KP_ENTER or evento.key == K_RETURN:
                        if currentScene == "Prologo, 1":
                            return "Prologo, 2"
                        else:
                            self.initialTime = pygame.time.get_ticks()
                            self.resetAlpha()
                            pickle.dump("Capitulo 1", open("Save/savefile.dat", "wb"))
                            return "Capitulo 1"

                    if evento.key == K_ESCAPE:
                        return "MusicaMenu"

        return currentScene

    def desenhaCapituloUm(self, screen):
        screen.fill(cores.Black)

        self.timer = (pygame.time.get_ticks() - self.initialTime) / 1000
        self.timer = int(self.timer)

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("src/Musics/outonoValsaAlegre.mp3")
            pygame.mixer.music.play(-1)

        if self.currentScene == "Capitulo 1":
            if 1 < self.timer < 5:
                screen.blit(self.capituloUm,
                            (300 - self.capituloUm.get_width() // 2, 350 - self.capituloUm.get_height() // 2))
            elif self.timer > 5:
                self.currentScene = "Capitulo 1, 1"
                self.initialTime = pygame.time.get_ticks()

        elif self.currentScene == "Capitulo 1, 1" or self.currentScene == "ObjetivoCapituloUm":
            screen.blit(cenario.SelectGarden, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.capituloUmParagrafo:
                self.espacoEntreLinhas += 30
                screen.blit(linhas, (50, 180 + self.espacoEntreLinhas))

            if self.timer % 2 == 0:
                screen.blit(self.btnEnter,
                            (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                screen.blit(self.btnEsc, (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

            if self.timer < 10:
                self.alphaMax = max(self.alphaMax - (self.deltaTime * 5), 0)
                self.alphaSurface.set_alpha(self.alphaMax)
                screen.blit(self.alphaSurface, (0, 0))

            if self.currentScene == "ObjetivoCapituloUm":
                self.alphaZero = min(self.alphaZero + (self.deltaTime * 5), 255)
                self.alphaSurface.set_alpha(self.alphaZero)
                screen.blit(self.alphaSurface, (0, 0))

                if self.alphaZero >= 255:
                    screen.blit(self.objetivoCapituloUm,
                                (300 - self.objetivoCapituloUm.get_width() // 2, 350 - self.objetivoCapituloUm.get_height() // 2))

                    if self.timer % 2 == 0:
                        screen.blit(self.btnEnter,
                                    (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                        screen.blit(self.btnEsc,
                                    (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

        pygame.display.flip()

        self.clock.tick(60)

    def eventoCapituloUm(self, currentScene, Flow, snake):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                return "Fim"

            if self.currentScene == "Capitulo 1, 1" or self.currentScene == "ObjetivoCapituloUm":
                if evento.type == KEYDOWN:
                    if evento.key == K_KP_ENTER or evento.key == K_RETURN:
                        if self.currentScene ==  "Capitulo 1, 1":
                            return "ObjetivoCapituloUm"
                        elif self.alphaZero >= 255:
                            pygame.mixer.music.stop()
                            self.resetAlpha()
                            Flow.resetGame("Garden", snake)
                            return "JogoCapituloUm"

                    if evento.key == K_ESCAPE:
                        return "MusicaMenu"

        return currentScene
