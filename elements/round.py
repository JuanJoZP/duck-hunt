import pygame
from typing import List

from elements.generic.element import Element
from elements.duck import Duck
from elements.score import Score
from scenes.scene import Scene


class Round(Element):
    def __init__(self, scene: Scene, n_round: int, total_ducks: int, score: Score) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.scene = scene
        self.duck = Duck(scene, 5)

    def on_update(self) -> None:
        # primero mover el pato
        self.duck.on_update()
        # sumar el timer para que el pato se vaya
        # tambien checkear el timer para sacar al pato y seguir con el otro
        pass

    def on_event(self, event: pygame.event.Event) -> None:
        # aca toca tomar los clicks o el boton del arduino
        # llamar la animacion o sonido de los disparos
        # luego mirar si colisiona con la posicion del pato
        # si si, llamar el metodo del pato que hace que caiga, cambiar de pato, sumar score
        # si no, resta un tiro disponible
        pass

    def on_draw(self, screen: pygame.Surface) -> None:
        self.duck.on_draw(screen)

    def get_done() -> bool:
        # true si ya pasaron todos los patos
        pass

    def get_ducks_info():
        # devuelve el numero de pato que esta pasando, cuantos ha fallado, cuantos faltan etc
        pass
