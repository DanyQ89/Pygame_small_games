from copy import deepcopy

import pygame
from pygame.draw import rect


class Board:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.list_of_squares = []
        self.left = 10
        self.top = 10
        self.cell_size = 20

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
                need.append([x, y, x + w, y + h, 0])
                rect(screen_class, 'white', (x, y, w, h), width=1)
                x += w
            self.list_of_squares.append(need)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)
        return cell

    def get_cell(self, pos):
        for i in range(len(self.list_of_squares)):
            for g in range(len(self.list_of_squares[i])):
                el = self.list_of_squares[i][g]
                x, y, x2, y2, alive = el
                if x <= pos[0] <= x2 and y <= pos[1] <= y2:
                    return i, g
        return None

    def w_h(self):
        return self.width, self.height

    def on_click(self, class_cell):
        if not class_cell:
            return
        x_coord, y_coord = list(class_cell)
        x, y, x2, y2, alive = self.list_of_squares[x_coord][y_coord]
        if not alive:
            alive = 1
        else:
            alive = 0
        rect(screen, 'green' if alive else 'black', (x + 1, y + 1, x2 - x - 2, y2 - y - 2))
        self.list_of_squares[x_coord][y_coord] = [x, y, x2, y2, alive]

    def get_list(self):
        return self.list_of_squares


class Life(Board):
    def __init__(self, width, height, squares=None):
        super().__init__(width, height)
        self.arr = None
        self.arr_2 = None

    @staticmethod
    def count_neighbors(y_coord, x_coord, arr):
        counter = 0
        for i in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
            first, second = i
            left = x_coord + second < n
            top = y_coord + first < n
            if left and top:
                counter += arr[y_coord + first][x_coord + second][-1]
            else:
                if not left and not top:
                    counter += arr[first][second][-1]
                elif not left and top:
                    counter += arr[y_coord + first][n - second - x_coord][-1]
                elif left and not top:
                    counter += arr[n - first - y_coord][x_coord + second][-1]

        return counter

    def next_move(self, squares):
        third = squares if not self.arr else self.arr
        self.arr_2 = deepcopy(third)
        for i in range(self.height):
            for j in range(self.width):
                neighbors = self.count_neighbors(i, j, third)
                x, y, x2, y2, alive = third[i][j]
                if alive and (neighbors < 2 or neighbors > 3):
                    alive = 0
                elif not alive and neighbors == 3:
                    alive = 1
                if alive:
                    color = 'green'
                else:
                    color = 'black'
                rect(screen, color, (x + 1, y + 1, x2 - x - 2, y2 - y - 2))
                self.arr_2[i][j][-1] = alive
        self.arr = self.arr_2

    def change(self, x, y):
        if self.arr:
            item = self.arr[x][y][-1]
            if item:
                self.arr[x][y][-1] = 0
            else:
                self.arr[x][y][-1] = 1


size = 800, 800
screen = pygame.display.set_mode(size)
n = 30
board = Board(n, n)
w_h = board.w_h()
life = Life(w_h[0], w_h[1])
running = True
living = False
clock = pygame.time.Clock()
v = 100
num_of_v = 5
board.render(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            a = board.get_click(event.pos)
            life.change(a[0], a[1])

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or (
                event.type == pygame.MOUSEBUTTONDOWN and event.button == 3):
            living = not living
        if event.type == pygame.MOUSEWHEEL:
            if (v > num_of_v and event.y == -1) or (event.y == 1 and v < num_of_v * 20):
                v += event.y * num_of_v
    if living:
        life.next_move(board.get_list())
    pygame.display.flip()
    clock.tick(v)
pygame.quit()
