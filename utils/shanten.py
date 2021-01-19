from utils.mahjong_helper import parse_hand_from_string
from utils.standard_shanten import calculateStandardShanten

def calculate_shanten(input_hand):

    hand = parse_hand_from_string(input_hand)

    chiitoi_shanten = calc_chiitoi_shanten(hand)
    kokushi_shanten = calc_kokushi_shanten(hand)
    standard_shanten = calc_standard_shanten(hand)

    return min(chiitoi_shanten, kokushi_shanten, standard_shanten)


def calc_chiitoi_shanten(hand):
    pair_count = 0

    for suit, tiles in hand.items():
        temp = {x: 0 for x in range(1, 10)}
        for tile in tiles:
            temp[tile] += 1

        for key, value in temp.items():
            if value >= 2:
                pair_count += 1

    return 6 - pair_count


def calc_kokushi_shanten(hand):
    unique_count = 0

    for suit, tiles in hand.items():
        if suit == 'z':
            for i in range(1, 7):
                if i in tiles:
                    unique_count += 1
        else:
            if 1 in tiles:
                unique_count += 1
            if 9 in tiles:
                unique_count += 1

    return 13 - unique_count


def calc_standard_shanten(hand):
    #
    # maximumShanten = max(8 - 2 * groups - max(pairs + taatsu, floor(hand.length/3)-groups) - min(1, max(0, pairs + taatsu - (4 - groups))), 6).
    #

    hand_array = [0]*38
    for suit, tiles in hand.items():
        offset = 1
        if suit == 'p':
            offset = 11
        elif suit == 's':
            offset = 21
        elif suit == 'z':
            offset = 31
        for tile in tiles:
            hand_array[tile + offset] += 1

    return calculateStandardShanten(hand_array)