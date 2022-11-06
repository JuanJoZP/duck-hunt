import pygame
pygame.font.init()

TITLE = "Duck hunt"
ICON = pygame.image.load('./img/duck.png')
FONT = pygame.font.Font('font/SummerPixel.ttf', 100)
TEXT_COL = (255, 255, 255)
BASE_RES = 720


class screenSize:
    def __init__(self) -> None:
        self.screen_size = (0, 0)

    def getSize(self):
        return self.screen_size

    def setSize(self, xy):
        self.screen_size = (xy[0], xy[1])


SCREEN_SIZE = screenSize()
