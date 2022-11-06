import pygame

from director import Director
from elements.generic.button import Button
from elements.generic.text import Text

from scenes.scene import Scene
from scenes.game_scene import GameScene

from config import FONT, TEXT_COL


class HomeScene(Scene):
    """ Welcome screen of the game, the first one to be loaded."""

    def __init__(self, director: Director):
        Scene.__init__(self, director)
        self.title = Text("Main Menu", 400, 200, TEXT_COL)
        start_btn = Button(self, "jugar_btn.png", 500, 300,
                           lambda: self.director.change_scene(GameScene(director)))
        help_btn = Button(self, "ayuda_btn.png", 500,
                          400, lambda: print("Help"))
        config_btn = Button(self, "config_btn.png", 500, 500,
                            lambda: print("Config"))
        self.buttons = [start_btn, help_btn, config_btn]

    def on_update(self):
        pass

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if (button.isHovering(event)):
                    button.action()

    def on_draw(self, screen):
        screen.fill((51, 255, 255))

        self.title.on_draw(screen)

        for button in self.buttons:
            button.on_draw(screen)
