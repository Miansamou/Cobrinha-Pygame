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

        # Capitulo Dois

        self.capituloDois = fontes.comicNeue40.render("Capítulo 2 – Punição divina", True, cores.White)

        self.textoCapituloDoisParagrafoUm = "De alguma forma, Caillou começou a crescer e a crescer cada\n"\
                                          "vez  mais  toda  vez  que  ele  se  alimentava,  todavia, ele não\n"\
                                          "parecia se sentir saciado, e todo o alimento sequer demorava\n"\
                                          "para  ser  digerido.  Com  fome  Caillou como qualquer animal\n"\
                                          "irracional  foi  atrás  de presas que habitavam o Jardim, presas\n"\
                                          "essas    cada   vez   maiores,   porcos,   lobos,   leões,   búfalos,\n"\
                                          "rinocerontes,  elefantes  e  até  mesmo girafas, até chegar um\n"\
                                          "momento  que  aquele  Jardim  se  tornou muito pequeno com\n"\
                                          "uma   alimentação  escassa   para  ele  e  por  fim,  quebrou  as\n"\
                                          "barreiras do Jardim que a separavam da humanidade."

        self.capituloDoisParagrafoUm = self.separaLinhas(self.textoCapituloDoisParagrafoUm)

        self.textoCapituloDoisParagrafoDois = "Então  ele  começou  a  devastar locais habitados por humanos,\n"\
                                            "estava  gerando  o  caos,   muitos  se  renderam  ao  seu  terror,\n"\
                                            "militares  não  eram  capazes  de  detê-lo,  e  estava  claro  para\n"\
                                            "todos  que  a  loucura  do  avanço   tecnológico  irritou  a   Deus,\n"\
                                            "aquela  certamente era a época do apocalipse, o julgamento de\n"\
                                            "todas as almas, a punição divina."

        self.capituloDoisParagrafoDois = self.separaLinhas(self.textoCapituloDoisParagrafoDois)

        self.objetivoCapituloDois = fontes.comicNeue25.render("Objetivo: Devore 10 pessoas", True, cores.White)

        # Capitulo 3

        self.capituloTres = fontes.comicNeue40.render("Capítulo 3 – Céu, o lugar de todos", True, cores.White)

        self.textoCapituloTresParagrafoUm = "Desesperada,  a  humanidade não  via outra escolha, a não ser\n" \
                                            "utilizar armas nucleares contra Caillou, e assim o fizeram, uma\n" \
                                            "grande  explosão  que  destruiu  um  país  inteiro,  milhares de\n" \
                                            "vidas  foram  sacrificadas  naquele  dia, mas este sacrifício não\n" \
                                            "foi  em  vão,  finalmente  Caillou  parou  de  sentir  fome,  tudo\n" \
                                            "estava  terminado,  a  humanidade  podia  enfim comemorar a\n" \
                                            "morte  de  um  inimigo que quase destruiu a raça humana, eles\n"\
                                            "poderiam  reconstruir  suas  vidas,  dessa vez repensando seus\n"\
                                            "atos e se redimindo perante Deus, e Caillou poderia encontrar\n"\
                                            "paz e vida eterna, no céu dos animais."

        self.capituloTresParagrafoUm = self.separaLinhas(self.textoCapituloTresParagrafoUm)

        self.textoCapituloTresParagrafoDois = "No  outro  mundo,  porém,  a  nossa  amada  python  ainda  se\n"\
                                              "sentia   estranha,  de  alguma  forma,  a  sede  e  a  fome  dela\n"\
                                              "pareciam  não ter fim,  mesmo tendo passado pela experiência\n"\
                                              "da  morte,  e  seu  instinto animal despertou mais uma vez, ele\n"\
                                              "iniciou  mais  uma  era  de caos,  por consequência  no terreno\n"\
                                              "sagrado  do  paraíso,  devorando  almas,  Querubins  e Serafins,\n"\
                                              "mas  diferente  da morte, não havia outro plano etéreo para as\n"\
                                              "vítimas  de Caillou, e uma vez devorado, sua existência se esvai\n"\
                                              "para todo o sempre."

        self.capituloTresParagrafoDois = self.separaLinhas(self.textoCapituloTresParagrafoDois)

        self.objetivoCapituloTres = fontes.comicNeue25.render("Objetivo: Acabe com 15 anjos", True, cores.White)

        # Capitulo 4

        self.capituloQuatro = fontes.comicNeue40.render("Capítulo 4 – A frota dos arcanjos", True, cores.White)

        self.textoCapituloQuatroParagrafoUm = "Deus  tendo  notado  tal  afronta  dentro  de  seu próprio reino,\n"\
                                              "sentiu   uma   grande  energia  maléfica  vinda  de,  Caillou  algo\n"\
                                              "semelhante com as vibrações negativas de Lúcifer, o anjo caído,\n"\
                                              "sem demora, Deus ordenou para que todos os arcanjos fossem\n"\
                                              "em direção da python  de  forma  que a mandasse diretamente\n"\
                                              "para  as  profundezas  do  inferno.  Os arcanjos  são  o posto de\n"\
                                              "maior hierarquia na divindade dos anjos,  poderosos  guerreiros\n"\
                                              "da paz com poderes inimagináveis."

        self.capituloQuatroParagrafoUm = self.separaLinhas(self.textoCapituloQuatroParagrafoUm)

        self.textoCapituloQuatroParagrafoDois = "Mesmo com todo o exército indo em direção da cobra, ela não\n"\
                                                "se  abalou,  pelo  contrário,  cada criatura dívida devorada a fez\n"\
                                                "ficar  cada  vez  maior  e  mais forte, tendo um incrível embate\n"\
                                                "contra as tropas do céu."

        self.capituloQuatroParagrafoDois = self.separaLinhas(self.textoCapituloQuatroParagrafoDois)

        self.objetivoCapituloQuatro = fontes.comicNeue25.render("Objetivo: Destrua 20 arcanjos", True, cores.White)

        # Capitulo 5

        self.capituloCinco = fontes.comicNeue40.render("Capítulo 5 – Julgamento de Caillou", True, cores.White)

        self.textoCapituloCincoParagrafoUm = "A  cobra  despertava sua fúria contra todos da  alvorada divina,\n"\
                                             "até ver em sua frente o príncipe da milícia celeste, São Miguel\n"\
                                             "Arcanjo,  paralisada  de  medo,  nada  pode  fazer,  até ter sua\n"\
                                             "cabeça  pisoteada  por  Maria,  a mãe de Jesus, e sem escolha,\n"\
                                             "viu São Miguel  erguer  sua  balança  e  iniciar o julgamento de\n"\
                                             "sua alma.  Mesmo sendo uma criatura irracional, seus pecados\n"\
                                             "não  poderiam  ser  relevados,  e  sua  alma  já  não tinha  mais\n"\
                                             "salvação,   ela  viu  o  Arcanjo  invocar  sua  espada  de  fogo  e\n"\
                                             "golpeá-la, precipitando sua alma para junto do reino de satanás,\n" \
                                             "o inferno."

        self.capituloCincoParagrafoUm = self.separaLinhas(self.textoCapituloCincoParagrafoUm)

        self.textoCapituloCincoParagrafoDois = "Mais  uma  vez,  Caillou havia  sido expurgada, e se viu em um\n"\
                                               "novo habitat  desconhecido, as chamas não ardiam, toda a sua\n"\
                                               "sede  e  fome já  não existia, e de alguma forma ela sentia que\n"\
                                               "naquele  lugar  seria  possível  chamá-lo  de lar,  e talvez ali ela\n"\
                                               "poderia viver enfim em paz."

        self.capituloCincoParagrafoDois = self.separaLinhas(self.textoCapituloCincoParagrafoDois)

        self.textoCapituloCincoParagrafoTres = "Alguns  demônios  não  demoraram  para  encontrá-la,  e  com\n"\
                                               "chicotes na mão, foram em sua direção para açoitá-la,  em um\n"\
                                               "gesto de legítima defesa, Caillou os devorou, mas diferente de\n" \
                                               "antes  que  se  alimentar  para  saciar  uma  fome  inesgotável,\n" \
                                               "Caillou pode se deleitar  e  se  divertir, então foi em direção de\n" \
                                               "outros demônios para continuar seu legado de caos, mas dessa\n" \
                                               "vez, por mera diversão."

        self.capituloCincoParagrafoTres = self.separaLinhas(self.textoCapituloCincoParagrafoTres)

        self.objetivoCapituloCinco = fontes.comicNeue25.render("Objetivo: Engula 25 Demônios", True, cores.White)

        # Capitulo 6

        self.capituloSeis = fontes.comicNeue40.render("Capítulo 6 –Imperador do Inferno", True, cores.White)

        self.textoCapituloSeisParagrafoUm = "Como no céu, o imperador do inferno, Lúcifer, não tardou para\n" \
                                            "encontrar  Caillou,  mas  ele  mesmo  decidiu  ir em direção da\n" \
                                            "criatura e combatê-la."

        self.capituloSeisParagrafoUm = self.separaLinhas(self.textoCapituloSeisParagrafoUm)

        self.textoCapituloSeisParagrafoDois = "- Ora, se não é aquela pequena cobrinha inútil da terra, quem\n" \
                                              "diria que iriamos  nos encontrar aqui, depois de fazê-la comer\n" \
                                              "aquele fruto proibido."

        self.capituloSeisParagrafoDois = self.separaLinhas(self.textoCapituloSeisParagrafoDois)

        self.textoCapituloSeisParagrafoTres = "O  fruto  proibido  ou  a  maçã  de Eva foi a origem  do  pecado\n" \
                                            "original da humanidade, que a fez cair no caos, o consumo dela\n" \
                                            "desperta uma  maldição eterna  para  a criatura que a digerir e\n" \
                                            "para toda a sua linhagem."

        self.capituloSeisParagrafoTres = self.separaLinhas(self.textoCapituloSeisParagrafoTres)

        self.textoCapituloSeisParagrafoQuatro = "- Você é uma  falha,  por  ser um “animalzinho puro”, não seria\n" \
                                                "barrada  na entrada do céu por qualquer pecado que fizesse, e\n" \
                                                "assim poderia consumir todos, eu lhe dei o poder para destruir\n" \
                                                "Deus...  achei que com essa maldição poderia fazer  com que a\n" \
                                                "minha sede e fome de vingança pelos seres celestes  poderiam\n" \
                                                "enfim  ser  saciados  através  de você...  estava errado, e agora\n" \
                                                "tenho que corrigir meu erro e acabar com a sua existência aqui\n" \
                                                "para SEMPRE!!"

        self.capituloSeisParagrafoQuatro = self.separaLinhas(self.textoCapituloSeisParagrafoQuatro)

        self.textoCapituloSeisParagrafoCinco = "Então Lúcifer se divide em diversas partes, e parte para o\n" \
                                               "ataque em direção de Caillou."

        self.capituloSeisParagrafoCinco = self.separaLinhas(self.textoCapituloSeisParagrafoCinco)

        self.objetivoCapituloSeis = fontes.comicNeue25.render("Objetivo: Oblitere as 30 partes de Lúcifer", True, cores.White)

        # Epilogo

        self.epilogo = fontes.comicNeue40.render("Epílogo", True, cores.White)

        self.epilogoTexto = "Após o confronto, o Capeta finalmente foi derrotado, e Cailllou\n" \
                              "vendo o trono do inferno desocupado, assume o seu mais novo\n" \
                              "reinado,  e assim, a nossa pequena cobrinha recebeu a alcunha\n" \
                              "de Imperador do Inferno."

        self.epilogoParagrafo = self.separaLinhas(self.epilogoTexto)

        self.epilogoMoralTexto = "Moral da história: A fome e sede de vingança nunca o levará a\n" \
                            "lugar algum, viva e se divirta"

        self.epilogoMoral = self.separaLinhas(self.epilogoMoralTexto)

        self.agradecimentos = fontes.hello30.render("Obrigado por jogar nosso jogo!!", True, cores.White)

        self.imagemCobrinha = fontes.animals90.render("S", True, cores.White)

    def saveData(self, texto):
        pickle.dump(texto, open("Save/savefile.dat", "wb"))

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
        paragrafo = [fontes.times20.render(linhas, True, cores.White) for linhas in texto]
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
        screen.blit(cenario.hellvsheaven, (0, 0))
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
                            self.saveData("Capitulo 1")
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
                            snake.resetCobrinha(30)
                            return "JogoCapituloUm"

                    if evento.key == K_ESCAPE:
                        return "MusicaMenu"

        return currentScene

    def desenhaCapituloDois(self, screen):
        screen.fill(cores.Black)

        self.timer = (pygame.time.get_ticks() - self.initialTime) / 1000
        self.timer = int(self.timer)

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("src/Musics/veraoCatastrofe.mp3")
            pygame.mixer.music.play(-1)

        if self.currentScene == "Capitulo 2":
            if 1 < self.timer < 5:
                screen.blit(self.capituloDois,
                            (300 - self.capituloDois.get_width() // 2, 350 - self.capituloDois.get_height() // 2))
            elif self.timer > 5:
                self.currentScene = "Capitulo 2, 1"
                self.initialTime = pygame.time.get_ticks()

        elif self.currentScene == "Capitulo 2, 1":
            screen.blit(cenario.animals, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.capituloDoisParagrafoUm:
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

        elif self.currentScene == "Capitulo 2, 2" or self.currentScene == "ObjetivoCapituloDois":
            screen.blit(cenario.city, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.capituloDoisParagrafoDois:
                self.espacoEntreLinhas += 30
                screen.blit(linhas, (50, 180 + self.espacoEntreLinhas))

            if self.timer % 2 == 0:
                screen.blit(self.btnEnter,
                            (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                screen.blit(self.btnEsc, (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

            if self.currentScene == "ObjetivoCapituloDois":
                self.alphaZero = min(self.alphaZero + (self.deltaTime * 5), 255)
                self.alphaSurface.set_alpha(self.alphaZero)
                screen.blit(self.alphaSurface, (0, 0))

                if self.alphaZero >= 255:
                    screen.blit(self.objetivoCapituloDois,
                                (300 - self.objetivoCapituloDois.get_width() // 2, 350 - self.objetivoCapituloDois.get_height() // 2))

                    if self.timer % 2 == 0:
                        screen.blit(self.btnEnter,
                                    (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                        screen.blit(self.btnEsc,
                                    (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

        pygame.display.flip()

        self.clock.tick(60)

    def eventoCapituloDois(self, currentScene, Flow, snake):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                return "Fim"

            if self.currentScene == "Capitulo 2, 1" or self.currentScene == "Capitulo 2, 2" or self.currentScene == "ObjetivoCapituloDois":
                if evento.type == KEYDOWN:
                    if evento.key == K_KP_ENTER or evento.key == K_RETURN:
                        if self.currentScene == "Capitulo 2, 1":
                            return "Capitulo 2, 2"
                        elif self.currentScene == "Capitulo 2, 2":
                            return "ObjetivoCapituloDois"
                        elif self.alphaZero >= 255:
                            pygame.mixer.music.stop()
                            self.resetAlpha()
                            Flow.resetGame("Garden", snake)
                            snake.resetCobrinha(40)
                            return "JogoCapituloDois"

                    if evento.key == K_ESCAPE:
                        return "MusicaMenu"

        return currentScene

    def desenhaCapituloTres(self, screen):
        screen.fill(cores.Black)

        self.timer = (pygame.time.get_ticks() - self.initialTime) / 1000
        self.timer = int(self.timer)

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("src/Musics/invernoTriste.mp3")
            pygame.mixer.music.play(-1)

        if self.currentScene == "Capitulo 3":
            if 1 < self.timer < 5:
                screen.blit(self.capituloTres,
                            (300 - self.capituloTres.get_width() // 2, 350 - self.capituloTres.get_height() // 2))
            elif self.timer > 5:
                self.currentScene = "Capitulo 3, 1"
                self.initialTime = pygame.time.get_ticks()

        elif self.currentScene == "Capitulo 3, 1":
            screen.blit(cenario.explosao, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.capituloTresParagrafoUm:
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

        elif self.currentScene == "Capitulo 3, 2" or self.currentScene == "ObjetivoCapituloTres":
            screen.blit(cenario.SelectHeaven, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.capituloTresParagrafoDois:
                self.espacoEntreLinhas += 30
                screen.blit(linhas, (50, 180 + self.espacoEntreLinhas))

            if self.timer % 2 == 0:
                screen.blit(self.btnEnter,
                            (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                screen.blit(self.btnEsc, (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

            if self.currentScene == "ObjetivoCapituloTres":
                self.alphaZero = min(self.alphaZero + (self.deltaTime * 5), 255)
                self.alphaSurface.set_alpha(self.alphaZero)
                screen.blit(self.alphaSurface, (0, 0))

                if self.alphaZero >= 255:
                    screen.blit(self.objetivoCapituloTres,
                                (300 - self.objetivoCapituloTres.get_width() // 2, 350 - self.objetivoCapituloTres.get_height() // 2))

                    if self.timer % 2 == 0:
                        screen.blit(self.btnEnter,
                                    (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                        screen.blit(self.btnEsc,
                                    (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

        pygame.display.flip()

        self.clock.tick(60)

    def eventoCapituloTres(self, currentScene, Flow, snake):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                return "Fim"

            if self.currentScene == "Capitulo 3, 1" or self.currentScene == "Capitulo 3, 2" or self.currentScene == "ObjetivoCapituloTres":
                if evento.type == KEYDOWN:
                    if evento.key == K_KP_ENTER or evento.key == K_RETURN:
                        if self.currentScene == "Capitulo 3, 1":
                            return "Capitulo 3, 2"
                        elif self.currentScene == "Capitulo 3, 2":
                            return "ObjetivoCapituloTres"
                        elif self.alphaZero >= 255:
                            pygame.mixer.music.stop()
                            self.resetAlpha()
                            Flow.resetGame("Sky", snake)
                            snake.resetCobrinha(30)
                            return "JogoCapituloTres"

                    if evento.key == K_ESCAPE:
                        return "MusicaMenu"

        return currentScene

    def desenhaCapituloQuatro(self, screen):
        screen.fill(cores.Black)

        self.timer = (pygame.time.get_ticks() - self.initialTime) / 1000
        self.timer = int(self.timer)

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("src/Musics/primaveraNoParaiso.mp3")
            pygame.mixer.music.play(-1)

        if self.currentScene == "Capitulo 4":
            if 1 < self.timer < 5:
                screen.blit(self.capituloQuatro,
                            (300 - self.capituloQuatro.get_width() // 2, 350 - self.capituloQuatro.get_height() // 2))
            elif self.timer > 5:
                self.currentScene = "Capitulo 4, 1"
                self.initialTime = pygame.time.get_ticks()

        elif self.currentScene == "Capitulo 4, 1":
            screen.blit(cenario.arcanjos, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.capituloQuatroParagrafoUm:
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

        elif self.currentScene == "Capitulo 4, 2" or self.currentScene == "ObjetivoCapituloQuatro":
            screen.blit(cenario.arcanjos, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.capituloQuatroParagrafoDois:
                self.espacoEntreLinhas += 30
                screen.blit(linhas, (50, 180 + self.espacoEntreLinhas))

            if self.timer % 2 == 0:
                screen.blit(self.btnEnter,
                            (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                screen.blit(self.btnEsc, (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

            if self.currentScene == "ObjetivoCapituloQuatro":
                self.alphaZero = min(self.alphaZero + (self.deltaTime * 5), 255)
                self.alphaSurface.set_alpha(self.alphaZero)
                screen.blit(self.alphaSurface, (0, 0))

                if self.alphaZero >= 255:
                    screen.blit(self.objetivoCapituloQuatro,
                                (300 - self.objetivoCapituloQuatro.get_width() // 2, 350 - self.objetivoCapituloQuatro.get_height() // 2))

                    if self.timer % 2 == 0:
                        screen.blit(self.btnEnter,
                                    (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                        screen.blit(self.btnEsc,
                                    (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

        pygame.display.flip()

        self.clock.tick(60)

    def eventoCapituloQuatro(self, currentScene, Flow, snake):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                return "Fim"

            if self.currentScene == "Capitulo 4, 1" or self.currentScene == "Capitulo 4, 2" or self.currentScene == "ObjetivoCapituloQuatro":
                if evento.type == KEYDOWN:
                    if evento.key == K_KP_ENTER or evento.key == K_RETURN:
                        if self.currentScene == "Capitulo 4, 1":
                            return "Capitulo 4, 2"
                        elif self.currentScene == "Capitulo 4, 2":
                            return "ObjetivoCapituloQuatro"
                        elif self.alphaZero >= 255:
                            pygame.mixer.music.stop()
                            self.resetAlpha()
                            Flow.resetGame("Sky", snake)
                            snake.resetCobrinha(40)
                            return "JogoCapituloQuatro"

                    if evento.key == K_ESCAPE:
                        return "MusicaMenu"

        return currentScene

    def desenhaCapituloCinco(self, screen):
        screen.fill(cores.Black)

        self.timer = (pygame.time.get_ticks() - self.initialTime) / 1000
        self.timer = int(self.timer)

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("src/Musics/veraoJulgamento.mp3")
            pygame.mixer.music.play(-1)

        if self.currentScene == "Capitulo 5":
            if 1 < self.timer < 5:
                screen.blit(self.capituloCinco,
                            (300 - self.capituloCinco.get_width() // 2, 350 - self.capituloCinco.get_height() // 2))
            elif self.timer > 5:
                self.currentScene = "Capitulo 5, 1"
                self.initialTime = pygame.time.get_ticks()

        elif self.currentScene == "Capitulo 5, 1":
            screen.blit(cenario.virgemMaria, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.capituloCincoParagrafoUm:
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

        elif self.currentScene == "Capitulo 5, 2":
            screen.blit(cenario.saoMiguel, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.capituloCincoParagrafoDois:
                self.espacoEntreLinhas += 30
                screen.blit(linhas, (50, 180 + self.espacoEntreLinhas))

            if self.timer % 2 == 0:
                screen.blit(self.btnEnter,
                            (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                screen.blit(self.btnEsc, (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

        elif self.currentScene == "Capitulo 5, 3" or self.currentScene == "ObjetivoCapituloCinco":
            screen.blit(cenario.SelectHell, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.capituloCincoParagrafoTres:
                self.espacoEntreLinhas += 30
                screen.blit(linhas, (50, 180 + self.espacoEntreLinhas))

            if self.timer % 2 == 0:
                screen.blit(self.btnEnter,
                            (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                screen.blit(self.btnEsc, (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))
            if self.currentScene == "ObjetivoCapituloCinco":
                self.alphaZero = min(self.alphaZero + (self.deltaTime * 5), 255)
                self.alphaSurface.set_alpha(self.alphaZero)
                screen.blit(self.alphaSurface, (0, 0))

                if self.alphaZero >= 255:
                    screen.blit(self.objetivoCapituloCinco,
                                (300 - self.objetivoCapituloCinco.get_width() // 2, 350 - self.objetivoCapituloCinco.get_height() // 2))

                    if self.timer % 2 == 0:
                        screen.blit(self.btnEnter,
                                    (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                        screen.blit(self.btnEsc,
                                    (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

        pygame.display.flip()

        self.clock.tick(60)

    def eventoCapituloCinco(self, currentScene, Flow, snake):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                return "Fim"

            if self.currentScene == "Capitulo 5, 1" or self.currentScene == "Capitulo 5, 2"  or self.currentScene == "Capitulo 5, 3" or self.currentScene == "ObjetivoCapituloCinco":
                if evento.type == KEYDOWN:
                    if evento.key == K_KP_ENTER or evento.key == K_RETURN:
                        if self.currentScene == "Capitulo 5, 1":
                            return "Capitulo 5, 2"
                        elif self.currentScene == "Capitulo 5, 2":
                            return "Capitulo 5, 3"
                        elif self.currentScene == "Capitulo 5, 3":
                            return "ObjetivoCapituloCinco"
                        elif self.alphaZero >= 255:
                            pygame.mixer.music.stop()
                            self.resetAlpha()
                            Flow.resetGame("Hell", snake)
                            snake.resetCobrinha(30)
                            return "JogoCapituloCinco"

                    if evento.key == K_ESCAPE:
                        return "MusicaMenu"

        return currentScene

    def desenhaCapituloSeis(self, screen):
        screen.fill(cores.Black)

        self.timer = (pygame.time.get_ticks() - self.initialTime) / 1000
        self.timer = int(self.timer)

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("src/Musics/veraoBatalha.mp3")
            pygame.mixer.music.play(-1)

        if self.currentScene == "Capitulo 6":
            if 1 < self.timer < 5:
                screen.blit(self.capituloSeis,
                            (300 - self.capituloSeis.get_width() // 2, 350 - self.capituloSeis.get_height() // 2))
            elif self.timer > 5:
                self.currentScene = "Capitulo 6, 1"
                self.initialTime = pygame.time.get_ticks()

        elif self.currentScene == "Capitulo 6, 1":
            screen.blit(cenario.hellThrone, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.capituloSeisParagrafoUm:
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

        elif self.currentScene == "Capitulo 6, 2":
            screen.blit(cenario.capeta, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.capituloSeisParagrafoDois:
                self.espacoEntreLinhas += 30
                screen.blit(linhas, (50, 180 + self.espacoEntreLinhas))

            if self.timer % 2 == 0:
                screen.blit(self.btnEnter,
                            (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                screen.blit(self.btnEsc, (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

        elif self.currentScene == "Capitulo 6, 3":
            screen.blit(cenario.frutaProibida, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.capituloSeisParagrafoTres:
                self.espacoEntreLinhas += 30
                screen.blit(linhas, (50, 180 + self.espacoEntreLinhas))

            if self.timer % 2 == 0:
                screen.blit(self.btnEnter,
                            (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                screen.blit(self.btnEsc, (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

        elif self.currentScene == "Capitulo 6, 4":
            screen.blit(cenario.capeta, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.capituloSeisParagrafoQuatro:
                self.espacoEntreLinhas += 30
                screen.blit(linhas, (50, 180 + self.espacoEntreLinhas))

            if self.timer % 2 == 0:
                screen.blit(self.btnEnter,
                            (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                screen.blit(self.btnEsc, (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

        elif self.currentScene == "Capitulo 6, 5" or self.currentScene == "ObjetivoCapituloSeis":
            screen.blit(cenario.capeta, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.capituloSeisParagrafoCinco:
                self.espacoEntreLinhas += 30
                screen.blit(linhas, (50, 180 + self.espacoEntreLinhas))

            if self.timer % 2 == 0:
                screen.blit(self.btnEnter,
                            (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                screen.blit(self.btnEsc, (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))
            if self.currentScene == "ObjetivoCapituloSeis":
                self.alphaZero = min(self.alphaZero + (self.deltaTime * 5), 255)
                self.alphaSurface.set_alpha(self.alphaZero)
                screen.blit(self.alphaSurface, (0, 0))

                if self.alphaZero >= 255:
                    screen.blit(self.objetivoCapituloSeis,
                                (300 - self.objetivoCapituloSeis.get_width() // 2, 350 - self.objetivoCapituloSeis.get_height() // 2))

                    if self.timer % 2 == 0:
                        screen.blit(self.btnEnter,
                                    (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                        screen.blit(self.btnEsc,
                                    (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

        pygame.display.flip()

        self.clock.tick(60)

    def eventoCapituloSeis(self, currentScene, Flow, snake):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                return "Fim"

            if self.currentScene == "Capitulo 6, 1" or self.currentScene == "Capitulo 6, 2" \
                    or self.currentScene == "Capitulo 6, 3" or self.currentScene == "Capitulo 6, 4" \
                    or self.currentScene == "Capitulo 6, 5" or self.currentScene == "ObjetivoCapituloSeis":
                if evento.type == KEYDOWN:
                    if evento.key == K_KP_ENTER or evento.key == K_RETURN:
                        if self.currentScene == "Capitulo 6, 1":
                            return "Capitulo 6, 2"
                        elif self.currentScene == "Capitulo 6, 2":
                            return "Capitulo 6, 3"
                        elif self.currentScene == "Capitulo 6, 3":
                            return "Capitulo 6, 4"
                        elif self.currentScene == "Capitulo 6, 4":
                            return "Capitulo 6, 5"
                        elif self.currentScene == "Capitulo 6, 5":
                            return "ObjetivoCapituloSeis"
                        elif self.alphaZero >= 255:
                            pygame.mixer.music.stop()
                            self.resetAlpha()
                            Flow.resetGame("Hell", snake)
                            snake.resetCobrinha(40)
                            return "JogoCapituloSeis"

                    if evento.key == K_ESCAPE:
                        return "MusicaMenu"

        return currentScene

    def desenhaEpilogo(self, screen):
        screen.fill(cores.Black)

        self.timer = (pygame.time.get_ticks() - self.initialTime) / 1000
        self.timer = int(self.timer)

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("src/Musics/primaveraFim.mp3")
            pygame.mixer.music.play(-1)

        if self.currentScene == "Epilogo":
            if 1 < self.timer < 5:
                screen.blit(self.epilogo,
                            (300 - self.epilogo.get_width() // 2, 350 - self.epilogo.get_height() // 2))
            elif self.timer > 5:
                self.currentScene = "Epilogo, 1"
                self.initialTime = pygame.time.get_ticks()

        elif self.currentScene == "Epilogo, 1" or self.currentScene == "Moral":
            screen.blit(cenario.whiteSnake, (0, 0))

            self.espacoEntreLinhas = 0
            for linhas in self.epilogoParagrafo:
                self.espacoEntreLinhas += 30
                screen.blit(linhas, (50, 380 + self.espacoEntreLinhas))

            if self.timer % 2 == 0:
                screen.blit(self.btnEnter,
                            (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                screen.blit(self.btnEsc, (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

            if self.currentScene == "Moral":
                self.alphaZero = min(self.alphaZero + (self.deltaTime * 5), 255)
                self.alphaSurface.set_alpha(self.alphaZero)
                screen.blit(self.alphaSurface, (0, 0))

                if self.alphaZero >= 255:
                    for linhas in self.epilogoMoral:
                        self.espacoEntreLinhas += 30
                        screen.blit(linhas, (50, 180 + self.espacoEntreLinhas))

                    screen.blit(self.agradecimentos, (300, 550))
                    screen.blit(self.imagemCobrinha, (370, 590))

                    if self.timer % 2 == 0:
                        screen.blit(self.btnEnter,
                                    (450 - self.btnEnter.get_width() // 2, 690 - self.btnEnter.get_height() // 2))
                        screen.blit(self.btnEsc,
                                    (150 - self.btnEsc.get_width() // 2, 690 - self.btnEsc.get_height() // 2))

        pygame.display.flip()

        self.clock.tick(60)

    def eventoEpilogo(self, currentScene, creditos):
        for evento in pygame.event.get():
            if evento.type == QUIT:
                return "Fim"

            if self.currentScene == "Epilogo, 1" or self.currentScene == "Moral":
                if evento.type == KEYDOWN:
                    if evento.key == K_KP_ENTER or evento.key == K_RETURN:
                        if self.currentScene == "Epilogo, 1":
                            return "Moral"
                        elif self.alphaZero >= 255:
                            pygame.mixer.music.stop()
                            self.resetAlpha()
                            creditos.initialTime = pygame.time.get_ticks()
                            pygame.mixer.music.load("src/Musics/snake-eater.mp3")
                            pygame.mixer.music.play(0)
                            return "Creditos"

                    if evento.key == K_ESCAPE:
                        return "MusicaMenu"

        return currentScene