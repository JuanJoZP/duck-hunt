from director import Director
from scene import Scene
import pygame


class HomeScene(Scene):
    """ Welcome screen of the game, the first one to be loaded."""

    def __init__(self, director: Director):
        Scene.__init__(self, director)
        # aca se declaran todos los botones, se pueden añadir a un grupo
        # para manejarlos mas facil
        # tambien el resto de elementos que solo hay que dibujar

    def on_update(self):
        # aca actualizar el hover de los botones
        pass

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # si hay un click entonces mirar si el click fue dentro del
            # boton, si si fue dentro del boton entonces llamar la funcion
            # que tiene que hacer ese boton
            pass

    def on_draw(self, screen):
        # se dibujan todos los elementos puede ser usando los grupos
        screen.fill((255, 255, 255))
