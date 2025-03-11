import pygame

from code.Const import W_HEIGHT


class Background:
    def __init__(self):
        self.image = pygame.image.load('../asset/desert-background-looped.png')
        self.rect1 = self.image.get_rect(topleft=(0, 0))
        self.rect2 = self.image.get_rect(topleft=(0, -W_HEIGHT))

    def move(self):
        self.rect1.y += 3
        self.rect2.y += 3

        if self.rect1.top >= W_HEIGHT:
            self.rect1.top = self.rect2.top - W_HEIGHT
        if self.rect2.top >= W_HEIGHT:
            self.rect2.top = self.rect1.top - W_HEIGHT

    def draw(self, window):
        window.blit(self.image, self.rect1)
        window.blit(self.image, self.rect2)
