import pygame
import time

# screen size 
WINDOW_W = 500
WINDOW_H = 228
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

IMAGE= 'img_forest.jpg'

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("My First Game!")

#fill screen and show
img= pygame.image.load(IMAGE)

clock= pygame.time.Clock()

circle_x= 10
circle_y= WINDOW_H/2
x_step= 10

play = True
while play:
  screen.blit(img, (0,0))    
  pygame.draw.circle(screen, (255,255,255), (circle_x, circle_y), 10)
  circle_x += x_step
  if circle_x > WINDOW_W:
    x_step= -10
  if circle_x < 0:
    x_step= 10
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False
  clock.tick(20)

pygame.quit()
