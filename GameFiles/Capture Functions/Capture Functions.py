# Capture Function for Shepard

capture_tokens = 3 #to be put under class function for shepherd

def capture(self):

    kDict = pg.key.get_pressed()
    if (kDict[pg.K_RSHIFT] != 0):
        if (capture_tokens > 0): #Right now I have the capture tokens under the class definition, might have to put under player class

            # When rightshift key is pressed, activates capture function if token >0

            # Get current position of the Shephard, using placeholder image var
            shepherd_rect = shephard .get_rect()
            shepherd_x = shepherd_rect.x
            shepherd_y = shepherd_rect.y

            # Gets position of all sheep (including evil sheep)
            # and eliminates all sheep within the range of the shephard

            for sheep in sheepSwarm:
                x = sheep.x
                y = sheep.y
                if ((shepherd_x - 40) <= x <= (shepherd_x + 40) and (shepherd_y - 40) >= y >= (shepherd_y + 40)):
                    sheepSwarm.remove(sheep)
            capture_tokens -= 1
    return

#Wrecking Function for Rude Sheep

def wreck_item(self):
    kDict = pg.key.get_pressed()
    if (kDict[pg.K_x] != 0):

            # When x key is pressed, activates capture function if token >0

            # Get current position of the rudesheep, using placeholder image var
            sheep_rect = sheep.get_rect()
            sheep_x = sheep_rect.x
            sheep_y = sheep_rect.y

            # Gets position of items
            # and wrecks items within range of the rude sheep

            for item in items:  # PlaceHolder
                x = item.x
                y = item.y
                if ((sheep_x - 40) <= x <= (sheep_x + 40) and (sheep_y - 40) >= y >= (sheep_y + 40)):
                    Placeholder.remove(item)
                    #here we will replace it with the new image of the wrecked shit

    return