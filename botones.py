import pygame
from director import screen

#load buttons images
start_img = pygame.image.load("btns/btn_jugar.png").convert_alpha()
help_img = pygame.image.load("btns/btn_ayuda.png").convert_alpha()
configuration_img = pygame.image.load("btns/btn_configuracion.png").convert_alpha()

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
#create buttons instances
start_btn = Button(100, 200, start_img)
help_btn = Button(450, 200, help_img)
configuration_btn = Button(304, 125, configuration_img)
