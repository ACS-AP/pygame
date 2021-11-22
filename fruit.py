from game_object import GameObject
from random import randint, choice

# Apple subclass of GameObject
class Apple(GameObject):
  def __init__(self):
    super(Apple, self).__init__(0, 0, 'src/images/apple.png')
    self.dx = 0
    self.dy = (randint(0, 200) / 100) + 1
    self.reset()

  def move(self):
    # self.x += self.dx
    self.y += self.dy

    if self.y > 500:
      self.reset()
        
  def reset(self):
    x_coordinates = [93, 218, 343]
    y_coordinates = [-64, 564]
    self.x = choice(x_coordinates)
    self.y = choice(y_coordinates)
  
# Strawberry subclass of GameObject
class Strawberry(GameObject):
  def __init__(self):
    super(Strawberry, self).__init__(0, 0, 'src/images/strawberry.png')
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = 0
    self.reset()

  def move(self):
    self.x += self.dx

    if self.x > 500:
      self.reset()
  
  def reset(self):
    x_coordinates = [-64, 564]
    y_coordinates = [93, 218, 343]
    self.x = choice(x_coordinates)
    self.y = choice(y_coordinates)
