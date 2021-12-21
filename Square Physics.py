import pygame; import keyboard; from sys import exit

pygame.init()
pygame.display.set_caption('Square Physics')
screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()

square = pygame.Surface((75, 75))
square_x = 100; square_y = 400
square.fill((0, 255, 0))

floor = pygame.Surface((1000, 25))
floor.fill((0, 0, 255))

platform = pygame.Surface((60, 125))
platform_x = 800; platform_y = 350
platform.fill((100, 0, 100))

jumping = False
jumping_strenght = 0
on_platform = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))
    screen.blit(floor, (0, 475))
    screen.blit(platform, (platform_x, platform_y))
    screen.blit(square, (square_x, square_y))

    if keyboard.is_pressed('left'):
        if square_y > platform_y - 53 and abs(square_x - platform_x + 8) < 70:
            if keyboard.is_pressed('left') and square_x < platform_x:
                square_x -= 3
        else:
            square_x -= 3

    if keyboard.is_pressed('right'):
        if square_y > platform_y - 53 and abs(square_x - platform_x + 8) < 70:
            if keyboard.is_pressed('right') and square_x > platform_x:
                square_x += 3
        else:
            square_x += 3

    if keyboard.is_pressed('up'):
        if square_y == 400 or square_y < platform_y - 73:
            jumping = True

    if square_y <= 400:
        if jumping:
            square_y -= 10 - jumping_strenght
            jumping_strenght += 0.25

        if square_y >= 399 and jumping_strenght > 5:
            square_y = 400
            jumping = False
            jumping_strenght = 0

    if square_y > platform_y - 80 and abs(square_x - platform_x + 8) < 73 and square_y < platform_y - 73:
        jumping = False
        jumping_strenght = 0
        on_platform = True

    else:
        if on_platform:
            if not jumping:
                if square_y < 400:
                    square_y += 6.5
                else:
                    square_y = 400
                    on_platform = False

    if square_x < -75:
        square_x = 1000

    if square_x > 1000:
        square_x = -75

    clock.tick(120)
    pygame.display.update()
