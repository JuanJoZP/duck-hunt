from director import Director
from scene import Scene
import pygame


class HomeScene(Scene):
    """ Welcome screen of the game, the first one to be loaded."""

    def __init__(self, director: Director):
        Scene.__init__(self, director)

    def on_update(self):
        pass

    def on_event(self):
        pass

    def on_draw(self, screen):
        screen.fill((255, 255, 255))
