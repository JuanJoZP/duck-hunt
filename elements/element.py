import pygame

from utils import scale_image
from scenes.scene import Scene


class Element:
    def __init__(self, scene: Scene, image: str, x: int, y: int, zoom: int) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.scene = scene
        self.image = scale_image(pygame.image.load(
            f"img/{image}").convert_alpha(), zoom)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def on_update() -> None:
        "Called from the scene and defined on the subclass."

        raise NotImplementedError(
            "on_update abstract method must be defined in subclass.")

    def on_event(self, event: pygame.event.Event) -> None:
        "Called when a specific event is detected in the loop."

        raise NotImplementedError(
            "on_event abstract method must be defined in subclass.")

    def on_draw(self, screen: pygame.Surface) -> None:
        "Called to draw the element to the screen."

        screen.blit(self.image, (self.rect.x, self.rect.y))
