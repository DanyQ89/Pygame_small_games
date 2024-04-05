import pygame
from pygame.draw import circle

if __name__ == '__main__':
    pygame.init()
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    screen.fill('black')
    running = True
    v = 40
    fps = 240
    position = None
    clock = pygame.time.Clock()
    circle(screen, 'red', (width // 2, height // 2), 20)
    x_circle = width // 2
    y_circle = height // 2
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                position = event.pos

        if position:
            num = v / fps
            if abs(position[0] - x_circle) > 1 or abs(position[1] - y_circle) > 1:
                if abs(x_circle - position[0]) > num:
                    if x_circle < position[0]:
                        x_circle += num
                    else:
                        x_circle -= num
                if abs(y_circle - position[1]) > num:
                    if y_circle < position[1]:
                        y_circle += num
                    else:
                        y_circle -= num
                screen.fill('black')
                circle(screen, 'red', (x_circle, y_circle), 20)
            clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
