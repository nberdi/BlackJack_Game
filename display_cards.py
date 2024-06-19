import random
from game_settings import *
from button import Button
from cards import all_cards
from text import Text


class Cards:
    def __init__(self):
        self.surface = pygame.surface.Surface((400, 400))
        self.rect = self.surface.get_rect(center=(200, 200))
        self.display_surface = pygame.display.get_surface()

        self.user_two_cards = []
        self.dealer_two_cards = []

        self.user_cards = None
        self.user_current_score = None
        self.user_first_card = None
        self.user_second_card = None

        self.dealer_cards = None
        self.dealer_current_score = None
        self.dealer_first_card = None
        self.dealer_second_card = None

    def run(self):
        # get random two cards from a dict of the list; check if there is an ace
        self.user_cards = self.is_eleven(self.random_cards(all_cards, self.user_two_cards))

        # count user total score
        self.user_current_score = self.sum_card_values(self.user_cards)

        # load user card imgs
        self.user_first_card = Button(button=self.user_cards[0], btn_size=(130, 130), btn_rect=(20, 450))
        self.user_second_card = Button(button=self.user_cards[2], btn_size=(130, 130), btn_rect=(170, 450))

        # to display user cards on the screen
        self.display_surface.blit(self.user_first_card.button, self.user_first_card.rect)
        self.display_surface.blit(self.user_second_card.button, self.user_second_card.rect)

        # display user score on the screen
        self.display_surface.blit(self.display_user_score(self.user_current_score), (30, 250))
        if self.user_current_score == 21:
            print("You win with a 'Blackjack'")

        # get random two cards from a dict of the list; check if there is an ace
        self.dealer_cards = self.is_eleven(self.random_cards(all_cards, self.dealer_two_cards))
        # count dealer total score
        self.dealer_current_score = self.sum_card_values(self.user_cards)
        # load dealer card imgs
        self.dealer_first_card = Button(button=self.dealer_cards[0], btn_size=(130, 130), btn_rect=(550, 300))
        # self.dealer_second_card = Button(button=self.dealer_cards[1], btn_size=(130, 130), btn_rect=(700, 300))

        # to display dealer cards on the screen
        self.display_surface.blit(self.dealer_first_card.button, self.dealer_first_card.rect)

        # display dealer score on the screen
        self.display_surface.blit(self.display_dealer_score(self.dealer_current_score), (550, 120))

    def display_user_score(self, user_score):
        display_user_score = Text(text=f"Your score is: {user_score}", color=(0, 0, 0), size=35)
        return display_user_score.surface

    def display_dealer_score(self, dealer_score):
        display_dealer_score = Text(text=f"Dealer's score is: {dealer_score}", color=(0, 0, 0), size=35)
        return display_dealer_score.surface

    def random_cards(self, all_cards, two_cards):
        first_type_of_card = random.choice(all_cards)
        second_type_of_card = random.choice(all_cards)

        # user key of the dict
        f_card_key = ''.join(list(first_type_of_card)[0])
        s_card_key = ''.join(list(second_type_of_card)[0])

        # user random card img
        first_card_img = random.choice(first_type_of_card[f_card_key])
        second_card_img = random.choice(second_type_of_card[s_card_key])

        # value key
        first_card_value_key = ''.join(list(first_type_of_card)[1])
        second_card_value_key = ''.join(list(second_type_of_card)[1])

        # get value
        first_card_value = first_type_of_card[first_card_value_key]
        second_card_value = second_type_of_card[second_card_value_key]

        two_cards = [first_card_img, first_card_value, second_card_img, second_card_value]
        return two_cards

    def is_eleven(self, adjusted_cards: list):
        if 1 in adjusted_cards:
            if adjusted_cards[1] + adjusted_cards[3] < 21:
                index = adjusted_cards.index(1)
                adjusted_cards[index] = 11
        return adjusted_cards

    def sum_card_values(self, adjusted_cards: list):
        summed_card_values = 0
        for i in adjusted_cards:
            if isinstance(i, int):
                summed_card_values += i
        return summed_card_values
