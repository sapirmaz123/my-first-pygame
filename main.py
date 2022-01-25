import pygame
import time

# screen size
WINDOW_W = 500
WINDOW_H = 228
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("My First Game!")

# fill screen and show
background = pygame.image.load('space.jpg')
ship_image = pygame.image.load('spaceship.png')
ship_image = pygame.transform.scale(ship_image, (50, 80))
laser_image = pygame.image.load('laser.png')
laser_image = pygame.transform.scale(laser_image, (20, 30))


clock = pygame.time.Clock()

circle_x = 10
circle_y = WINDOW_H/2
x_step = 10
play = True
ship_x = WINDOW_W / 2
ship_y = WINDOW_H - 80
laser_x= -100
laser_y= -100

while play:
    pygame.draw.circle(screen, (255, 255, 255), (circle_x, circle_y), 10)
    circle_x += x_step
    if circle_x > WINDOW_W:
        x_step = -10
    if circle_x < 0:
        x_step = 10
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship_x -= 10
            if event.key == pygame.K_RIGHT:
                ship_x += 10
            if event.key == pygame.K_SPACE:
                laser_x = ship_x + 16
                laser_y = ship_y
    screen.blit(background, (0, 0))
    laser_y -= 16
    screen.blit(ship_image, (ship_x, ship_y))
    screen.blit(laser_image, (laser_x, laser_y))

    clock.tick(20)

pygame.quit()
