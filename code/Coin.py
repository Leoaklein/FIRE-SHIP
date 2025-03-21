import random

import pygame

from code.Const import W_WIDTH


class Coin:
    def __init__(self):
        self.frames = [
            pygame.image.load(f'../asset/coin_rot_anim{i}.png') for i in range(6)
        ]
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(center=(random.randint(0, W_WIDTH),random.randint(-100, -20)))
        self.animation_speed = 10  # Velocidade da animação
        self.counter = 0  # Contador para trocar de frame

    def update(self):
        """ Atualiza a animação da moeda. """
        self.counter += 1
        self.rect.centery += 20
        if self.counter >= self.animation_speed:
            self.counter = 0
            self.index = (self.index + 1) % len(self.frames)  # Alterna os frames
            self.image = self.frames[self.index]


    def draw(self, window):
        """ Desenha a moeda na tela. """
        window.blit(self.image, self.rect)
