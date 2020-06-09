import pygame, random

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

        # Dificuldade base
        self.dificuldade = 15

        # Score primário
        self.score = 0

        # Cenário primário
        self.cenario = "Garden"

        self.clock = pygame.time.Clock()

    # Base para a movimentação da seta nos menus e da cobrinha
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

    # Atualização randômica do item da na tela
    def on_grid_random(self, min, max):
        x = random.randint(min, max)
        y = random.randint(min, max)
        return (x // 10 * 10, y // 10 * 10)