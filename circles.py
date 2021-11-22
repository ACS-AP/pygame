import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

#Game Loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
 
  screen.fill((0, 0, 0))

  for index in range(9):

    color = (78, 78, 78)
    x = ((index % 3) * 175) + 75
    y = (int(index / 3) * 175) + 75
    position = (x, y)

    pygame.draw.circle(screen, color, position, 50)
    
  pygame.display.flip()

  

