import pygame

from typing import Callable
from elements.generic.element import Element
from scenes.scene import Scene


class Button(Element):
    def __init__(self, scene: Scene, image: str, x: int, y: int, func: Callable[[None], None]) -> None:
        self.func = func
        super().__init__(scene, image, x, y, center=True)

    def action(self):
        self.func()

    def isHovering(self, event: pygame.event.Event):
        if event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
