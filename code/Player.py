import pygame

from code.Const import W_WIDTH, W_HEIGHT


class Player:
    def __init__(self):
        self.image = pygame.image.load('../asset/ship.png')
        self.rect = self.image.get_rect(topleft=(W_WIDTH/2, W_HEIGHT -30))
    def draw(self, window):
        window.blit(self.image, self.rect)

    def move(self):
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_UP] and self.rect.top > 5:
                self.rect.centery -= 10
            if pressed_key[pygame.K_DOWN] and self.rect.bottom < W_HEIGHT -5:
                self.rect.centery += 10
            if pressed_key[pygame.K_LEFT] and self.rect.left > 5:
                self.rect.centerx -= 10
            if pressed_key[pygame.K_RIGHT] and self.rect.right < W_WIDTH-5:
                self.rect.centerx += 10
            pass
