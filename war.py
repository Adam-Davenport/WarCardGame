# Preparing deck of cards
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

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
				cards.append(r+s)
		return cards

	# Function to shuffle deck
	def shuffle(self):
		import random
		random.shuffle(self.cards)

	# Function to split the deck in half
	def split(self):
		a = self.cards[0:26]
		b = self.cards[26::]
		return [a,b]
	pass
	"""
	This is the Deck Class. This object will create a deck of cards to initiate
	play. You can then use this Deck list of cards to split in half and give to
	the players. It will use SUITE and RANKS to create the deck. It should also
	have a method for splitting/cutting the deck in half and Shuffling the deck.
	"""

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
		print("{a} plays {b}".format(a=self.name, b=self.hand.cards[0]))
		return self.hand.remove()

	# Check and make sure the player still has cards to play
	def can_play(self):
		return len(self.hand.cards) > 0
	pass

######################
#### GAME PLAY #######
######################
# Deck and hand setup
deck = Deck()
hands = deck.split()
h1 = Hand(hands[0])
h2 = Hand(hands[1])
print(hands)

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
	if a[0] == b[0]:
		print("It's War")
		warCount += 1
	elif RANKS.index(a[0]) > RANKS.index(b[0]):
		print("{} wins!".format(player.name))

print("The game is over and lasted {} rounds and had {} wars!".format(counter, warCount))