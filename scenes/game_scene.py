from director import Director
from scenes.scene import Scene

from elements.background import Background
from elements.round import Round
from elements.bullets import Mira


class GameScene(Scene):
    """Ventana principal del juego"""

    def __init__(self, director: Director):
        Scene.__init__(self, director)
        self.bg = Background(self)
        self.round = Round(self, 1, 10, 0)
        self.mira = Mira(self, self.round)
        # toca cuadrar el tamaño de todas las imagenes
        # cuadrarlas para que se vean bien en una ventana de 1280x720 pixeles

        # revisar todos los elementos que no se este usando directamente el x,y
        # primero hay que pasarlas por relative_pos para acomodarlas a la resolucion

    def on_update(self):
        self.bg.on_update()
        self.round.on_update()
        self.mira.on_update()

    def on_event(self, event):
        pass

    def on_draw(self, screen):
        screen.fill((255, 255, 255))
        self.bg.on_draw(screen)
        self.round.on_draw(screen)
        self.mira.on_draw(screen)

        pass
