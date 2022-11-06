from director import Director
from scenes.scene import Scene
from elements.background import Background


class GameScene(Scene):
    """Ventana principal del juego"""

    def __init__(self, director: Director):
        Scene.__init__(self, director)
        self.bg = Background(self)
        # toca cuadrar el tamaño de todas las imagenes
        # cuadrarlas para que se vean bien en una ventana de 1280x720 pixeles

        # revisar todos los elementos que no se este usando directamente el x,y
        # primero hay que pasarlas por relative_pos para acomodarlas a la resolucion

    def on_update(self):
        pass

    def on_event(self, event):
        pass

    def on_draw(self, screen):
        screen.fill((255, 255, 255))
        self.bg.on_draw(screen)

        pass
