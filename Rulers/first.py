import pygame
from pygame.draw import rect, circle


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


class Lines(Board):
    def __init__(self, width, height, squares=None):
        super().__init__(width, height)
        self.arr = board.list_of_squares
        self.has_red = False
        self.red_coords = []
        self.num_of_moves = 0
        self.number = 1
        self.visited = {}

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)
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

    def on_click(self, cell_xy):
        x, y, x2, y2, color = self.arr[cell_xy[0]][cell_xy[1]]
        if color in [0, 2]:
            if not self.has_red:
                color = 1
                circle(screen, 'blue', (x + ((x2 - x) // 2), (y + ((y2 - y) // 2))), 22)
                # rect(screen, 'blue', (x + 1, y + 1, x2 - x - 2, y2 - y - 2))
                self.arr[cell_xy[0]][cell_xy[1]][-1] = color

            else:
                if self.has_path(cell_xy[0], cell_xy[1]):
                    self.arr[cell_xy[0]][cell_xy[1]][-1] = 1
                    circle(screen, 'blue', (x + ((x2 - x) // 2), (y + ((y2 - y) // 2))), 22)

                    # rect(screen, 'blue', (x + 1, y + 1, x2 - x - 2, y2 - y - 2))
                    if not color:
                        x, y, x2, y2, cell = self.red_coords
                        circle(screen, 'black', (x + ((x2 - x) // 2), (y + ((y2 - y) // 2))), 22)

                        # rect(screen, 'black', (x + 1, y + 1, x2 - x - 2, y2 - y - 2))
                        self.arr[cell[0]][cell[1]][-1] = 0
                    self.has_red = False
                    self.red_coords = []
                    self.visited = {}
        elif color == 1:
            if not self.has_red:
                color = 2
                self.has_red = True
                circle(screen, 'red', (x + ((x2 - x) // 2), (y + ((y2 - y) // 2))), 22)

                # rect(screen, 'red', (x + 1, y + 1, x2 - x - 2, y2 - y - 2))
                self.red_coords = [x, y, x2, y2, cell_xy]
                self.develop(*cell_xy)
                self.arr[cell_xy[0]][cell_xy[1]][-1] = color

    def find_neighbours(self, y_coord, x_coord):
        need = []
        for el in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            first, second = el
            top = 0 <= first + y_coord < height_of_board
            left = 0 <= second + x_coord < width_of_board
            if top and left and self.arr[y_coord + first][x_coord + second][-1] == 0:
                need.append([y_coord + first, x_coord + second])

        return need

    def has_path(self, first, second):
        if (first, second) in self.visited or self.arr[first][second][-1] == 2:
            return True
        return False

    def develop(self, x, y):
        need = self.find_neighbours(x, y)
        for x_2, y_2 in need:
            if (x_2, y_2) not in self.visited:
                self.visited[(x_2, y_2)] = (x, y)
                x, y, *_ = self.arr[x_2][y_2]
                self.develop(x_2, y_2)


size = 800, 800
screen = pygame.display.set_mode(size)

width_of_board = 10
height_of_board = 15
board = Board(width_of_board, height_of_board)
board.set_view(20, 20, 50)
w_h = board.w_h()
board.render(screen)
lines = Lines(w_h[0], w_h[1])

running = True
moving = False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            moving = True
            lines.get_click(event.pos)

    pygame.display.flip()
    a = lines.visited

    # clock.tick(7)
pygame.quit()
