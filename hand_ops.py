def sort_hand(hand):
#takes a hand and sorts it
#order: honors, souzu, manzu, pinzu -> number, wind, dragon
#ended up being a lot easier with lambda functions LMAO
	
	sortfunc = lambda x: x.number + (ord(x.suit) * 1000 if not x.ishonor else 0)
	
	hand.sort(key = sortfunc)
	
def hand_to_text(hand):
	texthand = []
	
	for tile in hand:
		if tile.ishonor:
			texthand.append(tile.suit)
		else:
			texthand.append(str(tile.number) + tile.suit)
	return texthand