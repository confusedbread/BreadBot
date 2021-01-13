from mahjong_helper import parse_hand_from_string


def calculate_shanten(hand):
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

    return 0


chiitoi_hand = "1133m45s1699p112z"
my_hand = parse_hand_from_string(chiitoi_hand)
print(my_hand)
shanten_pears = calc_chiitoi_shanten(my_hand)
print(shanten_pears)
shanten_kekw = calc_kokushi_shanten(my_hand)
print(shanten_kekw)
