import time
from game_settings import *
from sys import exit
from button import Button, BetButton, HitButton, StandButton
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

        # background image
        self.bg_image = pygame.transform.scale(BG_IMAGE, (WINDOW_WIDTH, WINDOW_HEIGHT))

        # button to start the game
        self.start_button = Button(button=START_BUTTON, btn_size=(300, 300), btn_rect=(200, 670))

        # button to exit the game
        self.quit_button = Button(button=QUIT_BUTTON, btn_size=(300, 300), btn_rect=(500, 670))

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
        self.result_text = False


    def run(self):
        work = True
        while work:
            # display game desk
            # self.window.blit(self.bg_image, (0, 0))
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
                self.display_chips.run()  # display chips
                if time.time() - self.shuffle_text_start_time < 3:
                    self.display_chips.display_shuffle_text()  # displays shuffle text for 3 seconds
                else:
                    self.shuffle_text_start_time = 0

            # the shuffle text disappears after 3 seconds, and the bet text will appear.
            if self.shuffle_text_start_time == 0 and not self.game_menu:
                if self.bet_text:   # displays the bet text for the user after the shuffle text disappears.
                    self.display_chips.display_bet_text()
                if self.bet_button.run():     # if the user clicks the bet button, the game starts.
                    self.bet_text = False
                    self.display_chips.allowed_bet = False

            # display cards
            if not self.display_chips.allowed_bet:
                # to display user cards on the screen
                self.window.blit(self.display_cards.user_first_card.button, self.display_cards.user_first_card.rect)
                self.window.blit(self.display_cards.user_second_card.button, self.display_cards.user_second_card.rect)

                # to display user score on the screen
                self.window.blit(self.display_cards.display_user_score(self.display_cards.user_current_score), (30, 250))
                if self.display_cards.user_current_score == 21:
                    win = self.display_chips.user_bet * 2
                    self.display_chips.user_balance += win
                    self.display_chips.user_bet = 0
                    self.window.blit(self.display_cards.blackjack_win.surface, self.display_cards.blackjack_win.rect)

                # to display dealer card on the screen
                self.window.blit(self.display_cards.dealer_first_card.button, self.display_cards.dealer_first_card.rect)

                # to display dealer score on the screen
                self.window.blit(self.display_cards.display_dealer_score(self.display_cards.dealer_current_score), (550, 120))

                if self.hit_button.run():
                    pass

                if self.stand_button.run():
                    self.result_text = True

                if self.result_text:
                    self.display_cards.dealer_current_score = self.display_cards.sum_card_values(
                        self.display_cards.dealer_cards)
                    if self.display_cards.user_current_score < self.display_cards.dealer_current_score:
                        self.window.blit(self.display_cards.dealer_second_card.button, self.display_cards.dealer_second_card.rect)
                        self.display_chips.user_bet = 0
                        self.display_cards.display_dealer_win()
                    elif self.display_cards.user_current_score > self.display_cards.dealer_current_score:
                        self.window.blit(self.display_cards.dealer_second_card.button, self.display_cards.dealer_second_card.rect)
                        win = self.display_chips.user_bet * 2
                        self.display_chips.user_balance += win
                        self.display_chips.user_bet = 0
                        self.display_cards.display_user_win()
                    elif self.display_cards.user_current_score == self.display_cards.dealer_current_score:
                        self.window.blit(self.display_cards.dealer_second_card.button, self.display_cards.dealer_second_card.rect)
                        self.display_chips.user_balance += self.display_chips.user_bet
                        self.display_chips.user_bet = 0
                        self.display_cards.display_draw()

            pygame.display.update()

            # quiting the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


if __name__ == '__main__':
    main = Game()
    main.run()
