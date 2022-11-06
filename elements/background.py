import pygame
from typing import List

from elements.generic.element import Element
from elements.duck import Duck
from scenes.scene import Scene


class Background(Element):
    def __init__(self, scene: Scene) -> None:
        super().__init__(scene, "trees.png", 0, 0)
        self.grass = Element(scene, "grass.png", 0, self.rect.height)
        # sacar a los patos de aca y ponerlos en game scene
        # aca solamente irian todas las cosas estaticas que no tienen mecanicas
        self.ducks: List[Duck] = []
        self.ducks.append(Duck(scene, 600, 350))

    def on_draw(self, screen: pygame.Surface):
        screen.fill((51, 255, 255))
        super().on_draw(screen)
        self.grass.on_draw(screen)

        for duck in self.ducks:
            duck.on_draw(screen)
