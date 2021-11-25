from random import shuffle
#QUESTION 1: Class that assembles a deck, shuffles it if asked, and deals cards
class Deck:
  def __init__(self):
    self.suitlist = ['s', 'h', 'd', 'c']
    self.ranklist = ['a', 'k', 'q', 'j', 't', '9', '8', '7', '6','5','4','3','2']
    self.cardlist = []
    for suit in self.suitlist:
      for rank in self.ranklist:
        self.cardlist.append(rank + suit)
  
  def shuffleDeck(self):
    shuffle(self.cardlist)
  
  def deal(self, numCards):
    self.newhand = []
    for i in range(int(numCards)):
      self.newhand.append(self.cardlist[0])
      self.cardlist.pop(0)
    return self.newhand

#QUESTION 2: function that determines the type of hand and value of highcard
def handType(hand):
  result = []
  ranklist2=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "t", "j", "q", "k", "a"]
  valuelist=[]
  typeOfHand = ""
  handnumber = 0
  highcardvalue = 0
  #Create List of values based on hand and sort
  for term in hand:
    valuelist.append(ranklist2.index(term[0]))
  valuelist.sort()
  #Check if the cards are all consecutive
  x = valuelist[0]
  count = 0
  for value in range(4):
    if x + value + 1 == valuelist[value+1]:
     count += 1
    
  if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
    if count == 4:
      typeofHand = "straight flush"
    elif valuelist == [2,3,4,5,14]:
      typeofHand = "straight flush"
    else:
      typeofHand = "flush"

  elif count == 4:
    typeofHand = "straight"
  
  elif valuelist == [2,3,4,5,14]:
    typeofHand = "straight"

  elif valuelist[0] == valuelist[1] == valuelist[2] == valuelist[3] or valuelist[1] == valuelist[2] == valuelist[3] == valuelist[4]:
    typeofHand = "Four of a kind"

  elif valuelist[0] == valuelist[1] == valuelist[2] or valuelist[1] == valuelist[2] == valuelist[3] or valuelist[2] == valuelist[3] == valuelist[4]:
    if valuelist[3] == valuelist[4] != valuelist[2] or valuelist[0] == valuelist[1] != valuelist[2]:
      typeofHand = "Full house"
    else:
      typeofHand = "Three of a kind"

  elif (valuelist[0] == valuelist[1] and valuelist[2] == valuelist[3]) or (valuelist[1] == valuelist[2] and valuelist[3] == valuelist[4]) or (valuelist[0] == valuelist[1] and valuelist[3] == valuelist[4]):
    typeofHand = "Two pair"
  
  elif valuelist[0] == valuelist[1] or valuelist[1] == valuelist[2] or valuelist[2] == valuelist[3] or valuelist[3] == valuelist[4]:
    typeofHand = "One pair"

  else:
    typeofHand = "High card"

  if typeofHand == "High card":
    handnumber =0
  elif typeofHand == "One pair":
    handnumber = 1
  elif typeofHand == "Two pair":
    handnumber = 2
  elif typeofHand == "Three of a kind":
    handnumber = 3
  elif typeofHand == "straight":
    handnumber = 4
  elif typeofHand == "flush":
    handnumber = 5
  elif typeofHand == "Full house":
    handnumber = 6
  elif typeofHand == "Four of a kind":
    handnumber = 7
  elif typeofHand == "straight flush":
    handnumber = 8
  
  if handnumber == 0:
    highcardvalue = valuelist[4]
  elif handnumber == 1:
    if valuelist[0] == valuelist[1]:
      highcardvalue = valuelist[0]
    elif valuelist[1] == valuelist[2]:
      highcardvalue = valuelist[1]
    elif valuelist[2] == valuelist[3]:
      highcardvalue = valuelist[2]
    elif valuelist[3] == valuelist[4]:
      highcardvalue = valuelist[3]
  elif handnumber == 2:
    highcardvalue = valuelist[3]
  elif handnumber == 3:
    highcardvalue = valuelist[2]
  elif handnumber == 4:
    if valuelist == [2,3,4,5,14]:
      highcardvalue = valuelist[3]
    else:
      highcardvalue = valuelist[4]
  elif handnumber == 5:
    highcardvalue = valuelist[4]
  elif handnumber == 6:
    highcardvalue = valuelist[2]
  elif handnumber == 7:
    highcardvalue = valuelist[3]
  elif handnumber == 8:
    if valuelist == [2,3,4,5,14]:
      highcardvalue = valuelist[3]
    else:
      highcardvalue = valuelist[4]
  
  return [handnumber, highcardvalue]
