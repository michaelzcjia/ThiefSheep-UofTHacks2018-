import sys, pygame
from GameFiles import Character as char

pygame.init()

size = width, height = 1000, 700
screen = pygame.display.set_mode(size)

black = 0, 0, 0
green = 95, 142, 41

# MAKE AUTOSHEEP SWARM
numSheep = 60
sheepSwarm = []

for sheep in range(numSheep):
    newSheep = char.autoSheep();
    newSheep.sheep = pygame.transform.scale(newSheep.sheep,(100,100))
    sheepSwarm.append(newSheep)

# sheep player tings

ling = char.autoSheep()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    for sheep in sheepSwarm:
        sheep.update()

        sheepPos = sheep.sheepRect
        #print(sheep.speed)

        if sheepPos.left < 0 or sheepPos.right > width:
            sheep.x_speed = -sheep.x_speed
            #print(sheep.speed, sheep.sheepRect)  # personal check

        if sheepPos.top < 0 or sheepPos.bottom > height:
            sheep.y_speed = -sheep.y_speed
            #print(sheep.speed, sheep.sheepRect)  # personal check

        screen.blit(sheep.sheep, sheep.sheepRect)

    pygame.display.flip()
    screen.fill(green)

   # ling.update()  # sheep moves
   #
   #  ling_pos = ling.sheepRect  # sheep position
   #
   #  if ling_pos.left < 0 or ling_pos.right > width:
   #      ling.x_speed = -ling.x_speed
   #      print(ling.speed, ling.sheepRect)  # personal check
   #
   #  if ling_pos.top < 0 or ling_pos.bottom > height:
   #      ling.y_speed = -ling.y_speed
   #      print(ling.speed, ling.sheepRect)  # personal check
   #

   #  screen.blit(ling.sheep, ling.sheepRect)
    #pygame.display.flip()

#
# speed1 = [2.5, 2]
# speed2 = [4, 4]
# speed3 = [6,3]
# speeds = [speed1, speed2, speed3]

# sheepSpecs = ()

# ball = pygame.image.load("Sprites/sheep.png")
# ballrect = ball.get_rect()
# ballrect2 = ball.get_rect()
# ballrect3 = ball.get_rect()
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
#
#     ballrect = ballrect.move(speed1)
#     ballrect2 = ballrect2.move(speed2)
#     ballrect3 = ballrect3.move(speed3)
#
#     sheepList = [ballrect, ballrect2, ballrect3]
#
#     spec = (sheepList, speeds)
#     for i in range(3):
#             if spec[0][i].left < 0 or spec[0][i].right > width:
#                 spec[1][i][0] = -spec[1][i][0]
#             if spec[0][i].top < 0 or spec[0][i].bottom > height:
#                 spec[1][i][1] = -spec[1][i][1]
#
#
#     screen.fill(black)
#     screen.blit(ball, ballrect3)
#     screen.blit(ball, ballrect2)
#     screen.blit(ball, ballrect)
#     pygame.display.flip()