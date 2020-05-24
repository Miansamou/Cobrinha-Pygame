import pygame, os

filesComicNeue = os.path.join(os.path.dirname(__file__), "ComicNeue-Regular.ttf")  # Pega o caminho absoluto da fonte desejada
filesChikhenButt = os.path.join(os.path.dirname(__file__), "ChickenButt.ttf")

pygame.init()

# Fontes Comic Neue
comicNeue90 = pygame.font.Font(filesComicNeue, 90)
comicNeue40 = pygame.font.Font(filesComicNeue, 40)
comicNeue15 = pygame.font.Font(filesComicNeue, 15)
comicNeue25 = pygame.font.Font(filesComicNeue, 25)

# Fontes Chikhen Butt
chikhenButt70 = pygame.font.Font(filesChikhenButt, 70)