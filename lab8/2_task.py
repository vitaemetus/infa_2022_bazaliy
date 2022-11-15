import pygame
from pygame.draw import *
from random import randint
pygame.init()

# Цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# Конфигурация окна pygame
FPS = 30
screen = pygame.display.set_mode((1200, 900))
clock = pygame.time.Clock()

# Конфигурация шариков в начале игры
number_of_objects = 6
r = [[], []]
x = [[], []]
y = [[], []]
Vx = [[], []]
Vy = [[], []]
color = [[], []]

for i in range(number_of_objects):
    r[0].append(randint(20, 60))
    x[0].append(randint(r[0][i] + 1, 1200 - (r[0][i] + 1)))
    y[0].append(randint(r[0][i] + 1, 900 - (r[0][i] + 1)))
    Vx[0].append(randint(5, 10))
    Vy[0].append(randint(5, 10))
    color[0].append(COLORS[randint(0, 5)])
    circle(screen, color[0][i], (x[0][i], y[0][i]), r[0][i])

for i in range(number_of_objects):
    r[1].append(randint(20, 60))
    x[1].append(randint(r[1][i] + 1, 1200 - (r[1][i] + 20)))
    y[1].append(randint(r[1][i] + 1, 900 - (r[1][i] + 20)))
    Vx[1].append(randint(5, 10))
    Vy[1].append(randint(5, 10))
    color[1].append(COLORS[randint(0, 5)])
    polygon(screen, color[1][i], ((x[1][i], y[1][i]),
                                  (x[1][i] + 2*r[1][i], y[1][i]),
                                  (x[1][i] + 2*r[1][i], y[1][i] + 2*r[1][i]),
                                  (x[1][i], y[1][i] + 2*r[1][i]),
                                  (x[1][i], y[1][i])))

finished = False
points = 0

while not finished:
    for event in pygame.event.get():
        # Обработка события выхода из игры, вывод количества набранных очков
        if event.type == pygame.QUIT:
            finished = True
            print("Ваши очки:", points)
        # Обработка нажатия кнопки мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Проверка по каждому из шариков
            for i in range(number_of_objects):
                # Проверка попадания
                if (event.pos[0] - x[0][i])**2 + (event.pos[1] - y[0][i])**2 <= r[0][i]**2:
                    # +1 к счетчику очков, создаем новый шарик вместо того, на который мы нажали
                    print('Circle!')
                    points += 2
                    circle(screen, BLACK, (x[0][i], y[0][i]), r[0][i])
                    r[0][i] = randint(20, 60)
                    x[0][i] = randint(r[0][i] + 1, 1200 - (r[0][i] + 1))
                    y[0][i] = randint(r[0][i] + 1, 900 - (r[0][i] + 1))
                    Vx[0][i] = randint(5, 10)
                    Vy[0][i] = randint(5, 10)
                    color[0][i] = COLORS[randint(0, 5)]
                    circle(screen, color[0][i], (x[0][i], y[0][i]), r[0][i])
                    continue

            for i in range(number_of_objects):
                # "Произошло ли нажатие в границах шарика?"
                if x[1][i] <= event.pos[0] <= x[1][i] + 2*r[1][i] and y[1][i] <= event.pos[1] <= y[1][i] + 2*r[1][i]:
                    # +1 к счетчику очков, создаем новый шарик вместо того, на который мы нажали
                    print('Square!')
                    points += 1
                    polygon(screen, BLACK, ((x[1][i], y[1][i]),
                                            (x[1][i] + 2 * r[1][i], y[1][i]),
                                            (x[1][i] + 2 * r[1][i], y[1][i] + 2 * r[1][i]),
                                            (x[1][i], y[1][i] + 2 * r[1][i]),
                                            (x[1][i], y[1][i])))
                    r[1][i] = randint(20, 60)
                    x[1][i] = randint(r[1][i] + 1, 1200 - (r[1][i] + 20))
                    y[1][i] = randint(r[1][i] + 1, 900 - (r[1][i] + 20))
                    Vx[1][i] = randint(5, 10)
                    Vy[1][i] = randint(5, 10)
                    color[1][i] = COLORS[randint(0, 5)]
                    polygon(screen, color[1][i], ((x[1][i], y[1][i]),
                                                  (x[1][i] + 2 * r[1][i], y[1][i]),
                                                  (x[1][i] + 2 * r[1][i], y[1][i] + 2 * r[1][i]),
                                                  (x[1][i], y[1][i] + 2 * r[1][i]),
                                                  (x[1][i], y[1][i])))
                    continue

    # Анимация шариков
    for i in range(number_of_objects):
        # Закрашиваем старый шарик черным цветом
        circle(screen, BLACK, (x[0][i], y[0][i]), r[0][i])
        # Проверяем, не находится ли шарик на границе окна по горизонтальной оси
        if x[0][i] + r[0][i] >= 1200 or x[0][i] - r[0][i] <= 0:
            # Если шарик на границе, происходит упругий удар, и шарик меняет направление движения
            Vx[0][i] = -Vx[0][i]
        # То же самое для вертикальной оси
        if y[0][i] + r[0][i] >= 900 or y[0][i] - r[0][i] <= 0:
            Vy[0][i] = -Vy[0][i]
        # Смещение шарика в соответствии со скоростью
        x[0][i] += Vx[0][i]
        y[0][i] += Vy[0][i]
        circle(screen, color[0][i], (x[0][i], y[0][i]), r[0][i])
    # Анимация прямоугольников
    for i in range(number_of_objects):
        polygon(screen, BLACK, ((x[1][i], y[1][i]),
                                (x[1][i] + 2 * r[1][i], y[1][i]),
                                (x[1][i] + 2 * r[1][i], y[1][i] + 2 * r[1][i]),
                                (x[1][i], y[1][i] + 2 * r[1][i]),
                                (x[1][i], y[1][i])))
        if x[1][i] + 2 * r[1][i] >= 1200 or x[1][i] <= 0:
            Vx[1][i] = -Vx[1][i]
        if y[1][i] + 2 * r[1][i] >= 900 or y[1][i] <= 0:
            Vy[1][i] = -Vy[1][i]
        x[1][i] += Vx[1][i]
        y[1][i] += Vy[1][i]
        polygon(screen, color[1][i], ((x[1][i], y[1][i]),
                                      (x[1][i] + 2 * r[1][i], y[1][i]),
                                      (x[1][i] + 2 * r[1][i], y[1][i] + 2 * r[1][i]),
                                      (x[1][i], y[1][i] + 2 * r[1][i]),
                                      (x[1][i], y[1][i])))
    pygame.display.update()
    clock.tick(FPS)
