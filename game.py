from game_settings import *
from sys import exit
from button import Button
from text import Text


class Game:
    def __init__(self):
        # size of the game
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        # title of the game
        pygame.display.set_caption("BlackJack")

        # icon of the game
        self.game_icon = pygame.image.load('imgs/game_icon.png')
        pygame.display.set_icon(self.game_icon)

        # background image
        bg_image = pygame.image.load('imgs/game_desk.png')
        self.bg_image = pygame.transform.scale(bg_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

        # button to start the game
        start_button = pygame.image.load('imgs/start_button.png')
        self.start_button = Button(button=start_button, btn_size=(300, 300), btn_rect=(200, 670))

        # button to exit the game
        quit_button = pygame.image.load('imgs/quit_button.png')
        self.quit_button = Button(button=quit_button, btn_size=(300, 300), btn_rect=(500, 670))

        # show game
        self.show_elements = True

        # game title on the screen
        self.display_game_title = Text(text="BlackJack")

        # game icon on the screen
        self.display_game_icon = pygame.transform.scale(self.game_icon, (200, 150))
        self.icon_rect = self.display_game_icon.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    def run(self):
        while True:
            # display game desk
            self.window.blit(self.bg_image, (0, 0))

            if self.show_elements:

                # display title of the game
                self.window.blit(self.display_game_title.surface, self.display_game_title.rect)

                # display icon of the game
                self.window.blit(self.display_game_icon, self.icon_rect)

                # display start btn img
                if self.start_button.run():
                    print('Game Start')

                # display quit btn img
                if self.quit_button.run():
                    print('Game Over')
                    break

            pygame.display.update()

            # quiting the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


if __name__ == '__main__':
    main = Game()
    main.run()
