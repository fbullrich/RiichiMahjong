import random
from wincheck import check_win, tenpai_check
import hands
from pool import build_pool, NTTile
from hand_ops import sort_hand, hand_to_text
from call_tiles import call_check

# todo: implement calling tiles and tenpai (related)

#Oct 4 - tenpai complete


def find_tile(tile, hand):
	tilefound = False
	returntile = None
	try:
		num = int(tile[0])
		suit = tile[1]
		honor = False
	except:
		honor = True
		suit = tile
		
	if honor:
		for hand_tiles in hand:
			if hand_tiles.suit == suit:
				tilefound = True
				returntile = hand_tiles
	else:
		for hand_tiles in hand:
			if (hand_tiles.number, hand_tiles.suit) == (num, suit):
				tilefound = True
				returntile = hand_tiles
	if tilefound:
		return returntile
	else:
		raise TileError
		

def start():
	greeting = "Welcome to mahjong v1.0"
	pool = build_pool()
	
	print greeting
	state = False
	
	while not state:
		win = False
	
		game_pool = pool[:]
		
		player_discards = []
		enemy_discards = []
		
		#track calls made
		call_count = 0
		
		# generate hand
		random.shuffle(game_pool)
		hand = [game_pool.pop() for z_ in range(14)]
		sort_hand(hand)
		
		#for calls
		# used for dora, yaku
		called_hand = []
		# used to print calls
		display_calls = [] 
		
		#simulate enemy hand
		del game_pool[0:14]
		
		print("Hand:", hand_to_text(hand))
		
		win = check_win(hand)
		
		if win:
			print("Tenhou! your hand:", hand_to_text(hand))
		else:
			while not win and (len(game_pool) > 14):
			
				# Discarding -------------
				discarded = False
				discard = raw_input("Enter discard tile:\n")
				try:
					hand.remove(find_tile(discard, hand))
					discarded = True
				except AttributeError:
					print "Unknown Error"
				except:
					print("Error: tile not in hand.")
				
				if discarded:
				
					# Enemy discard Phase -----
					e_discard = game_pool.pop()
					
					enemy_discards.append(e_discard)
		
					print "Enemy discard:", hand_to_text([e_discard])
					print ""
					
					test_hand = hand[:]
					test_hand.append(e_discard)
					
					if check_win(test_hand, call_count):
						print("Ron! Winning hand:", hand_to_text(sort_hand(test_hand)), display_calls)
						win = True
						
					else:
						# Calling discard ----------
						call = call_check(e_discard, hand)
					
						if call:
							call_count += 1
							called_tiles = []
							enemy_discards.remove(e_discard)
							
							if call == 'pon':
								for x in range(3):
									called_tiles.append(e_discard)
								for x in range(2):
									hand.remove(e_discard)
									
							elif call == 'top run':
								for num in range(e_discard.number, e_discard.number + 3):
									called_tiles.append(NTTile(num, e_discard.suit, 0, (num ==1 or num==9)))
									
									if not num == e_discard.number:
										hand.remove(NTTile(num, e_discard.suit, 0, (num==1 or num==9)))
										
							elif call == 'bottom run':
								for num in range(e_discard.number - 2, e_discard.number + 1):
									called_tiles.append(NTTile(num, e_discard.suit, 0, (num ==1 or num==9)))
									
									if not num == e_discard.number:
										hand.remove(NTTile(num, e_discard.suit, 0, (num==1 or num==9)))
							
							elif call == 'kanchan':
								for num in range(e_discard.number - 1, e_discard.number + 2):
									called_tiles.append(NTTile(num, e_discard.suit, 0, (num ==1 or num==9)))
									
									if not num == e_discard.number:
										hand.remove(NTTile(num, e_discard.suit, 0, (num==1 or num==9)))
							
							called_hand.append(called_tiles)
							display_calls.append(hand_to_text(called_tiles))
							
							sort_hand(hand)
							print hand_to_text(hand)
							print display_calls
							
						# Drawing Tiles -----------
						else:
							draw = game_pool.pop()
							
							print "Drew the %s" %hand_to_text([draw])
							
							tc = tenpai_check(hand, call_count)
							print(bool(tc))
							if tc:
								print("Tenpai! Waiting on:", tc)
							
							hand.append(draw)
							sort_hand(hand)
							
							if check_win(hand, call_count):
								print("Tsumo! Winning tile:", hand_to_text([draw]))
								win = True
								
							print(hand_to_text(hand))
							if call_count > 0:
								print(display_calls)
		
			if len(game_pool) == 14:
				print "Ryuukouku to be implemented"
		
		state = (raw_input("type 'end' to finish\n") == 'end')
		
def tenhou_sim():
	pool = build_pool()

	print "Start:"
	
	game_pool = pool[:]
	random.shuffle(game_pool)
	hand = [game_pool.pop() for z_ in range(14)]
	
	tenhou = check_win(hand)
	
	gamelimit = 1000000
	
	if tenhou:
		print "Tenhou on the first try!!"
		sort_hand(hand)
		print(hand_to_text(hand))
	else:
		state = True
		while state:
			games =1
			while not tenhou and (games < gamelimit):
				game_pool = pool[:]
				random.shuffle(game_pool)
				hand = [game_pool.pop() for z_ in range(14)]
				
				tenhou = check_win(hand)
				
				games +=1
			if games < gamelimit:
				print "Tenhou found on game: %d" %games
				sort_hand(hand)
				print("Hand:", hand_to_text(hand)) 
			else:
				print "No tenhou found in %d hands" %games
			
			state = (raw_input("type 'end' to finish\n") != 'end')

def test():
	pool = build_pool()
	
	mode = raw_input("tenpai or check win? \n")
	
	# hand that should win
	winning_hand = hands.called_hand()
	call_count = 2
	# call_count = 0
	
	# random.shuffle(winning_hand)
	
	if mode == 'tenpai':
		print "Tenpai hand:", hand_to_text(winning_hand)
		
		tenpai_tiles = tenpai_check(winning_hand, call_count)
		
		flat = []
		for tile in tenpai_tiles:
			for ti_ in tile:
				flat.append(ti_)
		
		list(set(flat))
		sort_hand(flat)
		
		if tenpai_tiles:
			print "Tenpai for:", hand_to_text(flat)
		else:
			print("Not in tenpai")
			
	else:
		sort_hand(winning_hand)
		print(hand_to_text(winning_hand))
		
		if check_win(winning_hand, call_count):
			print "Success"
		else:
			print "Failure"

start()