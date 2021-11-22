import pygame
from fruit import Apple, Strawberry
from player import Player
from bomb import Bomb
from random import randint

pygame.init()
screen = pygame.display.set_mode([500, 500])
myfont = pygame.font.SysFont('Comic Sans', 30)

level_one = pygame.image.load('images/bg1.jpeg')
level_two = pygame.image.load('images/bg2.jpeg')
level_three = pygame.image.load('images/bg3.jpeg')
level_four = pygame.image.load('images/bg4.jpeg')
level_five = pygame.image.load('images/bg5.jpeg')

clock = pygame.time.Clock()
apple = Apple()
strawberry = Strawberry()
player = Player()
bomb = Bomb()
bomb2 = Bomb()
collected = 0

running = True
while running:
  screen.fill((0, 0, 0))
  screen.blit(level_three, [0, 0])
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    # Check for event type KEYBOARD
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
      elif event.key == pygame.K_RIGHT:
        player.right()
      elif event.key == pygame.K_UP:
        player.up()
      elif event.key == pygame.K_DOWN:
        player.down()
  
  all_sprites = pygame.sprite.Group()
  all_sprites.add(player)
  all_sprites.add(apple)
  all_sprites.add(strawberry)
  all_sprites.add(bomb)

  fruit_sprites = pygame.sprite.Group()
  fruit_sprites.add(apple)
  fruit_sprites.add(strawberry)

  if collected == 2:
    all_sprites.add(bomb2)
    
  for entity in all_sprites:
    entity.move()
    entity.render(screen)

    fruit = pygame.sprite.spritecollideany(player, fruit_sprites, pygame.sprite.collide_rect_ratio(.85))
    if fruit:
      fruit.reset()
      collected += 1
      apple.dy += 0.05
      strawberry.dx += 0.05

    if pygame.sprite.collide_rect_ratio(.85)(player, bomb):
      bomb.reset()
      player.dx = 220
      player.dy = 220
      apple.reset()
      apple.dy = (randint(0, 200) / 100) + 1
      strawberry.reset()
      strawberry.dx = (randint(0, 200) / 100) + 1
      collected = 0
      # running = False

    score_obj = myfont.render(f'Collected: {collected}', True, (0, 0, 0))
    screen.blit(score_obj, (25, 450))

  pygame.display.flip()
  clock.tick(60)


apple = Apple()
strawberry = Strawberry()

#player
class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, './images/player.png')
    self.dx = 0
    self.dy = 0
    self.pos_x = 1
    self.pos_y = 1
    self.reset()

  def left(self):
    if self.pos_x > 0:
      self.pos_x -= 1
      self.update_dx_dy()

  def right(self):
    if self.pos_x < len(x_lanes) - 1:
      self.pos_x += 1
      self.update_dx_dy()

  def up(self):
    if self.pos_y > 0:
      self.pos_y -= 1
      self.update_dx_dy()

  def down(self): 
    if self.pos_y < len(y_lanes) - 1:
      self.pos_y += 1
      self.update_dx_dy()

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
    self.x = x_lanes[self.pos_x]
    self.y = y_lanes[self.pos_y]
    self.dx = self.x
    self.dy = self.y

  def update_dx_dy(self):
    self.dx = x_lanes[self.pos_x]
    self.dy = y_lanes[self.pos_y]

player = Player()

#make a group
all_sprites = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)

#game loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        player.left()
      elif event.key == pygame.K_RIGHT:
        player.right()
      elif event.key == pygame.K_UP:
        player.up()
      elif event.key == pygame.K_DOWN:
        player.down()
      
  fill_color = (0, 0, 0)
  screen.fill(fill_color)

  for entity in all_sprites:
    entity.move()
    entity.render(screen)

  #update window
  pygame.display.flip()
  #clock
  clock.tick(60)

