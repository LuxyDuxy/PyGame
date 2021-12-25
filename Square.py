import pygame, keyboard
pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
square_height = int(input('Square height: '))
square_width = int(input('Square width: '))
platform_0_height = int(input('Platform height: '))
platform_0_width = int(input('Platform width: '))
square = pygame.Rect(100, 600 - square_height, square_width, square_height)
platform_0 = pygame.Rect(700, 400, platform_0_width, platform_0_height)
jumping = False
jumping_strenght = 0.5
square_top_side_collision = False
off_platform = False
on_platform = False
left_side_of_platform = False
right_side_of_platform = False
square_y_fix = False
while True:
    screen.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
    if abs(square.right - platform_0.left) < 10:
            square_right_side_collision = True
    elif abs(square.left - platform_0.right) < 10:
        square_left_side_collision = True 
    if jumping:
        square.y -= 12 - jumping_strenght   
        jumping_strenght += 0.3 
    if square.colliderect(platform_0):
        pass
    else:
        square_right_side_collision = False
        square_left_side_collision = False  
        square_top_side_collision = False  
        off_platform = True 
    if abs(square.y - (platform_0.y + platform_0.height)) < 6 and square.x - platform_0.x > 50 and square.x - platform_0.x < platform_0.width or abs(square.y - (platform_0.y + platform_0.height)) < 6 and square.x - platform_0.x < platform_0.width and square.x - platform_0.x > -square.width:
        jumping_strenght = 16
        if not square_y_fix:
            square_y_fix = True
    if abs(square.y - (platform_0.y - square.height)) <= 6 and square.x - platform_0.x >= square.width * -1 and not square.x - platform_0.x > 0 and jumping_strenght > 12:
        left_side_of_platform = True 
        square.y = platform_0.y - square.height
        square_top_side_collision = True
        square_right_side_collision = False
        square_left_side_collision = False 
        off_platform = False
        if not on_platform:
            on_platform = True
        jumping_strenght = 14
    else:
        left_side_of_platform = False
        if right_side_of_platform:
            pass
        else:
            square_top_side_collision = False
            off_platform = True
    if abs(square.y - (platform_0.y - square.height)) <= 6 and abs(square.x - platform_0.x) <= platform_0.width and not square.x - platform_0.x < 0 and jumping_strenght > 12:
        right_side_of_platform = True 
        square.y = platform_0.y - square.height
        square_top_side_collision = True
        square_right_side_collision = False
        square_left_side_collision = False 
        off_platform = False
        if not on_platform:
            on_platform = True
        jumping_strenght = 14
    else:
        right_side_of_platform = False
        if left_side_of_platform:
            pass
        else:
            square_top_side_collision = False
            off_platform = True
    if keyboard.is_pressed('left') and not square_left_side_collision:
        square.x -= 3
    if keyboard.is_pressed('right') and not square_right_side_collision:
        square.x += 3  
    if not jumping and off_platform and on_platform:
        on_platform = False
        jumping = True
    if keyboard.is_pressed('up') and not jumping:
        jumping_strenght = 0.5
        jumping = True
    if square.y >= 600 - square_height and jumping_strenght > 5:
        on_platform = False
        jumping = False
        jumping_strenght = 0.5
        square.y = 600 - square_height
        square_y_fix = False
    if square.x <= 0 - square_width:
        square.x = 1000
    elif square.x >= 1000:
        square.x = 0 - square_width
    if jumping and square_top_side_collision and jumping_strenght > 10:
        jumping = False
    pygame.draw.rect(screen, (100, 0, 100), platform_0)
    pygame.draw.rect(screen, (0, 100, 200), square)
    pygame.display.flip()            
    clock.tick(120)
