import pygame, os

# Caminhos absolutos das fontes desejadas
filesComicNeue = os.path.join(os.path.dirname(__file__), "ComicNeue-Regular.ttf")
filesChikhenButt = os.path.join(os.path.dirname(__file__), "ChickenButt.ttf")
filesTimesNewRoman = os.path.join(os.path.dirname(__file__), "TimesNewRoman.ttf")
filesHelloLittleTiger = os.path.join(os.path.dirname(__file__), "HelloLittleTiger.otf")
filesPhonicsAnimals2 = os.path.join(os.path.dirname(__file__), "PhonicsAnimals2.ttf")
filesParisienne = os.path.join(os.path.dirname(__file__), "Parisienne-Regular.ttf")

pygame.init()

# Fontes Comic Neue
comicNeue90 = pygame.font.Font(filesComicNeue, 90)
comicNeue40 = pygame.font.Font(filesComicNeue, 40)
comicNeue15 = pygame.font.Font(filesComicNeue, 15)
comicNeue25 = pygame.font.Font(filesComicNeue, 25)

# Fontes Chikhen Butt
chikhenButt70 = pygame.font.Font(filesChikhenButt, 70)

#Fonte Hello Little Tiger
hello30 = pygame.font.Font(filesHelloLittleTiger, 30)

#Fonte Animals
animals90 = pygame.font.Font(filesPhonicsAnimals2, 90)

#Fonte Times New Roman
times20 = pygame.font.Font(filesTimesNewRoman, 20)

#Fonte Parisienne
parisienne25 = pygame.font.Font(filesParisienne, 25)