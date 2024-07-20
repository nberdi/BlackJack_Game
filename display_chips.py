from game_settings import *
from button import Button
from chips import chips_dict
from text import Text


class Chips:
    def __init__(self):
        self.surface = pygame.surface.Surface((CHIPS_WIDTH, CHIPS_HEIGHT))
        self.rect = self.surface.get_rect(bottomleft=(190, 550))
        self.display_surface = pygame.display.get_surface()

        # display chips
        self.twenty_five = Button(button=chips_dict['25'], btn_size=(100, 100), btn_rect=(50, 580))
        self.fifty = Button(button=chips_dict['50'], btn_size=(100, 100), btn_rect=(160, 580))
        self.hundred = Button(button=chips_dict['100'], btn_size=(100, 100), btn_rect=(275, 580))
        self.five_hundred = Button(button=chips_dict['500'], btn_size=(100, 100), btn_rect=(390, 580))

        # display text for user
        self.shuffle_text = Text(text="Shuffling...")
        self.bet_text = Text(text="Place Your Bets", size=100)

        # user balance
        self.user_balance = 2500
        self.user_balance_text = None

        # display user bet
        self.user_bet = 0
        self.display_user_bet_text = None

        # can user bet?
        self.allowed_bet = True

    def run(self):
        self.display_surface.blit(self.twenty_five.button, self.twenty_five.rect)
        self.display_surface.blit(self.fifty.button, self.fifty.rect)
        self.display_surface.blit(self.hundred.button, self.hundred.rect)
        self.display_surface.blit(self.five_hundred.button, self.five_hundred.rect)

        self.display_surface.blit(self.calculate_user_balance(), (560, 510))

        self.display_surface.blit(self.calculate_user_bet(), (60, 120))

        # user can bet by clicking chip buttons
        if self.allowed_bet:
            if self.twenty_five.run():
                if self.user_balance >= 25:
                    self.user_balance -= 25
                    self.user_bet += 25
            elif self.fifty.run():
                if self.user_balance >= 50:
                    self.user_balance -= 50
                    self.user_bet += 50
            elif self.hundred.run():
                if self.user_balance >= 100:
                    self.user_balance -= 100
                    self.user_bet += 100
            elif self.five_hundred.run():
                if self.user_balance >= 500:
                    self.user_balance -= 500
                    self.user_bet += 500

    def display_shuffle_text(self):
        self.display_surface.blit(self.shuffle_text.surface, self.shuffle_text.rect)

    def display_bet_text(self):
        self.display_surface.blit(self.bet_text.surface, self.bet_text.rect)

    def calculate_user_balance(self):
        self.user_balance_text = Text(text='$'+str(self.user_balance), color=(255, 255, 255), size=60)
        return self.user_balance_text.surface

    def calculate_user_bet(self):
        self.display_user_bet_text = Text(text='$'+str(self.user_bet), color=(255, 255, 255), size=60)
        return self.display_user_bet_text.surface
