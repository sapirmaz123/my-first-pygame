import pygame
import time

# screen size 
WINDOW_W = 500
WINDOW_H = 228
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

IMAGE= 'img_forest.jpg'

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("My First Game! ")

#fill screen and show
img= pygame.image.load(IMAGE)


play = True
while play:
  screen.blit(img, (0,0))    
  for i in range (0, WINDOW_H, 30):
    pygame.draw.line(screen, (255,255,255), [0,i], [WINDOW_W,i], width=4)
  for j in range (0, WINDOW_W, 30):
    pygame.draw.line(screen, (255,255,255), [j,0], [j,WINDOW_W], width=4)
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False


pygame.quit()
