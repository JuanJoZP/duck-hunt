import pygame

from math import tan, radians

from elements.generic.element import Element
from elements.round import Round
from scenes.scene import Scene

from arduino import Arduino
from config import DIST, BASE_RES
from utils import relative_pos


class Mira(Element):
    def __init__(self, scene: Scene, round: Round) -> None:
        super().__init__(scene, "mira.png", 0, 0, True)
        self.arduino = Arduino()
        self.round = round

    def on_update(self) -> None:
        data = self.arduino.read()
        if len(data) == 3:
            angle_y = data[2].replace("\r\n", "")
            # x =
            y = -tan(radians(float(angle_y))) * DIST
            py = ((19.5/2)-y)*(720/19.5)
            print(y)
            self.rect.center = relative_pos(460, py)

            if data[0] == "shot":
                self.round.duck.shoot(*self.rect.center)

    def on_draw(self, screen: pygame.Surface):
        super().on_draw(screen)
