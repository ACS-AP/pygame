import pygame
pygame.init()

# configure the screen
screen = pygame.display.set_mode([500, 500])

# creating game loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # clear screen
  screen.fill((13, 17, 24))

  for index in range(9):
    # draw circle
    color = (78, 78, 78)
    x = ((index % 3) * 175) + 75
    y = (int(index / 3) * 175) + 75
    position = (x, y)

    pygame.draw.circle(screen, color, position, 50)
    
  # update display
  pygame.display.flip()

  

