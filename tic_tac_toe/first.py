import pygame
from pygame.draw import rect, polygon, circle


class Board:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.list_of_squares = []
        self.list_of_colors = ['black', 'blue', 'red']
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.move = 1

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen_class):
        x = self.left
        y = self.top
        w, h = self.cell_size, self.cell_size
        for i in range(len(self.board)):
            x = self.left
            if i:
                y += h
            need = []
            for g in range(len(self.board[i])):
                need.append([x, y, x + w, y + h, None])
                rect(screen_class, 'white', (x, y, w, h), width=1)
                x += w
            self.list_of_squares.append(need)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, pos):
        for i in range(len(self.list_of_squares)):
            for g in range(len(self.list_of_squares[i])):
                el = self.list_of_squares[i][g]
                x, y, x2, y2, color = el
                if x <= pos[0] <= x2 and y <= pos[1] <= y2:
                    return i, g
        return None

    def change_move(self):
        if self.move == 1:
            self.move = 2
        else:
            self.move = 1

    def on_click(self, class_cell):
        if not class_cell:
            return
        x_coord, y_coord = list(class_cell)
        x, y, x2, y2, shape = self.list_of_squares[x_coord][y_coord]
        if not shape:
            if self.move == 1:
                polygon(screen, 'blue', ((x + 2, y + 2), (x2 - 2, y2 - 2)), width=2)
                polygon(screen, 'blue', ((x + 2, y2 - 2), (x2 - 2, y + 2)), width=2)
            else:
                circle(screen, 'red', (x + ((x2 - x) // 2), y + ((y2 - y) // 2)), 13, width=2)
            self.change_move()
        self.list_of_squares[x_coord][y_coord] = [x, y, x2, y2, '.']


size = 400, 400
screen = pygame.display.set_mode(size)
board = Board(10, 7)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)

    board.render(screen)
    pygame.display.flip()
pygame.quit()
