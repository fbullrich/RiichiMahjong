from collections import namedtuple
import itertools

NTTile = namedtuple('NTTile', ['number', 'suit', 'ishonor', 'isterminal'])
#				tile			'number'				'suit'				'ishonor'	'isterminal'
#				non-honors ->	number (1...9)			suit (s, m ,p)		false		true iff number is 1 or 9
#				honors ->		number (1..7)			honor (chun east etc)		true		true
#								(honor number used for sorting)						

def build_pool():
	NUMBER = tuple(range(1, 10))

	SUITS = ('s', 'm', 'p')

	WINDS = ('east', 'south', 'west', 'north')
	DRAGONS = ('chun', 'haku', 'hatsu')


	pool = []

	# simples and terminals
	for suit in SUITS:
		for num in NUMBER:
			for x_ in range(4):
				pool.append(NTTile(num, suit, False, (num == 1 or num == 9)))
			
	#honors
	for i_, tile in enumerate(itertools.chain(WINDS, DRAGONS)):
		for x_ in range(4):
			pool.append(NTTile(i_ + 10, tile, True, True))
			
	return pool

def unique_tiles():
	NUMBER = tuple(range(1, 10))

	SUITS = ('s', 'm', 'p')

	WINDS = ('east', 'south', 'west', 'north')
	DRAGONS = ('chun', 'haku', 'hatsu')
	
	unique_tiles = []
	
	# simples and terminals
	for suit in SUITS:
		for num in NUMBER:
			unique_tiles.append(NTTile(num, suit, False, (num == 1 or num == 9)))
			
	#honors
	for i_, tile in enumerate(itertools.chain(WINDS, DRAGONS)):
		unique_tiles.append(NTTile(i_ + 10, tile, True, True))
		
	return unique_tiles
	