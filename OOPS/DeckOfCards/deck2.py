import random

inp = input("Hi,\n Are you here to Play Deck of Cards? (y/n):")
if (inp == "Y") or (inp == "y") or (inp == "Yes") or (inp == "yes"):
    print("Lets play!!")
else:
    print("Better Luck Next Time!!")
    print("Bye!!")
    exit()
    

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print('{} of {}'.format(self.value, self.suit))
    
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Diamonds", "Hearts", "Clubs"]:
            for v in range(1,14):
                self.cards.append(Card(s, v))
                
    def show(self):
        #c is a single card object, accessing the show() method from the Card class
        for c in self.cards:
            c.show()

    def shuffle(self):
        #Fisher-Yates shuffle algorithm (which is what random.shuffle uses!)
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self #see note below

    def showHand(self):
        #card is a single card object, accessing the show() method from the Card class
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()

# card = Card("Clubs", 6)
# card.show()
deck1 = Deck()
deck1.shuffle()
# deck1.show()
# card = deck1.drawCard()
# card.show()
Hussain = Player("Hussain")

#since draw() returns a Player object, we can chain methods from that class.
Hussain.draw(deck1).draw(deck1)
#print(dave.draw(deck1)) #<Player object at 0x7fe2599b7eb8>
for i in range(3):
    Hussain.draw(deck1)

# f strings rock!
print(f'\nThe {len(Hussain.hand)} cards in {Hussain.name}\'s hand:')
Hussain.showHand()

print('\nDiscarded:')
Hussain.discard().show()

print(f'\nThe {len(Hussain.hand)} cards in {Hussain.name}\'s hand recived by 4 players:')
Hussain.showHand()
print("\nBye!!")

