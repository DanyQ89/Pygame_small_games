import pygame
from pygame import draw

if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    running = True
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()
    v = 300
    fps = 120
    position = None
    list_pos = []


    def func(x, y, left_right, up_down, numb):
        if numb + 10 >= x:
            left_right = '+'
        elif 500 - numb - 10 <= x:
            left_right = '-'
        if numb + 10 >= y:
            up_down = '+'
        elif 500 - numb - 10 <= y:
            up_down = '-'

        if left_right == '+':
            x += numb
        else:
            x -= numb
        if up_down == '+':
            y += numb
        else:
            y -= numb

        return x, y, left_right, up_down


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                list_pos.append((position[0], position[1], '-', '-'))
                draw.circle(screen, 'white', tuple(map(int, position)), 10)

        screen.fill('black')
        for i in range(len(list_pos)):
            num = v / fps
            list_pos[i] = func(*list_pos[i], num)
            draw.circle(screen, 'white', list_pos[i][:-2], 10)

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
