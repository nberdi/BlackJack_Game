from game_settings import *


class Button:
    def __init__(self, button, btn_size, btn_rect=(0, 0)):
        self.button = pygame.transform.scale(button, btn_size)  # btn img
        self.rect = self.button.get_rect(bottomleft=btn_rect)
        self.surface = pygame.display.get_surface()     # surface for button display
        self.clicked = False

    def set_position(self, position, attr):
        setattr(self.rect, attr, position)

    def run(self):
        action = False
        pos = pygame.mouse.get_pos()    # getting mouse position

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        self.surface.blit(self.button, self.rect)
        return action   # if the button is pressed, returns True


class BetButton(Button):
    def __init__(self):
        button = pygame.image.load('imgs/bet_button.png')
        super().__init__(button=button, btn_size=(300, 300), btn_rect=(920, 680))


class HitButton(Button):
    def __init__(self):
        button = pygame.image.load('imgs/hit_button.png')
        super().__init__(button=button, btn_size=(300, 300), btn_rect=(700, 200))


class StandButton(Button):
    def __init__(self):
        button = pygame.image.load('imgs/stand_button.png')
        super().__init__(button=button, btn_size=(300, 300), btn_rect=(920, 200))


class NewGameButton(Button):
    def __init__(self):
        button = pygame.image.load('imgs/new_game_button.png')
        super().__init__(button=button, btn_size=(300, 300), btn_rect=(700, 680))


class MenuButton(Button):
    def __init__(self):
        button = pygame.image.load('imgs/exit.png')
        super().__init__(button=button, btn_size=(50, 50), btn_rect=(20, 60))
