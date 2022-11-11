import pygame
import math
from pygame.draw import *

pygame.init()

FPS = 1
screen = pygame.display.set_mode((400, 400))

# rgb-кодировки:
red = (255, 0, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)

# координаты окружностей:
c0 = (200, 200)
cl = (160, 175)
cr = (240, 175)

# рисование:
circle(screen, yellow, c0, 100, 0)

circle(screen, red, cl, 20, 0)
circle(screen, black, cl, 10, 0)

circle(screen, red, cr, 15, 0)
circle(screen, black, cr, 7, 0)
# координаты "бровей":
phi = 3.14 / 2  # угол наклона

rect(screen, black, (150, 250, 100, 20), 0)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
