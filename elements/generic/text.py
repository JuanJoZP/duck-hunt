import pygame
from config import FONT
from utils import relative_pos


class Text:
    """Centered Text Class"""

    def __init__(self, text: str, x: int, y: int, color=(0, 0, 0), font=FONT):
        self.x, self.y = relative_pos(x, y)

        pygame.font.init()
        font = font
        self.txt = font.render(text, True, color)
        self.size = font.size(text)  # (width, height)

    def on_draw(self, screen):
        # coordenadas del centro del texto
        coords = (self.x - (self.size[0] / 2.), self.y - (self.size[1] / 2.))
        screen.blit(self.txt, coords)
