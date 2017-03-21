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
		return cards
	# Constructor
	def __init__(self):
		self.cards = self.create_cards()

	# Function to shuffle deck
	def shuffle(self):
		import random
		random.shuffle(self.cards)

	def get_cards(self):
		return self.cards
	pass
	"""
	This is the Deck Class. This object will create a deck of cards to initiate
	play. You can then use this Deck list of cards to split in half and give to
	the players. It will use SUITE and RANKS to create the deck. It should also
	have a method for splitting/cutting the deck in half and Shuffling the deck.
	"""

class Hand:
	'''
	This is the Hand class. Each player has a Hand, and can add or remove
	cards from that hand. There should be an add and remove card method here.
	'''
	pass

class Player:
	"""
	This is the Player class, which takes in a name and an instance of a Hand
	class object. The Payer can then play cards and check if they still have cards.
	"""
	pass


######################
#### GAME PLAY #######
######################
deck = Deck()
print("Welcome to War, let's begin...")
print(deck.get_cards())

# Use the 3 classes along with some logic to play a game of war!
