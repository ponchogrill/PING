import pygame
import sys
 
FPS = 90
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1020
BAT_WIDTH = 20
BAT_HEIGHT = 120
BAT_OFFSET = 10
ROK_WIDTH = 20
ROK_HEIGHT = 120
ROK_OFFSET = 10
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
 
clock = pygame.time.Clock()
sc = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT))
 
# радиус будущего круга
r = 20
# координаты круга
ball_x = SCREEN_WIDTH//2
ball_y = SCREEN_HEIGHT // 2
#скорости мячя
ball_speed_x = 3
ball_speed_y = 1
#координаты ракетки
#левая
bat_x = BAT_OFFSET
bat_y = (SCREEN_HEIGHT - BAT_HEIGHT) // 2
#правая
rok_x = SCREEN_WIDTH - ROK_OFFSET
rok_y = (SCREEN_HEIGHT - ROK_HEIGHT) // 2
#скорость ракетки
bat_speed_y = 0
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #передвигаем мяч по экрану
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    #выход за края экрана
    #левый
    if ball_x <= r:
        ball_speed_x = -ball_speed_x
    #правый
    if ball_x >= SCREEN_WIDTH -r:
        #летел на право-полетел на лево
        ball_speed_x = -ball_speed_x
    if ball_y <= r:
        ball_speed_y = -ball_speed_y
    #правый
    if ball_y >= SCREEN_HEIGHT -r:
        #летел на право-полетел на лево
        ball_speed_y = -ball_speed_y
    #передвигаем ракетку по экрану
    #левая
    keys = pygame.key.get_pressed()
    bat_y +=bat_speed_y
    if keys[pygame.K_w]:
        bat_y -= 3
    elif keys[pygame.K_s ]:
        bat_y += 3
    if bat_y <= 0:
        bat_y = 0
    elif bat_y >= SCREEN_HEIGHT - BAT_HEIGHT:
        bat_y = SCREEN_HEIGHT - BAT_HEIGHT
    #правая
        keys = pygame.key.get_pressed()
    bat_y +=bat_speed_y
    if keys[pygame.K_UP]:
        bat_y -= 3
    elif keys[pygame.K_DOWN ]:
        bat_y += 3
    if bat_y <= 0:
        bat_y = 0
    elif bat_y >= SCREEN_HEIGHT - BAT_HEIGHT:
        bat_y = SCREEN_HEIGHT - BAT_HEIGHT
    # заливаем фон
    sc.fill(WHITE)
    # рисуем круг
    pygame.draw.circle(sc, ORANGE,(ball_x, ball_y), r)
    pygame.draw.rect(sc, ORANGE, (bat_x, bat_y, BAT_WIDTH, BAT_HEIGHT))
    pygame.draw.rect(sc, ORANGE, (rok_x, rok_y, ROK_WIDTH, ROK_HEIGHT))
    # обновляем окно
    pygame.display.update()
    clock.tick(FPS)
