import random
import pygame
from pygame import Surface
from code.Background import Background
from code.Coin import Coin
from code.Const import W_HEIGHT, W_WIDTH
from code.Player import Player

class Level:
    def __init__(self, window: Surface):
        self.font = pygame.font.Font(None, 36)
        self.window = window
        self.speed = 10
        self.background = Background()
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.coin = Coin()
        self.coins = []
        self.coin_spawn_timer = 0
        self.coin_spawn_delay = 300
        self.score = 0
        self.game_time = 0  # Tempo total de jogo em milissegundos
        self.game_duration = 30000  # 30 segundos de jogo
        self.game_over = False
    def run(self):
        while True:
            if self.game_time >= self.game_duration: self.game_over = True
            dt = self.clock.tick(60)  # Obtém tempo decorrido entre frames (delta time)
            self.game_time += dt  # Incrementa o tempo de jogo
            self.coin_spawn_timer += dt  # Atualiza o tempo desde o último spawn
            pygame.event.get()
            self.window.fill((0, 0, 0))
            self.background.draw(self.window)
            self.background.move()
            self.player.move()
            self.player.draw(self.window)
            # Só gera uma nova moeda se passar tempo suficiente
            if self.game_over == False:
                if self.coin_spawn_timer >= self.coin_spawn_delay:
                    self.coins.append(Coin())
                    self.coin_spawn_timer = 0  # Reseta o timer para o próximo spawn
                    self.coin_spawn_timer += dt

            # Atualizar e desenhar moedas
            for coin in self.coins[:]:  # Itera sobre uma cópia da lista para evitar problemas ao remover elementos
                coin.update()
                coin.draw(self.window)

                # Se o jogador pegar a moeda, remove da lista e incrementa o score
                if self.player.rect.colliderect(coin.rect):
                    self.coins.remove(coin)
                    self.score += 1  # Incrementa a pontuação

                # Remove moedas que saíram da tela
                elif coin.rect.top > W_HEIGHT:
                    self.coins.remove(coin)


            score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.window.blit(score_text, (10, 10))

            pygame.display.flip()
            self.clock.tick(60)
            pass

