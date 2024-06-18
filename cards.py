import os
import pygame

ace = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []
ten = []
jack = []
queen = []
king = []

# Opening and loading all picture files to variables
for filename in os.listdir('imgs/game_cards'):
    if filename.startswith('ace_of_'):
        ace.append(pygame.image.load(f"imgs/game_cards/{filename}"))
    elif filename.startswith('02_of_'):
        two.append(pygame.image.load(f"imgs/game_cards/{filename}"))
    elif filename.startswith('03_of_'):
        three.append(pygame.image.load(f"imgs/game_cards/{filename}"))
    elif filename.startswith('04_of_'):
        four.append(pygame.image.load(f"imgs/game_cards/{filename}"))
    elif filename.startswith('05_of_'):
        five.append(pygame.image.load(f"imgs/game_cards/{filename}"))
    elif filename.startswith('06_of_'):
        six.append(pygame.image.load(f"imgs/game_cards/{filename}"))
    elif filename.startswith('07_of_'):
        seven.append(pygame.image.load(f"imgs/game_cards/{filename}"))
    elif filename.startswith('08_of_'):
        eight.append(pygame.image.load(f"imgs/game_cards/{filename}"))
    elif filename.startswith('09_of_'):
        nine.append(pygame.image.load(f"imgs/game_cards/{filename}"))
    elif filename.startswith('10_of_'):
        ten.append(pygame.image.load(f"imgs/game_cards/{filename}"))
    elif filename.startswith('jack_of_'):
        jack.append(pygame.image.load(f"imgs/game_cards/{filename}"))
    elif filename.startswith('queen_of_'):
        queen.append(pygame.image.load(f"imgs/game_cards/{filename}"))
    elif filename.startswith('king_of_'):
        king.append(pygame.image.load(f"imgs/game_cards/{filename}"))

all_cards: list[dict] = [
    {'ace': ace, 'value': 1},
    {'two': two, 'value': 2},
    {'three': three, 'value': 3},
    {'four': four, 'value': 4},
    {'five': five, 'value': 5},
    {'six': six, 'value': 6},
    {'seven': seven, 'value': 7},
    {'eight': eight, 'value': 8},
    {'nine': nine, 'value': 9},
    {'ten': ten, 'value': 10},
    {'jack': jack, 'value': 10},
    {'queen': queen, 'value': 10},
    {'king': king, 'value': 10}
]
