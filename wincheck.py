from pool import unique_tiles
from hand_ops import sort_hand
		
def check_for_triplets(tiles):
#destructive
#takes in a set of tiles and returns a list of lists, 
#with the inner lists being triplets
	unique_tiles = []
	counter = {}
	
	#find unique tiles
	for tile in tiles:	
		if tile not in unique_tiles:
			unique_tiles.append(tile)
			counter[tile] = 1
		else:
			counter[tile] += 1
			
			
	triplets = []
	for tile in unique_tiles:
		if counter[tile] > 2:
			#destroy! destroy!
			for x_ in range(3):
				tiles.remove(tile)
				
			triplets.append([tile] * 3)
	
	return triplets
	

def check_for_runs(tiles):
#destructive
#finds runs from the bottom up 
#takes in a set of tiles and returns a list of lists, 
#with the inner lists being runs of 3 tiles

	all_runs = []
	
	# check to see if there is not more possibility of a run
	# i.e. if there are 3 tiles left and a run cannot be formed
	no_more_runs = False 
	
	#counter
	i_ = 0
	
	while len(tiles) >= 3 and not no_more_runs:
			
		#temp values to keep track of potential run tiles
		temp1 = tiles[i_] 
		
		
		temp2 = False
		temp3 = False
		
		
		if not temp1.ishonor:
			# tile.number -> 'number'
			for temp2tile in tiles:
				if temp2tile.number == temp1.number + 1:
					temp2 = temp2tile
					break
			
			for temp3tile in tiles:
				if temp3tile.number == temp1.number + 2:
					temp3 = temp3tile
					break
			
			if temp1 and temp2 and temp3:
				all_runs.append([temp1, temp2, temp3])
				
				#remove run tiles from the list
				tiles.remove(temp1) 
				tiles.remove(temp2)
				tiles.remove(temp3)
				
				#reset index to not miss any runs
				i_ = 0
				
			else:
				# if 
				if i_ >= tiles.index(tiles[-3]):
					no_more_runs = True
				else:
					i_ += 1
		else:
			i_ += 1 
			
	return all_runs	
		
def chiitoitsu_check(hand):
	unique_tiles = []
	pair_count = 0
	
	unique_tiles = list(set(hand))
	
	for u_tile in unique_tiles:
		tile_count = 0
		for tile in hand:
			if u_tile == tile:
				tile_count += 1
				
		if tile_count == 2:
			pair_count += 1
	
	if pair_count == 7:
		return True
	else:
		return False
	
def kokushi_check(hand):
	all_terminals = True
	pair_count = 0
	unique_tiles = []
	
	for tile in hand:
		if not tile.isterminal:
			all_terminals = False
			break
		if tile not in unique_tiles:
			unique_tiles.append(tile)
	
	if all_terminals:
		for u_tile in unique_tiles:
			tile_count = 0
			for tile in hand:
				if u_tile == tile:
					tile_count += 1
					
			if tile_count >= 2:
				pair_count += 1
			
		if pair_count > 1:
			return False
		elif pair_count == 1:
			return True
	else:
		return False

def full_win_check(hand, call_count):
	u_tile_in_hand = {}
	pairs = []
	
	# find possible heads
	for tile in hand:
		if tile not in u_tile_in_hand:
			u_tile_in_hand[tile] = 1
		else:
			u_tile_in_hand[tile] += 1
			
			if tile not in pairs:
				pairs.append(tile)
	
	if not pairs:
		return False
	
	# test each pair -> finding 4 melds with the pair removed
	for pair in pairs:
		test_hand = hand[:]
		
		for x in range(2):
			test_hand.remove(pair)
		
		# classify hands
		souzu = []
		manzu = []
		pinzu = []
		honors = []
		
		# for run priority hand
		r_melds = []
		# for triplet priority hand
		t_melds = []
		
		
		
		# put hands into suits
		for tile in test_hand:
			if tile.ishonor:
				honors.append(tile)
			elif tile.suit == 's':
				souzu.append(tile)
			elif tile.suit == 'm':
				manzu.append(tile)
			elif tile.suit == 'p':
				pinzu.append(tile)
				
		honor_trips = check_for_triplets(honors)
		
		if honor_trips:
			for trip in honor_trips:
				r_melds.append(trip)
				t_melds.append(trip)
				
		# Runs Prority ----------
		#check runs first...
		r_souzu = souzu[:]
		r_manzu = manzu[:]
		r_pinzu = pinzu[:]
		
		
		souzuruns = check_for_runs(r_souzu)
		manzuruns = check_for_runs(r_manzu)
		pinzuruns = check_for_runs(r_pinzu)
		
		for runs in (souzuruns, manzuruns, pinzuruns):
			if runs:
				for run in runs:
					r_melds.append(run)
		
		#...then triplets
		souzutriplets = check_for_triplets(r_souzu)
		manzutriplets = check_for_triplets(r_manzu)
		pinzutriplets = check_for_triplets(r_pinzu)
		
		for triplets in (souzutriplets, manzutriplets, pinzutriplets):
			if triplets:
				for triplet in triplets:
					r_melds.append(triplet)
		
		if len(r_melds) == 4 - call_count:
			return True
		
		# Triplet priority ----------
		t_souzu = souzu[:]
		t_manzu = manzu[:]
		t_pinzu = pinzu[:]
		
		#triplets...
		souzutriplets = check_for_triplets(t_souzu)
		manzutriplets = check_for_triplets(t_manzu)
		pinzutriplets = check_for_triplets(t_pinzu)
		
		for triplets in (souzutriplets, manzutriplets, pinzutriplets):
			if triplets:
				for triplet in triplets:
					t_melds.append(triplet)
		
		#... then runs
		souzuruns = check_for_runs(t_souzu)
		manzuruns = check_for_runs(t_manzu)
		pinzuruns = check_for_runs(t_pinzu)
		
		for runs in (souzuruns, manzuruns, pinzuruns):
			if runs:
				for run in runs:
					t_melds.append(run)
					
		if len(t_melds) == 4 - call_count:
			return True

def check_win(hand, call_count = 0):
	sort_hand(hand)
	
	if (kokushi_check(hand) or chiitoitsu_check(hand)):
		return True
	
	return full_win_check(hand, call_count)

def winning_tiles_finder(hand, call_count):
	test_hand = hand[:]
	winning_tiles = []
	
	u_tiles = unique_tiles()
	
	for tile_ in u_tiles:
		
		test_hand.append(tile_)
		
		wt = check_win(test_hand, call_count)
		if wt:
			winning_tiles.append(tile_)
		
		test_hand.remove(tile_)
	
	return winning_tiles

def tenpai_check(hand, call_count = 0):
	discard_for_tenpai = []
	winning_tiles = []
	
	for i_, tile in enumerate(hand):
		if tile not in discard_for_tenpai:
			testhand = hand[:]
			
			testhand.remove(tile)
			
			tenpai_tiles = winning_tiles_finder(testhand, call_count)
			
			if tenpai_tiles and (tenpai_tiles not in winning_tiles):
				discard_for_tenpai.append(tile)
				winning_tiles.append(tenpai_tiles)
	
	wt = list(set([tile for tiles in winning_tiles for tile in tiles]))
	sort_hand(wt)
			
	return wt
	
	
	