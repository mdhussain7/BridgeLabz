import random

class Card:
   def __init__(self, suit, val):
      self.suit = suit
      self.value = val

      
   def show(self):
      print("{} of {}".format(self.value, self.suit))
      
class Deck:
   def __init__(self):
      self.cards = []
      self.build()
      
   def build(self):
      for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
         for v in range(1,14):
            self.cards.append(Card(s, v))
            
   def show(self):
      for c in self.cards:
         c.show()
   
   def shuffle(self):
      for i in range(len(self.cards) - 1, 0, -1):
         r = random.randint(0,i)
         self.cards[i],self.cards[r] = self.cards[r], self.cards[i]
   
   def drawCard(self):
      return self.cards.pop()
               

 
class Player:
   def __init__(self,name):
      self.name = name
      self.hand = []
   
   def draw(self, deck):
      self.hand.append(deck.drawCard())
      return self
      
   def showHand(self):
      for card in self.hand:
         card.show()


deck = Deck()
deck.shuffle()
         
card = Card("Card",6)
card.show()

p1 = Player("player")
p1.draw(deck)
p1.showHand()
card = deck.drawCard()
deck.show()
