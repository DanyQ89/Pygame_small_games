import math

import pygame
from pygame.draw import circle, polygon

if __name__ == '__main__':
    pygame.init()
    size = width, height = 201, 201
    screen = pygame.display.set_mode(size)
    screen2 = pygame.Surface(size, pygame.SRCALPHA)
    white = 'white'
    running = True
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()
    tr_a = 0
    rotation = 0
    v = 300
    fps = 120
    a = b = 70
    angle = 0.5235987755982988
    osnovanie = math.sqrt((a ** 2 + b ** 2) - (2 * a * b * math.cos(angle)))

    coords = [[(101, 101), (101 + osnovanie / 2, 101 - a), (101 - osnovanie / 2, 101 - a)],
              [(101, 101), (171, 121), ((101 + osnovanie / 2) + 35, 150)],
              [(101, 101), (101 - 70, 121), ((101 - osnovanie / 2) - 35, 150)]]

    color = pygame.Color('white')

    polygon(screen2, white, coords[0])
    polygon(screen2, white, coords[1])
    polygon(screen2, white, coords[2])

    circle(screen, white, (100.5, 100.5), 10)

    screen.blit(screen2, (0, 0))
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    tr_a -= 10
                elif event.button == 3:
                    tr_a += 10

        rotation += tr_a
        screen3 = pygame.transform.rotate(screen2, rotation)
        recta = screen3.get_rect()
        recta.center = (100.5, 100.5)
        screen.fill('black')
        screen.blit(screen3, recta)

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
