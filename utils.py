import pygame
from typing import Tuple

from config import SCREEN_SIZE, BASE_RES


def relative_pos(x: int, y: int) -> Tuple[int, int]:
    proportion = SCREEN_SIZE.getSize()[1]/BASE_RES

    return x * proportion, y*proportion


def draw_text(text, font: pygame.font.Font, text_col, x, y, screen: pygame.Surface):
    img = font.render(text, True, text_col)
    screen.blit(img, relative_pos(x, y))


def scale_image(image: pygame.Surface) -> pygame.Surface:
    proportion = SCREEN_SIZE.getSize()[1]/BASE_RES

    x = image.get_rect().width
    y = image.get_rect().height
    return pygame.transform.scale(image, (x * proportion, y*proportion))
