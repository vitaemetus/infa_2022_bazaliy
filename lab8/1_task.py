import pygame
from pygame.draw import circle
from pygame.draw import polygon

pygame.init()


FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((125, 125, 125))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

pygame.draw.circle(screen, YELLOW, (200, 200), 145)
pygame.draw.circle(screen, BLACK, (200, 200), 150, 5)
pygame.draw.circle(screen, PINK, (140, 160), 25, 10)
pygame.draw.circle(screen, PINK, (260, 160), 25, 15)
pygame.draw.circle(screen, BLACK, (140, 160), 15)
pygame.draw.circle(screen, BLACK, (260, 160), 10)
pygame.draw.polygon(screen, LIGHT_BLUE, [[140, 270], [260, 270], [260, 280], [140, 280]])
pygame.draw.polygon(screen, BLACK, [[180, 160], [180, 150], [100, 90], [100, 100]])
pygame.draw.polygon(screen, BLACK, [[220, 160], [220, 150], [310, 80], [320, 80]])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()