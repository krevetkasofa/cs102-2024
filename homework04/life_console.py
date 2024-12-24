"""Creating interface of console"""

import curses
import time

from life import GameOfLife
from ui import UI


class Console(UI):
    """Creating console"""

    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        screen.border(0)

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        h, w = screen.getmaxyx()  # Получаем размеры экрана
        for row_index, row in enumerate(self.life.curr_generation):
            for col_index, cell_value in enumerate(row):
                if 0 < row_index < h - 1 and 0 < col_index < w - 1:
                    char_to_draw = " "  # По умолчанию пустое пространство
                    if cell_value == 1:
                        char_to_draw = "1"  # Если клетка живая, отображаем "1"
                    screen.addch(row_index, col_index, char_to_draw)  # Рисуем клетку

    def run(self) -> None:
        screen = curses.initscr()
        curses.curs_set(0)
        screen.timeout(100)
        screen.nodelay(True)

        while True:
            screen.clear()
            self.draw_borders(screen)
            self.draw_grid(screen)
            screen.refresh()
            self.life.step()

            key = screen.getch()
            if key == ord("a"):
                break

        curses.endwin()


if __name__ == "__main__":
    life_game = GameOfLife((20, 20), max_generations=100)
    ui = Console(life_game)
    ui.run()
