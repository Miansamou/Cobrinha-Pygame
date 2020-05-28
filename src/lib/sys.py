import pygame

class System:
    def __init__(self):
        # Indica o tamanho da tela
        self.screen = pygame.display.set_mode((600, 700))

        # Título da tela de gameplay
        pygame.display.set_caption('Jogo da cobrinha')

        # Esconde o mouse
        pygame.mouse.set_visible(0)

        # Seta do menu
        self.seta = [(220, 185), (220, 215), (235, 200)]

        self.dificuldade = 0

        self.cenario = "Garden"

        self.clock = pygame.time.Clock()

    def mudarPrimeiroArrayBimensional(self, valorImutavel, valorTotal, soma):
        valorTotal += soma
        return (valorImutavel, valorTotal)

    def mudarSegundoArrayBimensional(self, valorImutavel, valorTotal, soma):
        valorTotal += soma
        return (valorTotal, valorImutavel)

    def setDificuldade(self, number):
        self.dificuldade = number

    def getDificuldade(self):
        return self.dificuldade

    def setCenario(self, scene):
        self.cenario = scene

    def getCenario(self):
        return self.cenario