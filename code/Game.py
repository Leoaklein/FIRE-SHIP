import pygame

from code.Background import Background
from code.Const import W_WIDTH, W_HEIGHT
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))
        self.running = True
        pygame.display.set_caption("FIRE SHIP")
        self.background = Background()
        self.level = Level(self.window)


    def run(self):
        while self.running:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == 0:
                self.level.run()
                #implementar as outras opções de menu
            elif menu_return == 1:
                pass
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()




game = Game()
game.run()

