import pygame
from director import Director
from scenes.home_scene import HomeScene


def main():
    dir = Director()
    scene = HomeScene(dir)
    dir.change_scene(scene)
    dir.loop()


if __name__ == '__main__':
    pygame.init()
    main()
