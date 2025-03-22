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
        self.background = Background()
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.coins = []
        self.coin_spawn_timer = 0
        self.coin_spawn_delay = 300
        self.score = 0
        self.game_time = 0
        self.game_duration = 30000
        self.game_over = False

    # cleaning level for restarting game
    def reset(self):
        self.coins = []
        self.coin_spawn_timer = 0
        self.score = 0
        self.game_time = 0
        self.game_over = False

    def run(self):
        self.reset()  # Cleaning Level
        while not self.game_over:
            dt = self.clock.tick(60)
            self.game_time += dt
            self.coin_spawn_timer += dt

            # Check for closed events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.window.fill((0, 0, 0))
            self.background.draw(self.window)
            self.background.move()
            self.player.move()
            self.player.draw(self.window)

            # Create coin
            if self.coin_spawn_timer >= self.coin_spawn_delay:
                self.coins.append(Coin())
                self.coin_spawn_timer = 0

            # update and draw coin
            for coin in self.coins[:]:
                coin.update()
                coin.draw(self.window)

                # Remove coin and increment score
                if self.player.rect.colliderect(coin.rect):
                    self.coins.remove(coin)
                    self.score += 1

                # Remove coins out screen
                elif coin.rect.top > W_HEIGHT:
                    self.coins.remove(coin)

            # Show the Score
            score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.window.blit(score_text, (10, 10))

            # Show game time
            time_left = max(0, (self.game_duration - self.game_time) // 1000)  # Tempo restante em segundos
            timer_text = self.font.render(f"Time: {time_left}", True, (255, 255, 255))
            self.window.blit(timer_text, (W_WIDTH - 120, 10))

            pygame.display.flip()

            # Check for game over
            if self.game_time >= self.game_duration:
                self.game_over = True

        # Show game over in the screen
        self.window.fill((0, 0, 0))  # cleaning screen
        game_over_text = self.font.render("Game Over", True, (255, 255, 255))
        score_final_text = self.font.render(f"Final Score: {self.score}", True, (255, 255, 255))

        # Text position
        self.window.blit(game_over_text, (W_WIDTH // 2 - 70, W_HEIGHT // 2 - 50))
        self.window.blit(score_final_text, (W_WIDTH // 2 - 90, W_HEIGHT // 2))

        pygame.display.flip()
        pygame.time.wait(3000)
