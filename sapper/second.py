import random

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

    def w_h(self):
        return self.width, self.height

    def get_list(self):
        return self.list_of_squares


class Minesweeper(Board):
    def __init__(self, width, height, squares=None):
        super().__init__(width, height)
        self.arr = []

    def set_mines(self, arr):
        self.arr = arr
        for i in range(len(arr)):
            for g in range(len(arr[i])):
                num = random.randint(0, 10)
                if num == 10:
                    arr[i][g][-1] = 10
                    x, y, x2, y2, color = arr[i][g]
                    rect(screen, 'red', (x + 1, y + 1, x2 - x - 2, y2 - y - 2))
                else:
                    arr[i][g][-1] = -1
        for i in range(len(arr)):
            for g in range(len(arr[i])):
                if self.arr[i][g][-1] != 10:
                    n = self.count_neighbors(i, g)[0]
                    self.arr[i][g][-1] = n

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.open_cell(cell)
            return cell

    def get_cell(self, pos):
        for i in range(len(self.arr)):
            for g in range(len(self.arr[i])):
                el = self.arr[i][g]
                x, y, x2, y2, num = el
                if x <= pos[0] <= x2 and y <= pos[1] <= y2 and num != 10:
                    return i, g
        return None

    def w_h(self):
        return self.width, self.height

    def open_cell(self, class_cell):
        i, g = class_cell
        num, list_of_neighbours = self.count_neighbors(i, g)
        x, y, x2, y2, num = self.arr[i][g]
        if type(num) is int:
            if num or num == 0:
                font = pygame.font.Font(None, 35)
                text = font.render(str(num), True, 'green')
                screen.blit(text, (x + 4, y + 4))
                self.arr[i][g][-1] = str(num)

        if num == 0 and list_of_neighbours:
            for i in list_of_neighbours:
                self.open_cell(i)

    def count_neighbors(self, y_coord, x_coord):
        counter = 0
        n_list = []
        list_need = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        for i in list_need:
            first, second = i
            left = 0 <= x_coord + second < width_of_board
            top = 0 <= y_coord + first < height_of_board
            if left and top:
                number = self.arr[y_coord + first][x_coord + second][-1]
                if number == 10:
                    counter += 1

                n_list.append([y_coord + first, x_coord + second])
        return counter, n_list


size = 800, 800
screen = pygame.display.set_mode(size)

width_of_board = 10
height_of_board = 15
board = Board(width_of_board, height_of_board)
board.set_view(20, 20, 50)
w_h = board.w_h()
minesweeper = Minesweeper(w_h[0], w_h[1])

board.render(screen)
list_of_squares = board.get_list()
minesweeper.set_mines(list_of_squares)
running = True
moving = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            moving = True
            minesweeper.get_click(event.pos)

    pygame.display.flip()
pygame.quit()
