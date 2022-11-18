import pygame
from random import randrange
from math import sin, cos, radians, pi

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

        # 0 a 360 pero en radianes, inicializarlo random
        self.angle = radians(30)
        self.velocity = vel

    def on_update(self) -> None:
        if self.leave:
            self.move_leave()
        elif self.fall:
            self.move_fall()
        else:
            self.move_vel()

    def check_bounce(self):
        MAX_X, MAX_Y = relative_pos(MAX_DUCK_SPAWN[0], MAX_DUCK_SPAWN[1])
        if self.rect.top < 0:
            self.angle = 2 * pi - self.angle
            self.rect.top = 0
        elif self.rect.bottom > MAX_Y:
            self.angle = 2 * pi - self.angle
            self.rect.bottom = MAX_Y
        elif self.rect.left < 0:
            self.angle = pi - self.angle
            self.rect.left = 0
        elif self.rect.right > MAX_X:
            self.angle = pi - self.angle
            self.rect.right = MAX_X

    def move_vel(self):
        self.check_bounce()
        x = self.velocity * cos(self.angle)
        # en pygame y aumenta hacia abajo, cambia signo
        y = -self.velocity * sin(self.angle)

        new_pos = relative_pos(x, y)
        new_pos = (new_pos[0] + self.rect.topleft[0],
                   new_pos[1] + self.rect.topleft[1])
        self.rect.topleft = new_pos

    def move_fall(self):
        x = 0
        y = self.velocity

        new_pos = relative_pos(x, y)
        new_pos = (new_pos[0] + self.rect.topleft[0],
                   new_pos[1] + self.rect.topleft[1])
        self.rect.topleft = new_pos

    def move_leave():
        # animacion cuando se va
        pass

    def on_draw(self, screen: pygame.Surface):
        super().on_draw(screen)

    def shoot(self, x, y) -> bool:
        if x >= self.rect.left and x <= self.rect.right:
            if y >= self.rect.top and y <= self.rect.bottom:
                self.fall = True

    def kill(self) -> None:
        del self
