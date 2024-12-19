import time
from game_settings import *
from sys import exit
from button import Button, BetButton, HitButton, StandButton, NewGameButton, MenuButton, DoubleButton
from text import Text
from alert import Alert
from display_chips import Chips
from display_cards import Cards


class Game:
    def __init__(self):
        # size of the game
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # title of the game
        pygame.display.set_caption(GAME_TITLE)

        # icon of the game
        pygame.display.set_icon(GAME_ICON)

        # button to start the game
        self.start_button = Button(button=START_BUTTON, btn_size=(300, 300), btn_rect=(300, 670))

        # button to exit the game
        self.quit_button = Button(button=QUIT_BUTTON, btn_size=(300, 300), btn_rect=(600, 670))

        # show game menu
        self.game_menu = True

        # game title on the screen
        self.display_game_title = Text(text=GAME_TITLE)

        # game icon on the screen
        self.display_game_icon = pygame.transform.scale(GAME_ICON, (200, 150))
        self.icon_rect = self.display_game_icon.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # display alert for user
        self.alert = Alert()
        self.alert_start_time = None  # track when the alert starts

        # chips
        self.display_chips = Chips()

        # shuffle text
        self.shuffle_text_start_time = None     # track when the shuffle text starts

        # allow to display bet text
        self.bet_text = True

        # cards
        self.display_cards = Cards()

        # button to bet
        self.bet_button = BetButton()

        # hit button
        self.hit_button = HitButton()

        # stand button
        self.stand_button = StandButton()

        # allow result text
        self.allow_result = False

        # allow take another card
        self.take_another_card = False
        self.user_another_card = None
        self.user_new_card_list = []

        self.dealer_new_card_list = []
        self.dealer_another_card = None

        # for new card img rect
        self.user_card_rect = 0
        self.dealer_card_rect = 0

        # allow click hit and stand btns
        self.allow_hit = True
        self.allow_stand = True

        # new game btn
        self.new_game_button = NewGameButton()

        # allow to display new game btn
        self.allow_new_game = False

        # start the game by displaying cards, scores, btns
        self.game = True

        # get random cards for the user and the dealer
        self.display_cards.play()

        self.menu_button = MenuButton()  # menu button

        self.double_button = DoubleButton()  # double button
        self.allow_double = True
        self.double = False
        self.double_result = False
        self.user_hand_more = False

    def blackjack_checker(self):
        # blackjack win
        if self.display_cards.blackjack_checked == 21:
            win = int(self.display_chips.user_bet + (self.display_chips.user_bet * 1.5))
            self.display_chips.user_balance += win
            self.display_chips.user_bet = 0
            self.window.blit(self.display_cards.blackjack_win.surface, self.display_cards.blackjack_win.rect)
            self.allow_hit = False
            self.allow_stand = False
            self.allow_double = False
            self.allow_new_game = True

    def hit(self):
        new_card: list = self.display_cards.random_card()
        if 1 in new_card and self.display_cards.user_current_score + 11 <= 21:
            index = new_card.index(1)
            new_card[index] = 11
        self.display_cards.user_cards += new_card
        only_int = []
        if 11 in self.display_cards.user_cards:
            for i in self.display_cards.user_cards:
                if isinstance(i, int):
                    only_int.append(i)
            if sum(only_int) > 21:
                index = self.display_cards.user_cards.index(11)
                self.display_cards.user_cards[index] = 1
        self.display_cards.user_current_score = self.display_cards.sum_card_values(self.display_cards.user_cards)
        return new_card

    def stand_btn(self):
        if self.allow_stand:
            if self.stand_button.run():
                self.allow_result = True
                self.allow_hit = False
                self.allow_double = False
                self.allow_new_game = True

        if self.allow_result:

            if self.display_cards.user_current_score > 21:
                self.user_hand_is_more()
            else:
                if self.display_cards.dealer_current_score < 17:
                    new_card = self.dealer_hand_less()
                    for card in new_card:
                        if not isinstance(card, int):
                            self.dealer_card_rect += 150
                            self.dealer_another_card = Button(button=card, btn_size=(130, 130),
                                                              btn_rect=(400 + self.dealer_card_rect, 300))
                            self.dealer_new_card_list.append(self.dealer_another_card)
                    self.display_cards.dealer_current_score = self.display_cards.sum_card_values(
                        self.display_cards.dealer_cards)

            if not None in self.dealer_new_card_list:
                for new in self.dealer_new_card_list:
                    self.window.blit(new.button, new.rect)

            if self.display_cards.dealer_current_score > 21:
                self.dealer_hand_is_more()
            else:
                self.result()
            self.allow_stand = False

    def hit_btn(self):
        if self.allow_hit:
            if self.hit_button.run():
                self.take_another_card = True
                self.allow_double = False

        if self.take_another_card:
            new_card = self.hit()
            for card in new_card:
                if not isinstance(card, int):
                    self.user_card_rect += 150
                    self.user_another_card = Button(button=card, btn_size=(130, 130), btn_rect=(
                        170 + self.user_card_rect, 450))
                    self.user_new_card_list.append(self.user_another_card)
        self.take_another_card = False

        if not None in self.user_new_card_list:
            for new in self.user_new_card_list:
                self.window.blit(new.button, new.rect)

        if self.display_cards.user_current_score > 21:
            self.user_hand_is_more()

    def double_btn(self):
        if self.display_chips.user_bet > self.display_chips.user_balance:
            self.allow_double = False
        if self.allow_double:
            if self.double_button.run():
                self.double = True
                self.double_result = True
                self.display_chips.user_balance -= self.display_chips.user_bet
                self.display_chips.user_bet += self.display_chips.user_bet

        if self.double:
            new_card = self.hit()
            for card in new_card:
                if not isinstance(card, int):
                    self.user_another_card = Button(button=card, btn_size=(130, 130), btn_rect=(320, 450))
                    self.user_new_card_list.append(self.user_another_card)

        self.double = False

        if not None in self.user_new_card_list:
            for new in self.user_new_card_list:
                self.window.blit(new.button, new.rect)

        if not None in self.dealer_new_card_list:
            for new in self.dealer_new_card_list:
                self.window.blit(new.button, new.rect)

        if self.double_result:
            if self.display_cards.user_current_score > 21:
                self.user_hand_is_more()
                self.user_hand_more = True
            else:
                if self.display_cards.dealer_current_score < 17:
                    new_card = self.dealer_hand_less()
                    for card in new_card:
                        if not isinstance(card, int):
                            self.dealer_card_rect += 150
                            self.dealer_another_card = Button(button=card, btn_size=(130, 130), btn_rect=(
                                400 + self.dealer_card_rect, 300))
                            self.dealer_new_card_list.append(self.dealer_another_card)
                    self.display_cards.dealer_current_score = self.display_cards.sum_card_values(
                        self.display_cards.dealer_cards)

            if not self.user_hand_more:
                if self.display_cards.dealer_current_score > 21:
                    self.dealer_hand_is_more()
                else:
                    self.result()
                    self.allow_hit = False
                    self.allow_stand = False
                    self.allow_double = False
                    self.allow_new_game = True

    def dealer_hand_less(self):
        new_card: list = self.display_cards.random_card()
        if 1 in new_card and self.display_cards.dealer_current_score + 11 <= 21:
            index = new_card.index(1)
            new_card[index] = 11
        self.display_cards.dealer_cards += new_card
        only_int = []
        if 11 in self.display_cards.dealer_cards:
            for i in self.display_cards.dealer_cards:
                if isinstance(i, int):
                    only_int.append(i)
            if sum(only_int) > 21:
                index = self.display_cards.dealer_cards.index(11)
                self.display_cards.dealer_cards[index] = 1
        return new_card

    def user_hand_is_more(self):
        self.allow_hit = False
        self.allow_stand = False
        self.allow_double = False
        self.allow_new_game = True
        self.display_cards.dealer_current_score = self.display_cards.sum_card_values(
            self.display_cards.dealer_cards)
        self.display_cards.allow_first_card = False
        self.window.blit(self.display_cards.dealer_second_card.button, self.display_cards.dealer_second_card.rect)
        self.display_chips.user_bet = 0
        self.display_cards.display_dealer_win()

    def dealer_hand_is_more(self):
        self.allow_hit = False
        self.allow_stand = False
        self.allow_double = False
        self.allow_new_game = True
        self.display_cards.allow_first_card = False
        self.window.blit(self.display_cards.dealer_second_card.button, self.display_cards.dealer_second_card.rect)
        win = self.display_chips.user_bet * 2
        self.display_chips.user_balance += win
        self.display_chips.user_bet = 0
        self.display_cards.display_user_win()

    def result(self):
        self.display_cards.allow_first_card = False
        self.window.blit(self.display_cards.dealer_second_card.button, self.display_cards.dealer_second_card.rect)
        if self.display_cards.user_current_score < self.display_cards.dealer_current_score:
            self.display_chips.user_bet = 0
            self.display_cards.display_dealer_win()
        elif self.display_cards.user_current_score > self.display_cards.dealer_current_score:
            win = self.display_chips.user_bet * 2
            self.display_chips.user_balance += win
            self.display_chips.user_bet = 0
            self.display_cards.display_user_win()
        elif self.display_cards.user_current_score == self.display_cards.dealer_current_score:
            self.display_chips.user_balance += self.display_chips.user_bet
            self.display_chips.user_bet = 0
            self.display_cards.display_draw()

    def play(self):
        # the shuffle text disappears after 3 seconds, and the bet text will appear.
        if self.shuffle_text_start_time == 0 and not self.game_menu:
            if self.bet_text:  # displays the bet text for the user after the shuffle text disappears.
                self.display_chips.display_bet_text()
            if self.bet_button.run():  # if the user clicks the bet button, the game starts.
                self.bet_text = False
                self.display_chips.allowed_bet = False

        # display cards
        if not self.display_chips.allowed_bet:
            # to display user cards on the screen
            self.window.blit(self.display_cards.user_first_card.button, self.display_cards.user_first_card.rect)
            self.window.blit(self.display_cards.user_second_card.button,
                             self.display_cards.user_second_card.rect)

            # to display user score on the screen
            self.window.blit(self.display_cards.display_user_score(
                self.display_cards.user_current_score), (30, 250))

            # check blackjack
            self.blackjack_checker()

            # to display dealer card on the screen
            self.window.blit(self.display_cards.dealer_first_card.button,
                             self.display_cards.dealer_first_card.rect)
            # to display dealer hidden card on the screen
            self.window.blit(self.display_cards.hidden_card.button,
                             self.display_cards.hidden_card.rect)

            # to display dealer score on the screen
            if self.display_cards.allow_first_card:
                self.window.blit(self.display_cards.display_dealer_score(
                    self.display_cards.dealer_first_card_score), (250, 120))
            else:
                self.window.blit(self.display_cards.display_dealer_score(
                    self.display_cards.dealer_current_score), (250, 120))

            self.hit_btn()
            self.stand_btn()
            self.double_btn()

            if self.allow_new_game:
                if self.new_game_button.run():
                    self.bet_text = True
                    self.display_chips.allowed_bet = True
                    self.display_cards.allow_first_card = True
                    self.allow_stand = True
                    self.allow_hit = True
                    self.allow_double = True
                    self.allow_result = False
                    self.double_result = False
                    self.user_hand_more = False

                    self.user_new_card_list = []
                    self.dealer_new_card_list = []
                    self.user_card_rect = 0
                    self.dealer_card_rect = 0

                    self.display_cards.play()
                    self.game = False
                    self.allow_new_game = False

    def run(self):
        work = True
        while work:
            # display game desk
            self.window.fill('#006a42')

            if self.game_menu:

                # display title of the game
                self.window.blit(self.display_game_title.surface, self.display_game_title.rect)

                # display icon of the game
                self.window.blit(self.display_game_icon, self.icon_rect)

                # display start btn img
                if self.start_button.run():
                    print('Game Start')
                    self.alert_start_time = time.time()

                # display quit btn img
                if self.quit_button.run():
                    print('Game Over')
                    work = False

            # display alert on the screen for 3 secs
            if self.alert_start_time:
                if time.time() - self.alert_start_time < 3:
                    self.alert.run()
                else:
                    self.alert_start_time = None
                    self.game_menu = False
                    self.shuffle_text_start_time = time.time()

            # display game chips on the screen
            if not self.game_menu:

                if self.menu_button.run():
                    self.display_chips.user_balance = 2500
                    self.game_menu = True
                    self.bet_text = True
                    self.display_chips.allowed_bet = True
                    self.display_cards.allow_first_card = True
                    self.allow_stand = True
                    self.allow_hit = True
                    self.allow_double = True
                    self.allow_result = False
                    self.double_result = False
                    self.user_hand_more = False

                    self.user_new_card_list = []
                    self.dealer_new_card_list = []
                    self.user_card_rect = 0
                    self.dealer_card_rect = 0

                    self.display_cards.play()

                self.display_chips.run()  # display chips
                if time.time() - self.shuffle_text_start_time < 3:
                    self.display_chips.display_shuffle_text()  # displays shuffle text for 3 seconds
                else:
                    self.shuffle_text_start_time = 0
                    self.game = True

                if self.game:
                    self.play()
                else:
                    self.game = True

            pygame.display.update()

            # quiting the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


if __name__ == '__main__':
    main = Game()
    main.run()
