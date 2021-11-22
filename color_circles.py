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
  # draw circles
  color = (255, 59, 48)
  position = (75, 75)
  pygame.draw.circle(screen, color, position, 75)

  color = (255, 149, 0)
  position = (425, 75)
  pygame.draw.circle(screen, color, position, 75)

  color = (255, 204, 0)
  position = (250, 250)
  pygame.draw.circle(screen, color, position, 75)

  color = (76, 217, 100)
  position = (75, 425)
  pygame.draw.circle(screen, color, position, 75)

  color = (90, 200, 250)
  position = (425, 425)
  pygame.draw.circle(screen, color, position, 75)
  # update display
  pygame.display.flip()
  