from utils.mahjong_helper import parse_hand_from_string
from utils.emoji import tiles

def hand_to_emoji(hand_str):
    
    emoji_str = ""
    hand = parse_hand_from_string(hand_str)

    for tile in hand['m']:
        emoji_str += tiles[str(tile) + 'm']

    for tile in hand['s']:
        emoji_str += tiles[str(tile) + 's']

    for tile in hand['p']:
        emoji_str += tiles[str(tile) + 'p']

    for tile in hand['z']:
        emoji_str += tiles[str(tile) + 'z']

    return emoji_str