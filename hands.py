from pool import NTTile

# collection of winning hands to test with

def kokushi():
	kokushi_hand = []
	
	# add tiles
	kokushi_hand.append(NTTile(14, 'chun', 1, 1))
	kokushi_hand.append(NTTile(15, 'haku', 1, 1))
	kokushi_hand.append(NTTile(16, 'hatsu', 1, 1))
	
	kokushi_hand.append(NTTile(1, 'p', 0, 1))
	kokushi_hand.append(NTTile(1, 's', 0, 1))
	kokushi_hand.append(NTTile(1, 'm', 0, 1))
	
	kokushi_hand.append(NTTile(9, 'p', 0, 1))
	kokushi_hand.append(NTTile(9, 's', 0, 1))
	kokushi_hand.append(NTTile(9, 'm', 0, 1))
				
	kokushi_hand.append(NTTile(10, 'east', 1, 1))
	kokushi_hand.append(NTTile(12, 'west', 1, 1))
	kokushi_hand.append(NTTile(13, 'north', 1, 1))
	
	kokushi_hand.append(NTTile(11, 'south', 1, 1))
	# kokushi_hand.append(NTTile(13, 'north', 1, 1))
	
	kokushi_hand.append(NTTile(20, 'random', 1, 0))

	hand = [kokushi_hand.pop() for x in range(14)]
	return hand

# 2 4 6 8 pairs of pinzu
# 2 4 6 pairs of souzu
# also tanyao
def chiitoitsu():
	chiitoitsu_hand = []

	for x in range(4):
		chiitoitsu_hand.append(NTTile(2*x + 2, 'p', 0, 0))
		chiitoitsu_hand.append(NTTile(2*x + 2, 'p', 0, 0))
	for y in range(2):
		chiitoitsu_hand.append(NTTile(2*y + 2, 's', 0, 0))
		chiitoitsu_hand.append(NTTile(2*y + 2, 's', 0, 0))
		
	chiitoitsu_hand.append(NTTile(5, 'm', 0, 0))
	
	chiitoitsu_hand.append(NTTile(5, 'm', 0, 0))
	# chiitoitsu_hand.append(NTTile(8, 'm', 0, 0))
	
	
	hand = [chiitoitsu_hand.pop() for x in range(14)]
	return hand
	
def suuankou():
	suuankou_hand = []
	
	for x in ('p', 's', 'm'):
		for y in range(3):
			suuankou_hand.append(NTTile(2, x, 0, 0))
			
	for y in range(3):
		suuankou_hand.append(NTTile(9, 'p', 0, 0))
	
	for z in range(2):
		suuankou_hand.append(NTTile(5, 's', 0, 0))	
	
	hand = [suuankou_hand.pop() for x in range(14)]
	return hand
	
def pinfu():
	pinfu = []
	
	for x in ('p', 's', 'm'):
		for i in range(2,5):
			pinfu.append(NTTile(i, x, 0, 0))
		if x == 'p':
			for i in range(6,9):
				pinfu.append(NTTile(i, x, 0, 0))
	
	for y in range(2):
		pinfu.append(NTTile(4, 'm', 0, 0))
	
	hand = [pinfu.pop() for x in range(14)]
	return hand
		
def tenpai_hand():
	tenpai_hand = []
	
	for x in ('p', 's', 'm'):
		for y in range(3):
			tenpai_hand.append(NTTile(2, x, 0, 0))
			
	for y in range(3):
		tenpai_hand.append(NTTile(9, 's', 0, 0))
	
	tenpai_hand.append(NTTile(6, 'p', 0, 0))
	tenpai_hand.append(NTTile(6, 'm', 0, 0))
	
	hand = [tenpai_hand.pop() for x in range(14)]
	return hand
	
def not_tenpai_hand():
	not_tenpai_hand = []
	
	for x in ('p', 's', 'm'):
		for y in range(3):
			not_tenpai_hand.append(NTTile(2, x, 0, 0))
			
	for y in range(3):
		not_tenpai_hand.append(NTTile(9 + y * 2, 's', 0, 0))
	
	not_tenpai_hand.append(NTTile(6, 'p', 0, 0))
	not_tenpai_hand.append(NTTile(6, 'm', 0, 0))
	
	hand = [not_tenpai_hand.pop() for x in range(14)]
	return hand
	
def test_hand():
	tenpai_hand = []
	
	
	for y in range(3):
		tenpai_hand.append(NTTile(1, 'm', 0, 1))
		tenpai_hand.append(NTTile(4, 'm', 0, 0))
			
	for y in range(2,8):
		tenpai_hand.append(NTTile(y, 'm', 0, y == 9))
	
	tenpai_hand.append(NTTile(9, 'm', 0, 1))
	tenpai_hand.append(NTTile(9, 'm', 0, 1))
	
	hand = [tenpai_hand.pop() for x in range(14)]
	return hand
	
def chuuren():
	chuuren_hand = []

	for y in range(3):
		chuuren_hand.append(NTTile(9, 'm', 0, 1))
			
	for x in range(8, 1, -1):
		chuuren_hand.append(NTTile(x, 'm', 0, 0))
		
	for y in range(3):
		chuuren_hand.append(NTTile(1, 'm', 0, 1))
		
	# chuuren_hand.append(NTTile(5, 'm', 0, 0))
	chuuren_hand.append(NTTile(11, 'south', 1, 1))
	
	hand = [chuuren_hand.pop() for x in range(14)]
	return hand
	
def called_hand():
	called_hand = []
	
	# for y in range(3):
		# called_hand.append(NTTile(11, 'south', 1, 1))
		
	# for y in range(3):
		# called_hand.append(NTTile(12, 'west', 1, 1))
		
	# called_hand.append(NTTile(13, 'north', 1, 1))
	# called_hand.append(NTTile(13, 'north', 1, 1))
	
	for y in range(3):
		called_hand.append(NTTile(1, 's', 0, 1))
		
	for y in range(2):
		called_hand.append(NTTile(7, 'm', 0, 0))
	
	for y in range(2):
		called_hand.append(NTTile(4, 'm', 0, 0))
		
	called_hand.append(NTTile(5, 'm', 0, 0))	
		
	
		
	hand = [called_hand.pop() for x in range(len(called_hand))]
		
	return hand