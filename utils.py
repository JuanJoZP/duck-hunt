import pygame

from config import SCREEN_SIZE


def draw_text(text, font, text_col, x, y, screen):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def scale_image(image: pygame.Surface, zoom: int) -> pygame.Surface:
    x, y = SCREEN_SIZE.getSize()
    return pygame.transform.scale(image, (x * zoom, y*zoom))
