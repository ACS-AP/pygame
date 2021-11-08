# Import and initialize pygame
import pygame
pygame.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])
# Creat the game loop
running = True

class GameObject(pygame.sprite.Sprite):
  # Remove width and height and add image here!
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    # self.surf = pygame.Surface((width, height)) REMOVE!
    # self.surf.fill((255, 0, 255)) REMOVE!
    self.surf = pygame.image.load(image) # ADD!
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

#box = GameObject(120, 300, 50, 50)
apple = GameObject(120, 300, 'apple.png') # ADD!
apple.render(screen) # ADD!

while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  # Draw a circle
  screen.fill((255, 255, 255))

  box.render(screen)
  # Update the window
  pygame.display.flip()

  # Configure the screen
screen = pygame.display.set_mode([500, 500])

# Clear screen
screen.fill((255, 255, 255))

def render(self, screen):
  screen.blit(self.surf, (self.x, self.y))



