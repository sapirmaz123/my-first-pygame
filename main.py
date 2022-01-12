import pygame
import time

# screen size 
WINDOW_W = 500
WINDOW_H = 228
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

IMAGE= 'background.jpg'

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("My First Game")

#fill screen and show
img= pygame.image.load(IMAGE)

play = True
while play:
  screen.blit(img, (0,0))
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False

pygame.quit()
