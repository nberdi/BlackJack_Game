from game_settings import *


class Text:
    def __init__(self, text, color=(128, 0, 0), size=120):
        self.font = pygame.font.SysFont('bald', size)  # font and size
        self.surface = self.font.render(text, True, color)
        self.rect = self.surface.get_rect(center=(WINDOW_WIDTH / 2, 200))
