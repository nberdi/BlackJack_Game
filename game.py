import time
from game_settings import *
from sys import exit
from button import Button
from text import Text
from alert import Alert


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

    def run(self):
        while True:
            # display game desk
            self.window.blit(self.bg_image, (0, 0))

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
                    break

                if self.alert_start_time:
                    if time.time() - self.alert_start_time < 3:
                        self.alert.run()
                    else:
                        self.alert_start_time = None
                        self.game_menu = False

            pygame.display.update()

            # quiting the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


if __name__ == '__main__':
    main = Game()
    main.run()
