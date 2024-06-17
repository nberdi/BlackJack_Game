from game_settings import *
from text import Text
from button import Button
from chips import chips_dict


class Alert:
    def __init__(self):
        self.surface = pygame.surface.Surface((ALERT_WIDTH, ALERT_HEIGHT))
        self.rect = self.surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.display_surface = pygame.display.get_surface()

        # display 'Your Balance:'
        self.alert_text = Text(text="Your Balance:", color=(255, 255, 255), size=90)

        # display 500 chip img
        self.chip = Button(button=chips_dict['500'], btn_size=(200, 200))
        self.chip.set_position((410, 200), 'center')

        # display user balance
        self.balance_text = Text(text="$2500", color=(255, 255, 255), size=90, pos=(WINDOW_WIDTH / 2, 500))

    def run(self):
        self.surface.fill((69, 69, 69))
        self.display_surface.blit(self.surface, self.rect)  # display surface (box)
        self.display_surface.blit(self.alert_text.surface, self.alert_text.rect)  # display text "Your Balance"
        self.display_surface.blit(self.chip.button, self.chip.rect.center)   # display 500 chip
        self.display_surface.blit(self.balance_text.surface, self.balance_text.rect)  # display user balance
