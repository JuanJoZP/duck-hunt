import pygame
from director import Director
from utils import draw_text
from scene import Scene
from config import FONT, TEXT_COL
from buttons import Button

from scenes.game_scene import GameScene


class HomeScene(Scene):
    """ Welcome screen of the game, the first one to be loaded."""

    def __init__(self, director: Director):
        Scene.__init__(self, director)
        start_btn = Button(750, 600,  pygame.image.load(
            "img/jugar_btn.png").convert_alpha(), lambda: self.director.change_scene(GameScene(dir)))
        help_btn = Button(750, 800, pygame.image.load(
            "img/ayuda_btn.png").convert_alpha(), lambda: print("Help"))
        config_btn = Button(750, 700, pygame.image.load(
            "img/configuracion_btn.png").convert_alpha(), lambda: print("Config"))
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
            button.draw_button(screen)
