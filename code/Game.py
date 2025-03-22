import pygame

from code.Background import Background
from code.Const import W_WIDTH, W_HEIGHT
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()  # start pygame
        self.window = pygame.display.set_mode((W_WIDTH, W_HEIGHT))  # Screen Size
        self.running = True
        pygame.display.set_caption("SHIP COIN")  #Window title
        self.background = Background()
        self.menu = Menu(self.window)
        self.level = Level(self.window)

    def run(self):
        while self.running:
            menu_return = self.menu.run()

            if menu_return == 0:  # Start Game
                self.level.reset()  # cleaning the level
                self.level.run()  # Start Level

            # Check for closed events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
