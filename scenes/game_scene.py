from director import Director
from scenes.scene import Scene
from elements.background import Background


class GameScene(Scene):
    """Ventana principal del juego"""

    def __init__(self, director: Director):
        Scene.__init__(self, director)
        self.bg = Background(self, "trees.png", 0, 0, 1)

    def on_update(self):
        # aca actualizar el hover de los botones
        pass

    def on_event(self, event):
        pass

    def on_draw(self, screen):
        screen.fill((255, 255, 255))
        self.bg.on_draw(screen)

        pass
