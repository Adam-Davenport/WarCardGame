# Preparing deck of cards
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
	# Function to create all cards in a deck
	def create_cards(self):
		cards = []
		for s in SUITE:
			for r in RANKS:
				cards.append(r+s)
	# Constructor
	def __init__(self):
		self.cards = self.create_cards()

	# Function to shuffle deck and split it
	def shuffle(self):
		import random
		random.shuffle(self.cards)

	pass

