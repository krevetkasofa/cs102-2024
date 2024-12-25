"""GameOfLife GUI version"""

import pygame
from pygame.locals import *

from life import GameOfLife
from ui import UI


class GUI(UI):
    """The Game of Life"""

    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.speed = speed
        self.cell_size = cell_size
        self.cell_width = self.life.cols
        self.cell_height = self.life.rows
        self.width = self.cell_size * self.cell_width
        self.height = self.cell_size * self.cell_height
        self.screen_size = self.width, self.height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.grid = self.life.curr_generation

        self.button = pygame.Rect(0, 0, 150, 50)
        pygame.font.init()
        self.font = pygame.font.Font(None, 30)

        self.status = False

    def draw_lines(self) -> None:
        """Draw the grid"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        """Draw the cells"""
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                x, y = j * self.cell_size + 1, i * self.cell_size + 1
                rect_cor = (x, y, self.cell_size - 1, self.cell_size - 1)
                color = "blue" if self.life.curr_generation[i][j] == 1 else "white"
                pygame.draw.rect(self.screen, color, rect_cor)

    def run(self) -> None:
        """Draw the buttons and Run the game"""
        pygame.init()  # pylint: disable=no-member
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:  # pylint: disable=no-member
                    mouse_pos = event.pos
                    pos_x = mouse_pos[1] // self.cell_size
                    pos_y = mouse_pos[0] // self.cell_size
                    if self.life.curr_generation[pos_x][pos_y] == 1:
                        self.life.curr_generation[pos_x][pos_y] = 0
                    else:
                        self.life.curr_generation[pos_x][pos_y] = 1
                    self.draw_grid()
                    self.draw_lines()
                    if self.button.collidepoint(mouse_pos) and self.status is False:
                        self.status = True
                    elif self.button.collidepoint(mouse_pos) and self.status is True:
                        self.status = False

            if self.status is False:
                self.draw_grid()
                self.life.curr_generation = self.life.get_next_generation()
                button_color = "light gray"
                button_text = "pause"
            else:
                button_color = "dark gray"
                button_text = "resume"

            pygame.draw.rect(self.screen, pygame.Color(button_color), self.button, border_radius=10)
            button_display_text = self.font.render(button_text, True, pygame.Color("black"))
            self.screen.blit(button_display_text, (35, 13))

            pygame.display.flip()
            clock.tick(self.speed)

        pygame.quit()  # pylint: disable=no-member


if __name__ == "__main__":
    game_of_life = GameOfLife(size=(50, 50), randomize=True, max_generations=20)
    ui = GUI(game_of_life, cell_size=15, speed=1)
    ui.run()
