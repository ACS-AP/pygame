import pygame
pygame.init()

#configure the screen
screen = pygame.display.set_mode([500, 500])
w, h = pygame.display.get_surface().get_size()

def draw_color_circles():
  blue = (20, 121, 199)
  red = (255, 0, 0)
  orange = (250, 141, 7)
  yellow = (255, 255, 0)
  green = (25, 184, 22)

  radius = 50

  top_left = (0 + radius, 0 + radius)
  top_right = (w - radius, radius)
  bottom_left = (radius, h - radius)
  bottom_right = (w - radius, h - radius)
  center = (w / 2, h / 2)

  pygame.draw.circle(screen, red, top_left, radius)
  pygame.draw.circle(screen, orange, top_right, radius)
  pygame.draw.circle(screen, yellow, center, radius)
  pygame.draw.circle(screen, green, bottom_left, radius)
  pygame.draw.circle(screen, blue, bottom_right, radius)

def draw_circle_grid():
  grey = (100, 100, 100)
  radius = 50
  for i in range(3):
    for j in range(3):
      pygame.draw.circle(screen, grey, (w * (i / 3) + radius, h * ((j % 3) / 3) + radius), radius)

""" 
0, 0
0, 250
0, 500
250, 0
250, 250
250, 500

0 / 3 = 0
1 / 3 = 0.33
2 / 3 = 0.66
3 / 3 = 1
4 / 3 = 1.33
5 / 3 = 1.66

0 % 3 = 0
1 % 3 = 1
2 % 3 = 2
3 % 3 = 0
4 % 3 = 1
5 % 3 = 2

500 / 1 / 3
 """

#game loop
running = True
while running: 
  #look at events
  for event in pygame.event.get():
    # close game window
    if event.type == pygame.QUIT:
      running = False

  #clear screen
  black = (0, 0, 0)
  screen.fill(black)
  
  #draw_color_circles()
  draw_circle_grid()

  #update the display
  pygame.display.flip()

  

