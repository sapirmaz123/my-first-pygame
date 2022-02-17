import pygame #ליבא ספריה של pygame
import time #ליבא ספריה של זמן  
import cv

# screen size
WINDOW_W = 800 #הגדרת רוחב מסך
WINDOW_H = 500 #הגדרת גובה מסך
WINDOW_SIZE = (WINDOW_W, WINDOW_H) #טאפל של גודל המסך

pygame.init() #התחלה
screen = pygame.display.set_mode(WINDOW_SIZE) #הצגת המסך שהגדרנו
pygame.display.set_caption("My First Game!") #הצגת כותרת המשחק

# fill screen and show
background = pygame.image.load('space.jpg') #העלאת הרקע ושמירה במשתנה
ship_image = pygame.image.load('spaceship.png') #העלאת החללית ושמירה במשתנה
ship_image = pygame.transform.scale(ship_image, (50, 80)) #שמירת החללית בגודל הרצוי
laser_image = pygame.image.load('laser.png') #העלאת הלייזר ושמירה במשתנה
laser_image = pygame.transform.scale(laser_image, (20, 30)) #שמירת הלייזר בגודל הרצוי

# add sound
gun_shoot="Gun_shoot.mp3" #שמירת הסאונד במשתנה
success= "winning.mp3"
pygame.mixer.init() #התחלת סאונד
pygame.mixer.music.load(gun_shoot) #העלאה של הסאונד
pygame.mixer.music.load(success) 


clock = pygame.time.Clock() #הגדרת שעון  

def is_laser_hit(laser_pos):
  return abs(laser_pos[0]-circle_x) <50 and abs(laser_pos[1]-circle_y) <50 
    

laser_list = []
# prints all the laser on the screen
def print_lasers():
  for i in range(len(laser_list)):
    laser = laser_list[i]
    screen.blit(laser_image,(laser[0],laser[1]))
    laser_list[i] = [laser[0],laser[1]-30]
    if is_laser_hit(laser): 
      return True

  # remove lazer that our outside of the window
  if len(laser_list) > 0 and laser_list[0][1] < 0:
    laser_list.remove(laser_list[0])

pygame.font.init() 

counter= 0
circle_x = 10 #ציר האיקס של הכדור
circle_y = WINDOW_H/2 #ציר הווי של הכדור (גובה המסך/ 2)
x_step = 10 #צעדים בציר האיקס של הכדור
ship_x = WINDOW_W / 2 #ציר האיקס של החללית (רוחב המסך/ 2)
ship_y = WINDOW_H - 80 #ציר הווי של החללית (גובה המסך - גובה החללית)
laser_x= -100  #הגדרת ציר האיקס של הלייזר כך שלא יראו אותו
laser_y= -100  #הגדרת ציר האיקס של הלייזר כך שלא יראו אותו
play = True 

while play:
    pygame.draw.circle(screen, (255, 255, 255), (circle_x, circle_y), 10) #ציור עיגול (מסך, צבע לבן, מיקום שהגדרנו, רדיוס)
    circle_x += x_step #הגדלת ציר האיקס של הכדור כדי שיזוז לפי הצעדים שהגדרנו
    if circle_x > WINDOW_W: #אם ציר האיקס של הכדור גדול מרוחב המסך
        x_step = -10 #הקטנת ציר האיקס של הכדור כל פעם ב10
    if circle_x < 0: #אם ציר האיקס של הכדור קטן מ0
        x_step = 10 #הגדלת ציר האיקס של הכדור כל פעם ב10
    pygame.display.flip() #הצגת הכדור על המסך
    for event in pygame.event.get(): #לולאה של כל האירועים שיכולים לקרות על המסך
        if event.type == pygame.QUIT: #אם סוג האירוע הוא לחיצה על יציאה
            play = False #שינוי המשתנה לשקר ויציאה מהלולאה כך שהתוכנית תיסגר
        elif event.type == pygame.KEYDOWN: #אם סוג האירוע הוא לחיצה על מקש
            if event.key == pygame.K_LEFT: #אם הלחיצה היא על המקש שמאלה
                ship_x -= 10 #ציר האיקס של החללית יקטן ב10
            if event.key == pygame.K_RIGHT: #אם הלחיצה היא על המקש ימינה
                ship_x += 10 #ציר האיקס של החללית יגדל ב10
            if event.key == pygame.K_SPACE: #אם הלחיצה היא על מקש הרווח
                pygame.mixer.Channel(0).play(pygame.mixer.Sound(gun_shoot)) # פתיחת ערוץ למקרה שנוסיף עוד סאונד וניגון של הסאונד
                laser_list.append([ship_x+16,ship_y])

    screen.blit(background, (0, 0)) #הצגת הרקע 
    # laser_y -= 10 #הקטנת ציר הווי של הלייזר כדי שיזוז למעלה
    screen.blit(ship_image, (ship_x, ship_y)) #הצגת החללית במיקום שהגדרנו
    if print_lasers():
        circle_x= 10
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(success))
        counter+=10

    red = (150, 0, 0)
    font = pygame.font.SysFont(None, 50)
    img = font.render('score: '+ str(counter), True, red)
    screen.blit(img, (20, 20))

    clock.tick(40) #קצב החזרה של הלולאה

pygame.quit() #סיום התוכנית
