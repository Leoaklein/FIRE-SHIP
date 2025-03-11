import pygame

from code.Background import Background
from code.Const import W_WIDTH, W_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))
        self.running = True
        pygame.display.set_caption("FIRE SHIP")
        self.background = Background()
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.background.move()
            self.window.fill((0, 0, 0)) #limpa a tela
            self.background.draw(self.window)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()


game = Game()
game.run()

