import os
from game_settings import *

chips_dict: dict = {}
for filename in os.listdir('imgs/game_chips'):
    if filename.startswith('25-'):
        chips_dict['25'] = pygame.image.load(f'imgs/game_chips/{filename}')
    elif filename.startswith('50-'):
        chips_dict['50'] = pygame.image.load(f'imgs/game_chips/{filename}')
    elif filename.startswith('100-'):
        chips_dict['100'] = pygame.image.load(f'imgs/game_chips/{filename}')
    elif filename.startswith('500-'):
        chips_dict['500'] = pygame.image.load(f'imgs/game_chips/{filename}')
