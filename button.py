from graphics import *
class Button:
 def __init__(self, xpos, ypos, text, window, color):
  self.xpos = int(xpos)
  self.ypos = int(ypos)
  self.window = window
  self.text = text
  self.b1 = Rectangle(Point(self.xpos, self.ypos), Point(self.xpos + 80, self.ypos +80))
  self.t1 = Text(Point(self.xpos + 40, self.ypos + 40), text)
  self.t1.setFill("black")
  self.color = color
  self.b1.setFill(color)
  self.activated = True
  self.b1.draw(self.window)
  self.t1.draw(self.window)

 def clicked(self, testp):
   if self.activated == False:
     return False
   elif self.xpos < testp.getX() < (self.xpos +80) and self.ypos <testp.getY() <(self.ypos + 80):
     return True
  
 def thinClicked(self, testp2):
   if self.xpos < testp2.getX() < (self.xpos + 20) and self.ypos < testp2.getY() < (self.ypos + 46):
     return True
  
 def deactivate(self):
    self.activated = False
    self.t1.setFill("gray")
  
 def activate(self):
    self.activated = True
    self.t1.setFill("black")

 def fontSize(self, newsize):
   self.t1.undraw()
   self.t1.setSize(newsize)
   self.t1.draw(self.window)
  
 def makeThin(self):
   self.b1.undraw()
   self.t1.undraw()
   self.b1 = Rectangle(Point(self.xpos, self.ypos), Point(self.xpos + 20, self.ypos + 46))
   self.b1.setFill(self.color)
   self.b1.draw(self.window)
   self.t1 = Text(Point(self.xpos + 10, self.ypos + 23), self.text)
   self.t1.draw(self.window)
  
 def makeLong(self):
   self.b1.undraw()
   self.t1.undraw()
   self.b1 = Rectangle(Point(self.xpos, self.ypos), Point(self.xpos + 140, self.ypos + 20))
   self.b1.setFill(self.color)
   self.b1.draw(self.window)
   self.t1 = Text(Point(self.xpos + 70, self.ypos + 10), self.text)
   self.t1.draw(self.window)
 
 def colorChange(self, newcolor):
   self.b1.undraw()
   self.t1.undraw()
   self.b1.setFill(newcolor)
   self.b1.draw(self.window)
   self.t1.draw(self.window)