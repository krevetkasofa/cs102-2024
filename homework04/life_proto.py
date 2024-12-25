"""Creating prototype of game"""

import random
import typing as tp
from pprint import pprint as pp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

        self.grid = self.create_grid(randomize=True)

    def draw_lines(self) -> None:
        """Отрисовать сетку"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        """Запустить игру"""
        pygame.init()  # pylint: disable=no-member
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_lines()
            self.draw_grid()
            self.draw_lines()
            self.grid = self.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)

        pygame.quit()  # pylint: disable=no-member

    def create_grid(self, randomize: bool = False) -> Grid:
        """
        Создание списка клеток.

        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """
        grid = [[0] * self.cell_width for _ in range(self.cell_height)]
        if randomize:
            for i, row in enumerate(grid):
                for j, _ in enumerate(row):
                    grid[i][j] = random.randint(0, 1)
        return grid

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for i, row in enumerate(self.grid):
            for j, val in enumerate(row):
                if val == 1:
                    for x in range(i * self.cell_size, (i + 1) * self.cell_size):
                        pygame.draw.line(
                            self.screen, pygame.Color("blue"), (j * self.cell_size, x), ((j + 1) * self.cell_size, x)
                        )
                else:
                    for x in range(i * self.cell_size, (i + 1) * self.cell_size + 1):
                        pygame.draw.line(
                            self.screen, pygame.Color("white"), (j * self.cell_size, x), ((j + 1) * self.cell_size, x)
                        )

    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Вернуть список соседних клеток для клетки `cell`.

        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.

        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.

        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """
        neighbours = []
        row, col = cell
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < self.cell_height and 0 <= j < self.cell_width and (row, col) != (i, j):
                    neighbours.append(self.grid[i][j])

        return neighbours

    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        next_generation = self.create_grid()
        for row_index in range(len(next_generation)):
            for col_index in range(len(next_generation[row_index])):
                neighbors = self.get_neighbours((row_index, col_index))
                alive_neighbors_count = sum(neighbors)
                current_cell = self.grid[row_index][col_index]

                if current_cell == 1:
                    next_generation[row_index][col_index] = 1 if alive_neighbors_count in (2, 3) else 0
                else:
                    next_generation[row_index][col_index] = 1 if alive_neighbors_count == 3 else 0

        return next_generation


if __name__ == "__main__":
    game = GameOfLife(500, 500, 10)
    game.run()
