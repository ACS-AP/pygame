from game_object import GameObject

# Player subclass of GameObject
class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'images/player.png')
    self.dx = 95
    self.dy = 95
    self.reset()

  def left(self):
    if self.dx <= 95:
      self.dx -= 0
    else:
      self.dx -= 125

  def right(self):
    if self.dx >= 345:
      self.dx += 0
    else:
      self.dx += 125

  def up(self):
    if self.dy <= 95:
      self.dy -= 0
    else:
      self.dy -= 125

  def down(self):
    if self.dy >= 345:
      self.dy += 0
    else:
      self.dy += 125
  
  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
    self.x = 250 - 32
    self.y = 250 - 32
