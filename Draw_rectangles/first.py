import pygame
from pygame.draw import rect

if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    screen2 = pygame.Surface(screen.get_size())
    running = True
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()
    v = 300
    fps = 120
    position = None
    drawing = False
    w = 0
    h = 0
    position_list = []
    while running:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                drawing = True
            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    rel = event.rel
                    w += rel[0]
                    h += rel[1]
            elif event.type == pygame.MOUSEBUTTONUP:
                screen2.blit(screen, (0, 0))
                position_list.append([position[0], position[1], w, h])
                position, w, h = None, 0, 0
                drawing = False
            elif keys[pygame.K_LCTRL] and keys[pygame.K_z]:
                if position_list:
                    position_list.pop()
                    screen.fill('black')
                    screen2.fill('black')
                    for i in position_list:
                        rect(screen2, 'white', i, width=1)

        screen.fill('black')
        screen.blit(screen2, (0, 0))
        if position and drawing:
            rect(screen, 'white', (position[0], position[1], w, h), width=1)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
