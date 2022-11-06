import pygame
from elements.generic.element import Element
from scenes.scene import Scene


class Duck(Element):
    def __init__(self, scene: Scene, x: int, y: int) -> None:
        super().__init__(scene, "duck_sprite.png", x, y)
        # cambiar el x y por un rand

        # revisar la posicion, esta quedando mal cuando se cambia de resolucion
        # puede ser que no este mal duck sino grass o trees

    def on_draw(self, screen: pygame.Surface):
        super().on_draw(screen)
