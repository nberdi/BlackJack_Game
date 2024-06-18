import random
from button import Button
from cards import all_cards
from text import Text


class Cards:
    def __init__(self):
        # user random dict
        self.first_type_of_card = random.choice(all_cards)
        self.second_type_of_card = random.choice(all_cards)

        # user key of the dict
        self.f_card_key = ''.join(list(self.first_type_of_card)[0])
        self.s_card_key = ''.join(list(self.second_type_of_card)[0])

        # user random card img
        self.first_card_img = random.choice(self.first_type_of_card[self.f_card_key])
        self.second_card_img = random.choice(self.second_type_of_card[self.s_card_key])

        # value key
        self.first_card_value_key = ''.join(list(self.first_type_of_card)[1])
        self.second_card_value_key = ''.join(list(self.second_type_of_card)[1])

        # get value
        self.first_card_value = self.first_type_of_card[self.first_card_value_key]
        self.second_card_value = self.second_type_of_card[self.second_card_value_key]

        # user score
        self.user_score = None
        print(self.first_card_value + self.second_card_value)

        # to display card imgs
        self.first_card = Button(button=self.first_card_img, btn_size=(130, 130), btn_rect=(20, 450))
        self.second_card = Button(button=self.second_card_img, btn_size=(130, 130), btn_rect=(170, 450))

        # for dealer
        self.dealer_first_type_of_card = random.choice(all_cards)      # user random dict
        self.dealer_second_type_of_card = random.choice(all_cards)     # user random dict

        self.dealer_f_card_key = ''.join(list(self.dealer_first_type_of_card)[0])    # user key of the dict
        self.dealer_s_card_key = ''.join(list(self.dealer_second_type_of_card)[0])   # user key of the dict

        # user random card img
        self.dealer_first_card_img = random.choice(self.dealer_first_type_of_card[self.dealer_f_card_key])
        self.dealer_second_card_img = random.choice(self.dealer_second_type_of_card[self.dealer_s_card_key])

        # value key
        self.dealer_first_card_value_key = ''.join(list(self.dealer_first_type_of_card)[1])
        self.dealer_second_card_value_key = ''.join(list(self.dealer_second_type_of_card)[1])

        # get value
        self.dealer_first_card_value = self.dealer_first_type_of_card[self.dealer_first_card_value_key]
        self.dealer_second_card_value = self.dealer_second_type_of_card[self.dealer_second_card_value_key]

        self.dealer_score = None
        print(self.dealer_first_card_value + self.dealer_second_card_value)

        self.dealer_first_card = Button(button=self.dealer_first_card_img, btn_size=(130, 130), btn_rect=(550, 300))
        self.dealer_second_card = Button(button=self.dealer_second_card_img, btn_size=(130, 130), btn_rect=(700, 300))

    def calculate_user_score(self):
        user_score = self.first_card_value + self.second_card_value
        self.user_score = Text(text=f"Your score is: {user_score}", color=(0, 0, 0), size=35)
        return self.user_score.surface

    def calculate_dealer_score(self):
        dealer_score = self.dealer_first_card_value + self.dealer_second_card_value
        self.dealer_score = Text(text=f"Dealer's score is: {dealer_score}", color=(0, 0, 0), size=35)
        return self.dealer_score.surface
