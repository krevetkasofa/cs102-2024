"""Business logic of the game LIFE"""
import pathlib
import random
import typing as tp
import pygame


Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

        self.size = size

    def create_grid(self, randomize: bool = False) -> Grid:
        """
        Creating grid
        """
        grid = [[0] * self.cols for _ in range(self.rows)]
        if randomize:
            for i, row in enumerate(grid):
                for j, _ in enumerate(row):
                    grid[i][j] = random.randint(0, 1)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Get neighbours
        """
        neighbors_cells = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        grid_of_neighbours = []
        x, y = cell
        for i, j in neighbors_cells:
            cur_x, cur_y = x + i, y + j
            if 0 <= cur_x < len(self.curr_generation) and 0 <= cur_y < len(self.curr_generation[0]):
                grid_of_neighbours.append(self.curr_generation[cur_x][cur_y])
        return grid_of_neighbours

    def get_next_generation(self) -> Grid:
        """
        Get next generation
        """
        next_generation = self.create_grid()
        for i, row in enumerate(next_generation):
            for j, _ in enumerate(row):
                neighbours = self.get_neighbours((i, j))
                sum_neigh = sum(neighbours)
                if self.curr_generation[i][j] == 1:
                    if sum_neigh == 2 or sum_neigh == 3:
                        next_generation[i][j] = 1
                    else:
                        next_generation[i][j] = 0
                else:
                    if sum_neigh == 3:
                        next_generation[i][j] = 1
        return next_generation

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        if not self.is_max_generations_exceeded and self.is_changing:
            self.prev_generation = self.curr_generation
            self.curr_generation = self.get_next_generation()
            self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.max_generations is not None and self.generations >= self.max_generations

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.prev_generation != self.curr_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            grid = [[int(cell) for cell in line.strip()] for line in lines]

        game_instance = GameOfLife((len(grid), len(grid[0])))
        game_instance.curr_generation = [row for row in grid if row]
        return game_instance


def save(self, filename: pathlib.Path) -> None:
    """
    Сохранить текущее состояние клеток в указанный файл.
    """
    try:
        with open(filename, "w") as f:
            for row in self.curr_generation:
                f.write(" ".join(str(val) for val in row) + "\n")
    except Exception as e:
        print("Ошибка при сохранении файла:", e)
