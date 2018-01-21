import sys, pygame
pygame.init()

size = width, height = 1800, 900

speed1 = [2.5, 2]
speed2 = [4, 4]
speed3 = [6,3]
black = 0, 0, 0
speeds = [speed1, speed2, speed3]

sheepSpecs = ()

screen = pygame.display.set_mode(size)

ball = pygame.image.load("sheep.png")
ballrect = ball.get_rect()
ballrect2 = ball.get_rect()
ballrect3 = ball.get_rect()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed1)
    ballrect2 = ballrect2.move(speed2)
    ballrect3 = ballrect3.move(speed3)

    sheepList = [ballrect, ballrect2, ballrect3]

    spec = (sheepList, speeds)
    for i in range(3):
            if spec[0][i].left < 0 or spec[0][i].right > width:
                spec[1][i][0] = -spec[1][i][0]
            if spec[0][i].top < 0 or spec[0][i].bottom > height:
                spec[1][i][1] = -spec[1][i][1]


    screen.fill(black)
    screen.blit(ball, ballrect3)
    screen.blit(ball, ballrect2)
    screen.blit(ball, ballrect)
    pygame.display.flip()