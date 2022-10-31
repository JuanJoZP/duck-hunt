from director import Director
from scenes.scene import Scene
import pygame


class GameScene(Scene):
    """Ventana principal del juego"""

    def __init__(self, director: Director):
        Scene.__init__(self, director)
        # aca se declaran todos los botones, se pueden añadir a un grupo
        # para manejarlos mas facil
        # tambien el resto de elementos que solo hay que dibujar

    def on_update(self):
        # aca actualizar el hover de los botones
        pass

    def on_event(self, event):
        pass

    def on_draw(self, screen):
        # se dibujan todos los elementos puede ser usando los grupos
        screen.fill((255, 255, 255))
        pass
