import pygame
from elements.element import Element
from scenes.scene import Scene


class Background(Element):
    def __init__(self, scene: Scene, image: str, x: int, y: int, zoom: int) -> None:
        super().__init__(scene, image, x, y, zoom)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def on_draw(self, screen: pygame.Surface):
        screen.fill((51, 255, 255))
        super().on_draw(screen)
