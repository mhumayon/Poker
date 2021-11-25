from random import shuffle
from previous import Deck
from previous import handType
from graphics import *
from button import Button
from time import sleep

w = GraphWin("Poker", 1000, 500)
bDeal = Button(300, 333, "Deal", w, "green")
bQuit = Button(600, 333, "Quit", w, "red")
discardingBox = Rectangle(Point(770, 100), Point(970, 330))
bDiscard = Button(830, 370, "Confirm Discard", w, "yellow")
bCard1 = Button(800, 230, "1", w, "light blue")
bCard2 = Button(830, 230, "2", w, "light blue")
bCard3 = Button(860, 230, "3", w, "light blue")
bCard4 = Button(890, 230, "4", w, "light blue")
bCard5 = Button(920, 230, "5", w, "light blue")
bCard1.makeThin()
bCard2.makeThin()
bCard3.makeThin()
bCard4.makeThin()
bCard5.makeThin()
bDiscard.fontSize(7)
discardingBox.draw(w)
t1 = Text(Point(500,60), "")
#empty string to avoid an error the first time the if statement in the while loop runs
list1 = []
bettingBar = Entry(Point(130, 260), 15)
bettingBar.draw(w)
bettingBox = Rectangle(Point(30, 100), Point(230, 330))
bettingBox.draw(w)
balance = 100
t2 = Text(Point(130, 125), "BETTING:")
t3 = Text(Point(130, 148), "Current Balance: $" + str(balance))
t4 = Text(Point(130, 230), "Enter amount to bet:")
t5 = Text(Point(130, 300), "Illegal Bet! Try again")
t7 = Text(Point(870, 125), "DISCARDING:")
t8 = Text(Point(870, 148), "You can discard and replace cards")
t9 = Text(Point(870, 165), "only once after each deal")
t10 = Text(Point(870, 210), "Click on the card(s) you want to discard:")
t11 = Text(Point(500, 100), "Discard cards to improve your hand (click only 'Confirm Discard' if you want to keep your hand)" )
t12 = Text(Point(870, 300), "Click the button below to confirm")
t8.setSize(8)
t9.setSize(8)
t10.setSize(6)
t11.setSize(7)
t12.setSize(8)
t3.setSize(8)
t4.setSize(8)
t2.draw(w)
t3.draw(w)
t4.draw(w)
t7.draw(w)
t8.draw(w)
t9.draw(w)
t10.draw(w)
t12.draw(w)
def moneyGet(currentBalance, betMoney, multiplier):
  return (currentBalance + int(betMoney) * multiplier)
  
def moneyEarned(betMoney, multiplier):
  return(int(betMoney) * multiplier)


while True:
  pokerDeck = Deck()
  pokerDeck.shuffleDeck() 
  p1=w.getMouse()

  if bDeal.clicked(p1):
    if int(bettingBar.getText()) < 0 or (balance - int(bettingBar.getText())) < 0:
      t5.draw(w)
      bDeal.deactivate()
      sleep(1.5)
      bDeal.activate()
      t5.undraw()
      continue

    betValue = bettingBar.getText()
    bettingBar.setText("")

    for i in list1:
      i.undraw()
    list1 = []
    t1.undraw()
    x = pokerDeck.deal(5)
    print(x)

    y = handType(x)
    p = Point(430, 200)
    n=0
    for card in x:
      card = "cards/" + card + ".gif"
      c1= Image(p, card)
      c1.draw(w)
      list1.append(c1)
      n += 30
      p = Point(430 + n, 200)
    msg = ""
    msg2 = " hand with high card"
    msg3 = ""
    handnames = ["High card", "One pair", "Two pair", "Three of a kind", "Straight", "Flush", "Full house", "Four of a kind", "Straight flush"]
    valuestocards = ["Null", "Null", " two", " three", " four", " five", " six", " seven", " eight", " nine", " ten", " jack", " queen", " king", " ace"]
    if 0 <= y[0] <= 8:
      msg = handnames[y[0]]
    if 0<= y[1] <= 14:
      msg3 = valuestocards[y[1]]
    msgfull = msg + msg2 + msg3
    t1 = Text(Point(500,60), msgfull)
    t1.draw(w)


    discardcheck = Point(10,10)
    cardstoremove =[]
    t11.draw(w)

    while not bDiscard.clicked(discardcheck):
      discardcheck = w.getMouse()
      if bCard1.thinClicked(discardcheck):
        if x[0] not in cardstoremove:
          cardstoremove.append(x[0])
          bCard1.colorChange("yellow")
        elif x[0] in cardstoremove:
          cardstoremove.pop(cardstoremove.index(x[0]))
          bCard1.colorChange("light blue")

      if bCard2.thinClicked(discardcheck):
        if x[1] not in cardstoremove:
          cardstoremove.append(x[1])
          bCard2.colorChange("yellow")
        elif x[1] in cardstoremove:
          cardstoremove.pop(cardstoremove.index(x[1]))
          bCard2.colorChange("light blue")

      if bCard3.thinClicked(discardcheck):
        if x[2] not in cardstoremove:
          cardstoremove.append(x[2])
          bCard3.colorChange("yellow")
        elif x[2] in cardstoremove:
          cardstoremove.pop(cardstoremove.index(x[2]))
          bCard3.colorChange("light blue")

      if bCard4.thinClicked(discardcheck):
        if x[3] not in cardstoremove:
          cardstoremove.append(x[3])
          bCard4.colorChange("yellow")
        elif x[3] in cardstoremove:
          cardstoremove.pop(cardstoremove.index(x[3]))
          bCard4.colorChange("light blue")

      if bCard5.thinClicked(discardcheck):
        if x[4] not in cardstoremove:
          cardstoremove.append(x[4])
          bCard5.colorChange("yellow")
        elif x[4] in cardstoremove:
          cardstoremove.pop(cardstoremove.index(x[4]))
          bCard5.colorChange("light blue")
    
    bCard1.colorChange("light blue")
    bCard2.colorChange("light blue")
    bCard3.colorChange("light blue")
    bCard4.colorChange("light blue")
    bCard5.colorChange("light blue")
    t11.undraw()
    
    if cardstoremove != []:
      t1.undraw()
      replacementcards = pokerDeck.deal(len(cardstoremove))
      for i in range(len(cardstoremove)):
        x[x.index(cardstoremove[i])] = replacementcards[0]
        replacementcards.pop(0)
      #repeat hand categorizing and displaying if cards have been removed 
      print(x)
      y = handType(x)
      p = Point(430, 200)
      n=0
      for card in x:
        card = "cards/" + card + ".gif"
        c1= Image(p, card)
        c1.draw(w)
        list1.append(c1)
        n += 30
        p = Point(430 + n, 200)
      msg = ""
      msg2 = " hand with high card"
      msg3 = ""
      if 0 <= y[0] <= 8:
        msg = handnames[y[0]]
      if 0<= y[1] <= 14:
        msg3 = valuestocards[y[1]]
      msgfull = msg + msg2 + msg3
      t1 = Text(Point(500,60), msgfull)
      t1.draw(w)

    cardstoremove = []

    if y[0] == 0:
      earned = moneyEarned(betValue, -1)
      balance = moneyGet(balance, betValue, -1)
    elif y[0] == 1 and y[1] < 11:
      earned = moneyEarned(betValue, -1)
      balance = moneyGet(balance, betValue, -1)
    elif y[0] == 1 and y[1] >= 11:
      balance = moneyGet(balance, betValue, 1)
      earned = moneyEarned(betValue, 1)
    elif y[0] == 2:
      balance = moneyGet(balance, betValue, 2)
      earned = moneyEarned(betValue, 2)
    elif y[0] == 3:
      balance = moneyGet(balance, betValue, 3)
      earned = moneyEarned(betValue, 3)
    elif y[0] == 4:
      balance = moneyGet(balance, betValue, 4)
      earned = moneyEarned(betValue, 4)
    elif y[0] == 5:
      balance = moneyGet(balance, betValue, 6)
      earned = moneyEarned(betValue, 6)
    elif y[0] == 6:
      balance = moneyGet(balance, betValue, 9)
      earned = moneyEarned(betValue, 9)
    elif y[0] == 7:
      balance = moneyGet(balance, betValue, 25)
      earned = moneyEarned(betValue, 25)
    elif y[0] ==8 and y[1] == 14:
      balance = moneyGet(balance, betValue, 250)
      earned = moneyEarned(betValue, 250)
    elif y[0] == 8:
      balance = moneyGet(balance, betValue, 50)
      earned = moneyEarned(betValue, 50)
    
    if earned >= 0:
      t6 = Text(Point(500, 100), "+ $" + str(earned))
      t6.setFill("green")
    elif earned < 0:
      t6 = Text(Point(500, 100), "- $" + str(-1 * earned))
      t6.setFill("red")
    t6.draw(w)
    bDeal.deactivate()
    sleep(1.5)
    bDeal.activate()
    t6.undraw()
    t3.undraw()
    t3 = Text(Point(130, 148), "Current Balance: $" + str(balance))
    t3.setSize(8)
    t3.draw(w)
    if balance == 0:
      tlose = Text(Point(500, 100), "You lose! Click anywhere other than the quit button to play again.")
      tlose.setSize(10)
      tlose.draw(w)
      pcontinue = w.getMouse()
      if not bQuit.clicked(pcontinue):
        balance = 100
        t3.undraw()
        t3 = Text(Point(130, 148), "Current Balance: $" + str(balance))
        t3.setSize(8)
        t3.draw(w)
        tlose.undraw()
        t1.undraw()
        for item in list1:
          item.undraw()
        continue
      w.close()
      break
    

  if bQuit.clicked(p1):
    for i in list1:
      i.undraw()
    t1.undraw()
    print("Thanks for Playing!")
    w.close()
    break