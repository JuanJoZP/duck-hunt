import pygame
from random import randrange
from math import sin, cos, radians

from config import MAX_DUCK_SPAWN
from utils import relative_pos

from elements.generic.element import Element
from scenes.scene import Scene


class Duck(Element):
    def __init__(self, scene: Scene, vel: int) -> None:
        super().__init__(scene, "duck_sprite.png", 0, 0)
        x = randrange(0, MAX_DUCK_SPAWN[0] - self.rect.width)
        y = randrange(0, MAX_DUCK_SPAWN[1] - self.rect.height)
        self.rect.topleft = relative_pos(x, y)

        self.leave = False
        self.fall = False

        self.angle = 45  # 0 a 360, inicializarlo random
        self.velocity = vel

    def on_update(self) -> None:
        if self.leave:
            self.move_leave()
        elif self.fall:
            self.move_fall()
        else:
            self.move_vel()

    def on_draw(self, screen: pygame.Surface):
        print("moveee")
        super().on_draw(screen)

    def move_vel(self):
        # FALTA HACER LOS REBOTES
        x = self.velocity * cos(radians(self.angle))
        # en pygame y aumenta hacia abajo, cambia signo
        y = -self.velocity * sin(radians(self.angle))

        new_pos = relative_pos(x, y)
        new_pos = (new_pos[0] + self.rect.topleft[0],
                   new_pos[1] + self.rect.topleft[1])
        self.rect.topleft = new_pos

    def move_fall():
        # animacion cuando le disparan
        pass

    def move_leave():
        # animacion cuando se va
        pass

    def in_sight(x, y) -> bool:
        # true si x y esta dentro de el pato
        pass

    def kill(self) -> None:
        del self
