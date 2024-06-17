from game_settings import *
from sys import exit


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

    def run(self):
        while True:
            # display game desk
            self.window.blit(self.bg_image, (0, 0))
            pygame.display.update()

            # quiting the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


if __name__ == '__main__':
    main = Game()
    main.run()
