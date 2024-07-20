import random
from game_settings import *
from button import Button
from cards import all_cards
from text import Text


class Cards:
    def __init__(self):
        self.surface = pygame.surface.Surface((CARD_WIDTH, CARD_HEIGHT))
        self.rect = self.surface.get_rect(center=(420, 70))
        self.display_surface = pygame.display.get_surface()

        self.user_cards = None
        self.user_current_score = None
        self.blackjack_checked = None
        self.user_first_card = None
        self.user_second_card = None

        self.dealer_cards = None
        self.dealer_current_score = None
        self.dealer_first_card_score = None
        self.dealer_first_card = None
        self.dealer_second_card = None

        self.allow_first_card = True

        # results
        self.blackjack_win = Text(text="You win with a 'Blackjack'", size=60, pos=(WINDOW_WIDTH / 2, 70))
        self.user_win = Text(text="You Win!", size=60, pos=(WINDOW_WIDTH / 2, 70))
        self.dealer_win = Text(text="Dealer Wins!", size=60, pos=(WINDOW_WIDTH / 2, 70))
        self.draw = Text(text="Push!", size=60, pos=(WINDOW_WIDTH / 2, 70))

        # second hidden card
        self.hidden_card = None

    def play(self):
        # get random two cards from a dict of the list; check if there is an ace
        self.user_cards = self.is_eleven(self.random_card() + self.random_card())
        # count user total score
        self.user_current_score = self.sum_card_values(self.user_cards)
        self.blackjack_checked = self.user_current_score
        # load user card imgs
        self.user_first_card = Button(button=self.user_cards[0], btn_size=(130, 130), btn_rect=(20, 450))
        self.user_second_card = Button(button=self.user_cards[2], btn_size=(130, 130), btn_rect=(170, 450))

        # get random two cards from a dict of the list; check if there is an ace
        self.dealer_cards = self.is_eleven(self.random_card() + self.random_card())
        # count dealer total score
        self.dealer_current_score = self.sum_card_values(self.dealer_cards)
        # display dealer's first card
        self.dealer_first_card_score = self.dealer_cards[1]
        # load dealer card imgs
        self.dealer_first_card = Button(button=self.dealer_cards[0], btn_size=(130, 130), btn_rect=(250, 300))
        self.dealer_second_card = Button(button=self.dealer_cards[2], btn_size=(130, 130), btn_rect=(400, 300))

        hidden_card = pygame.image.load('imgs/hidden_card.png')
        self.hidden_card = Button(button=hidden_card, btn_size=(160, 130), btn_rect=(380, 300))

    def display_user_score(self, user_score):
        display_user_score = Text(text=f"Your score is: {user_score}", color=(0, 0, 0), size=35)
        return display_user_score.surface

    def display_dealer_score(self, dealer_score):
        display_dealer_score = Text(text=f"Dealer's score is: {dealer_score}", color=(0, 0, 0), size=35)
        return display_dealer_score.surface

    def random_card(self):
        random_card_dict = random.choice(all_cards)
        random_card_dict_key = ''.join(list(random_card_dict)[0])
        random_card_img = random.choice(random_card_dict[random_card_dict_key])
        random_card_value_key = ''.join(list(random_card_dict)[1])
        random_card_value = random_card_dict[random_card_value_key]
        return [random_card_img, random_card_value]

    def is_eleven(self, adjusted_cards: list):
        x = []
        if 1 in adjusted_cards:
            for i in adjusted_cards:
                if isinstance(i, int):
                    x.append(i)
            if sum(x) < 21:
                index = adjusted_cards.index(1)
                adjusted_cards[index] = 11
        return adjusted_cards

    def sum_card_values(self, adjusted_cards: list):
        summed_card_values = 0
        for i in adjusted_cards:
            if isinstance(i, int):
                summed_card_values += i
        return summed_card_values

    def display_user_win(self):
        self.display_surface.blit(self.user_win.surface, self.user_win.rect)

    def display_dealer_win(self):
        self.display_surface.blit(self.dealer_win.surface, self.dealer_win.rect)

    def display_draw(self):
        self.display_surface.blit(self.draw.surface, self.draw.rect)
