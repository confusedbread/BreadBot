from utils import mahjong_helper


def calculate_shanten(hand):
  pass

def chiitoi_shanten(hand):
  pair_count = 0

  for suit, tiles in hand.items():
    temp = {x: 0 for x in range(1, 10)}
    for tile in tiles:
      if tile not in temp:
        
        pass
      else:
        temp[tile] += 1

    for key, value in temp.items():
      if value >= 2:
        pair_count += 1
  
  return 6 - pair_count

def kokushi_shanten(hand):
  unique_count = 0

  for suit, tiles in hand.items():
    if suit == 'z':
      for i in range(1,7):
    else:
      if '1' in tiles:
        unique_count += 1
      if '9' in tiles:
        unique_count += 1

chiitoi_hand = "1133m45s699p112z"
my_hand = parse_hand_from_string(chiitoi_hand)
print(my_hand)
shanten = chiitoi_shanten(my_hand)
print(shanten)