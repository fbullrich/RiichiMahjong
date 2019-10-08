def protorun(tile, hand):	
	call_dirs = ['Run']
	protorun_found = False

	bottom1 = False
	bottom2 = False
	top1 = False
	top2 = False
	
	for h_tiles in hand:
		# Hand tile 2 below tile tbc -> '1' given 3
		if h_tiles.number == tile.number - 2:
			bottom2 = True
		
			
		# Hand tile 1 below tile to be called -> '2' given 3
		elif h_tiles.number == tile.number - 1:
			bottom1 = True
			
		# Hand tile 1 above tile tbc -> '4' given 3
		elif h_tiles.number == tile.number + 1:
			top1 = True
		
		# Hand tile 2 above tile tbc -> '5' given 3
		elif h_tiles.number == tile.number + 2:
			top2 = True
	
	if top1 and top2:
		call_dirs.append('Top Run')
		protorun_found = True
		
	if bottom1 and bottom2:
		call_dirs.append('Bottom Run')
		protorun_found = True
		
	if top1 and bottom1:
		call_dirs.append('Kanchan')
		protorun_found = True
	
	if protorun_found:
		return call_dirs
	else:
		return []


def pairs(tile, hand):
	tile_count = 0
	for h_tiles in hand:
		if h_tiles.number == tile.number and h_tiles.suit == tile.suit:
			tile_count += 1
		
		
	if tile_count == 2:
		return ['Pon']
	elif tile_count >= 3:
		return ['Pon', 'Kan']
	else:
		return []
	
def call_check(tile, hand):
	# 1st element of run list - 'Run'
	# 1st element of pon list - 'Pon'

	# classify hands
	souzu = []
	manzu = []
	pinzu = []
	honors = []
	
	# list of call commands
	# Kanchan - calling a kanchan
	# Top run - calling a run from the top e.g. 4, 5 -> 3
	# Bottom run - calling a run from the bottom e.g. 1, 2 -> 3
	calls = []
	
	# put hands into suits
	for tiles in hand:
		if tiles.ishonor:
			honors.append(tiles)
		elif tiles.suit == 's':
			souzu.append(tiles)
		elif tiles.suit == 'm':
			manzu.append(tiles)
		elif tiles.suit == 'p':
			pinzu.append(tiles)
	
	# check based on suit of tile
	# could be implemented in protorun func? eh
	if tile.suit == 's' and souzu:
		calls.append(protorun(tile, souzu))
		calls.append(pairs(tile, souzu))
		
	elif tile.suit == 'm' and manzu:
		calls.append(protorun(tile, manzu))
		calls.append(pairs(tile, manzu))
		
	elif tile.suit == 'p' and pinzu:
		calls.append(protorun(tile, pinzu))
		calls.append(pairs(tile, pinzu))
		
	elif tile.ishonor and honors:
		calls.append(pairs(tile, honors))
	
	if tile.ishonor and calls:
		if calls[0]:
			call = raw_input("Call: %s \n" % ', '.join(calls[0]))
		else:
			call = False
			
		if call:
			if (call.lower() in map(lambda x: x.lower() if isinstance(x, str) else x, calls[0])):
				return call.lower()
		
		return False
	
	else:
		# check that either run or pon can be called
		try:
			if calls[0] and calls[1]:
				call = raw_input("Call: %s %s \n" % (', '.join(calls[0][1:]), ', '.join(calls[1]) ))
				
			elif calls[0]:
				call = raw_input("Call: %s \n" % ', '.join(calls[0][1:]))
			
			elif calls[1]:
				call = raw_input("Call: %s \n" % ', '.join(calls[1]))
				
			else:
				call = False
		except Exception as e:
			if e is not IndexError:
				print e
				
			call = False
		
		# case insensitive
		if call:
			if (call.lower() in map(lambda x: x.lower() if isinstance(x, str) else x, calls[0])) or (call.lower() in map(lambda x: x.lower() if isinstance(x, str) else x, calls[1])):
				return call.lower()
		
		return False