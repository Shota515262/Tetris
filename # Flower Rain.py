# Rose Rain
import pygame
import random
import math
import sys
from pygame import gfxdraw

pygame.init()

WIDTH = 1280
HEIGH = 720

SCREEN = pygame.display.set_mode((WIDTH, HEIGH))
pygame,display.set_cation("Rpse Rain")

clock = pygame.time.Clock()

BACKGROUND = (5, 5, 15)

COLORS = [
    (255, 60, 80),
    (255, 100, 120),
    (255, 120, 180),
    (180, 80, 255),
    (120, 120, 255)
]


class Rose:

    def __init__(self):
        self.reset()

    def reset(self):

        self.x = random.randint(0, WIDTH)

        self.y = random.randint(-HEIGHT, -50)

        self.size = random.uniform(0.6, 2)

        self.color = random.choice(COLORS)

        self.petal_count = random.randint(5, 8)

        self.angle = random.uniform(0, math.pi)

        self.rotation_speed = random.uniform(-0.02, 0.02)

        self.fall_speed = random.uniform(0.5, 1.8)

        self.swing = random.uniform(0, 6.28)

        self.swing_speed = random.uniform(0.01, 0.03)

    def update(self):

        self.y += self.fall_speed

        self.angle += self.rotation_speed

        self.swing += self.swing_speed

        self.offset = math.sin(self.swing) * 20

        if self.y > HEIGHT + 50:
            self.reset()

    def draw(self, surface):

        cx = int(self.x + self.offset)

        cy = int(self.y)

        for i in range(self.petal_count):

            angle = self.angle + (
                i * 2 * math.pi / self.petal_count
            )

            length = 12 * self.size

            points = []

            for t in range(21):

                t /= 20

                x = (
                    cx
                    + length
                    * math.cos(angle)
                    * math.sin(math.pi * t)
                )

                y = (
                    cy
                    + length
                    * math.sin(angle)
                    * math.sin(math.pi * t)
                )

                points.append((x, y))

            if len(points) > 2:

                gfxdraw.filled_polygon(
                    surface,
                    points,
                    self.color
                )

                gfxdraw.aapolygon(
                    surface,
                    points,
                    self.color
                )

        gfxdraw.filled_circle(
            surface,
            cx,
            cy,
            int(3 * self.size),
            (240, 220, 50)
        )


ROSE_COUNT = 800

roses = [
    Rose()
    for _ in range(ROSE_COUNT)
]

overlay = pygame.Surface(
    (WIDTH, HEIGHT),
    pygame.SRCALPHA
)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if (
            event.type
            == pygame.KEYDOWN
            and event.key
            == pygame.K_ESCAPE
        ):
            running = False

    overlay.fill((5, 5, 15, 30))

    screen.blit(
        overlay,
        (0, 0)
    )

    for rose in roses:

        rose.update()

        rose.draw(screen)

    fps = pygame.font.SysFont(
        None,
        24
    )

    text = fps.render(
        f"FPS {int(clock.get_fps())}",
        True,
        (255, 255, 255)
    )

    screen.blit(
        text,
        (10, 10)
    )

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
                