# Preparing deck of cards
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
from random import shuffle

class Deck:
	# Constructor
	def __init__(self):
		self.cards = self.create_cards()
		self.shuffle()

	# Function to create all cards in a deck
	def create_cards(self):
		cards = []
		for s in SUITE:
			for r in RANKS:
				cards.append([r,s])
		return cards

	# Function to shuffle deck
	def shuffle(self):
		shuffle(self.cards)

	# Function to split the deck in half
	def split(self):
		a = self.cards[0:26]
		b = self.cards[26::]
		return [a,b]
	pass

class Hand:
	# Hand constructor
	def __init__(self, cards):
		self.cards = cards

	# Puts a card on the bottom of the players hand
	def add(self, card):
		self.cards.append(card)

	# Takes the top card off the players hand and returns that value
	def remove(self):
		return self.cards.pop(0)
	pass

class Player:
	def __init__(self, name, hand):
		self.name = name
		self.hand = hand

	# Plays the top card from the deck
	def play(self):
		print("{} plays {} of {}".format(self.name, self.hand.cards[0][0], self.hand.cards[0][1]))
		return self.hand.remove()

	# Remove war cards
	def remove_war_cards(self):
		print("{} puts 3 cards face down.".format(self.name))
		war_cards = []
		for i in range(3):
			if self.can_play():
				war_cards.append(self.hand.remove())
		return war_cards

	# Check and make sure the player still has cards to play
	def can_play(self):
		return len(self.hand.cards) > 0
	pass

###############################
#	Game Logic Functions
###############################
# Check who won the round
def compare_cards(a, b):
	if RANKS.index(a[0]) >= RANKS.index(b[0]):
		return True
	else:
		return False

# Function to handle a war
def war(player, opponent, cards):
	# combine all cards in play to one pool and add in warcards
	warcards = player.remove_war_cards()
	warcards = append_list(warcards, cards)
	warcards = append_list(warcards, open.remove_war_cards)
	if player.can_play() and opponent.can_play():
		a = player.play()
		b = opponent.play()
		warcards.append(a)
		warcards.append(b)
		if compare_cards(a, b):
			print("{} had the higher card and won this war!".format(player.name))
			winner = player
		else:
			print("{} had the higher card and won this war!".format(opponent.name))
			winner = opponent
		shuffle(warcards)
		for w in warcards:
			winner.hand.add(w)


def append_list(li, appendage):
	for a in appendage:
		li.append(a)
	return li

######################
#### GAME PLAY #######
######################
# Deck and hand setup
deck = Deck()
hands = deck.split()
h1 = Hand(hands[0])
h2 = Hand(hands[1])

# Player Setup
print("Welcome to War, let's begin...")
print("What is your name?")
name = input()
player = Player(name, h1)
opponent = Player('Computer', h2)
counter = 0
warCount = 0

while player.can_play() and opponent.can_play():
	counter += 1
	a = player.play()
	b = opponent.play()
	winner = player
	if a[0] == b[0]:
		print("It's War")
		warCount += 1
		warcards = [a,b]
		war(player, opponent, warcards)
		#
		# # Each player grabs their war cards.
		# warcards = player.remove_war_cards()
		# warcards.append(opponent.remove_war_cards())
		# # Add the current card in play to this stack so it is given to the winner
		# warcards.append(a)
		# warcards.append(b)
		# # Each player plays another card
		# if player.can_play():
		# 	if opponent.can_play():
		# 		a = player.play()
		# 		b = opponent.play()
		# 		warcards.append(a)
		# 		warcards.append(b)
		# 		if compare_cards(a, b):
		# 			print("{} had the higher card!".format(player.name))
		# 			winner = player
		# 		else:
		# 			print("{} had the higher card!".format(opponent.name))
		# 			winner = opponent
		# 		shuffle(warcards)
		# 		for i in warcards:
		# 			winner.hand.add(i)
	else:
		if compare_cards(a, b):
			player.hand.add(a)
			player.hand.add(b)
		else:
			opponent.hand.add(a)
			opponent.hand.add(b)


print("The game is over and lasted {} rounds and had {} wars!".format(counter, warCount))
