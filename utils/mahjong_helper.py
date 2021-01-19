def parse_hand_from_string(hand_str):
    hand = {
        'm' : [],
        'p' : [],
        's' : [],
        'z' : []
    }
    tiles = []
    tile_count = 0

    hand_str = hand_str.lower()

    for char in hand_str:
        if valid_suit(hand_str, char):
            if valid_tiles(hand_str, char, tiles):
                hand[char] = tiles
                tiles = []
        else:
            tiles.append(int(char))
            tile_count += 1

    if tile_count != 13:
        raise Exception(
            "Invalid Number of tiles {}. Expected 13".format(tile_count))

    return hand


def valid_suit(hand_str, suit):
    return (suit == 'm' or suit == 's' or suit == 'p' or suit == 'z')


def valid_tiles(hand_str, suit, tiles):
    max_tile = 8 if suit == 'z' else 10

    for tile in tiles:
        if 0 >= tile or tile >= max_tile:
            raise Exception("Invalid Hand {}. Found in {}{}".format(
                hand_str, tiles, suit))

    return True
