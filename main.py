import pygame #ליבא ספריה של pygame
import time #ליבא ספריה של זמן  

# screen size
WINDOW_W = 500 #הגדרת רוחב מסך
WINDOW_H = 228 #הגדרת גובה מסך
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
pygame.mixer.init() #התחלת סאונד
pygame.mixer.music.load(gun_shoot) #העלאה של הסאונד


clock = pygame.time.Clock() #הגדרת שעון 

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
                laser_x = ship_x + 16 #ציר האיקס של הלייזר= לציר האיקס של החללית+ חצי מגודל החללית (כך שיצא מאמצע החללית)
                laser_y = ship_y #ציר הווי של הלייזר= לציר הווי של החללית
                pygame.mixer.Channel(0).play(pygame.mixer.Sound(gun_shoot)) # פתיחת ערוץ למקרה שנוסיף עוד סאונד וניגון של הסאונד

    screen.blit(background, (0, 0)) #הצגת הרקע 
    laser_y -= 10 #הקטנת ציר הווי של הלייזר כדי שיזוז למעלה
    screen.blit(ship_image, (ship_x, ship_y)) #הצגת החללית במיקום שהגדרנו
    screen.blit(laser_image, (laser_x, laser_y)) #הצגת הלייזר במיקום שהגדרנו

    clock.tick(40) #קצב החזרה של הלולאה

pygame.quit() #סיום התוכנית
