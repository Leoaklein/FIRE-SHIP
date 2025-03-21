import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import W_HEIGHT, W_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('../asset/desert-background-looped.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        while True:

            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'PLAY', (255,255,255),(W_WIDTH/2,W_HEIGHT/2-20))
            self.menu_text(50, 'SCORE', (255,255,255), (W_WIDTH/2,W_HEIGHT/2+20))
            if menu_option == 0:
                self.menu_text(50, 'PLAY', (255, 0, 0), (W_WIDTH / 2, W_HEIGHT / 2 - 20))
            elif menu_option == 1:
                self.menu_text(50, 'SCORE', (255, 0, 0), (W_WIDTH / 2, W_HEIGHT / 2 + 20))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = 1
                    elif event.key == pygame.K_UP:
                        menu_option = 0
                    elif event.key ==pygame.K_RETURN:
                        return menu_option

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


