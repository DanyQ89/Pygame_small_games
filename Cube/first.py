import pygame
from pygame import Color
from pygame.draw import rect, polygon

w, hue = list(map(str, input().split()))
# w, hue = ['64', '0']
if not w.isnumeric() or not hue.isnumeric() or '.' in w + hue:
    print('Неправильный ввод')
else:
    w = int(w)
    hue = int(hue)
    if (w % 4 != 0 or w > 100) or (not 0 <= hue <= 360):
        print('Неправильный ввод')
    else:
        side = w
        half_side = w // 2
        pygame.init()
        pygame.display.set_caption('Куб')
        size = 300, 300
        middle_point_x, middle_point_y = ((300 - half_side) // 2, (300 - half_side) // 2)
        screen = pygame.display.set_mode(size)
        screen.fill('black')
        color = Color(178, 0, 0)
        hsv = color.hsva

        color.hsva = (hue, hsv[1], 75, hsv[3])
        rect(screen, color, (middle_point_x - side // 2, middle_point_x, side, side))
        color.hsva = (hue, hsv[1], 100, hsv[3])
        polygon(screen, color,
                ((middle_point_x - half_side, middle_point_y), (middle_point_x, middle_point_y - half_side),
                 (middle_point_x + side, middle_point_y - half_side), (middle_point_x + half_side, middle_point_y)))
        color.hsva = (hue, hsv[1], 50, hsv[3])
        polygon(screen, color, (
            (middle_point_x + half_side, middle_point_y), (middle_point_y + side, middle_point_y - half_side),
            (middle_point_x + side, middle_point_y + half_side),
            (middle_point_x + half_side, middle_point_y + side)))
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
