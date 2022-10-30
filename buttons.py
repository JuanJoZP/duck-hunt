import pygame
from typing import Callable


class Button():
    def __init__(self, x: int, y: int, image: pygame.Surface, func: Callable[[None], None]):
        self.image = image
        self.func = func
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw_button(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def action(self):
        self.func()

    def isHovering(self, event: pygame.event.Event):
        if event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
