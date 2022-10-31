import pygame
from director import Director
from utils import draw_text
from utils import draw_text
from scenes.scene import Scene
from config import FONT, TEXT_COL
from buttons import Button

from scenes.game_scene import GameScene


class HomeScene(Scene):
    """ Welcome screen of the game, the first one to be loaded."""

    def __init__(self, director: Director):
        Scene.__init__(self, director)
        start_btn = Button(self, "jugar_btn.png", 750, 600, 0.2,
                           lambda: self.director.change_scene(GameScene(director)))
        help_btn = Button(self, "ayuda_btn.png", 750,
                          800, 0.2, lambda: print("Help"))
        config_btn = Button(self, "config_btn.png", 750, 700, 0.2,
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
        draw_text("Main Menu", FONT, TEXT_COL, 750, 250, screen)

        for button in self.buttons:
            button.on_draw(screen)
