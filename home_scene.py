from director import Director
from utils import draw_text
from scene import Scene
from config import FONT, TEXT_COL
from botones import Button
import pygame

start_img = pygame.image.load("btns/btn_jugar.png").convert_alpha()
help_img = pygame.image.load("btns/btn_ayuda.png").convert_alpha()
configuration_img = pygame.image.load("btns/btn_configuracion.png").convert_alpha()

start_btn = Button(100, 200, start_img)
help_btn = Button(450, 200, help_img)
configuration_btn = Button(304, 125, configuration_img)

class HomeScene(Scene):
    """ Welcome screen of the game, the first one to be loaded."""

    def __init__(self, director: Director):
        Scene.__init__(self, director)

    def on_update(self):
        pass

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
    
    def on_draw(self, screen):
        screen.fill((51, 255, 255))
        draw_text("Press SPACE to pause.", FONT, TEXT_COL, 160, 250)
        start_btn.draw_button(screen)
        help_btn.draw_button(screen)
        configuration_btn.draw_button(screen)
