import math
from random import choice
from random import randint as rnd
import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.g = 3
        self.eloss = 0.6
        self.stuck_check = 0

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.vy = self.vy + self.g

        if self.x + self.r >= 800 and self.vx > 0:
            self.vx = -(self.vx * self.eloss)
        if self.y + self.r >= 550 and self.vy > 0:
            self.vx = self.vx * self.eloss
            self.vy = -(self.vy * self.eloss)

        if abs(self.vx) <= 2:
            self.stuck_check += 1
        else:
            self.stuck_check = 0
        if self.stuck_check >= 45:
            self.x = 0
            self.y = 550
            self.vx = self.vy = self.g = self.eloss = 0
            self.r = 0

        self.x += self.vx
        self.y += self.vy

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.r + obj.r)**2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 20
        self.y = 450
        self.w = 20
        self.h = 5

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((self.y - event.pos[1]), (event.pos[0] - self.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
        self.w = 20

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan2((self.y - event.pos[1]), (event.pos[0] - self.x))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.polygon(self.screen, self.color,
                            ((self.x, self.y),
                             (self.x + self.w * math.cos(self.an), self.y - self.w * math.sin(self.an)),
                             ((self.x + self.w * math.cos(self.an) + self.h * math.cos(math.pi / 2 - self.an)),
                             (self.y - self.w * math.sin(self.an) + self.h * math.sin(math.pi / 2 - self.an))),
                             ((self.x + self.h * math.cos(math.pi / 2 - self.an)),
                              (self.y + self.h * math.sin(math.pi / 2 - self.an))),
                             (self.x, self.y)))
        # FIXIT don't know how to do it

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 70:
                self.f2_power += 1
                self.w += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(20, 50)
        self.color = RED
        self.wait = 0

    def new_target(self):
        """ Инициализация новой цели. """
        self.live = 1
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = RED

    def hit(self):
        global points
        """Попадание шарика в цель."""
        screen.fill(WHITE)
        points += 1
        s = 'Заль поражениа за ' + str(bullet) + ' выстрелов'
        f1 = pygame.font.Font(None, 30)
        text1 = f1.render(s, True, BLACK)
        screen.blit(text1, (270, 280))
        pygame.display.update()
        pygame.time.wait(1000)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)


def text():
    global points
    s = 'Счет: ' + str(points)
    f1 = pygame.font.Font(None, 30)
    text1 = f1.render(s, True, BLACK)
    screen.blit(text1, (15, 50))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
my_font = pygame.font.SysFont('Times new roman', 30)
text_surface = my_font.render('Some Text', False, (0, 0, 0))
bullet = 0
points = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
finished = False
text()

while not finished:
    screen.fill(WHITE)
    text()
    gun.draw()
    target.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
            bullet = 0
    gun.power_up()
    screen.blit(text_surface, (0, 0))

pygame.quit()
