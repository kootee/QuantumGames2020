import pew
import microqiskit
from map import level

pew.init()
screen = pew.Pix()
ammo = 8
world_x = 1
world_y = 1
grid_location = 5
grid = level

#displays screen based on "world coordinates"
def update_screen(grid_location):
    #cells = [i for i in range((grid_location * 8 - 8),(grid_location * 8))]
    current_screen = [grid[i] for i in range((grid_location * 8 - 8),(grid_location * 8))]
    print(current_screen)
    return current_screen

current_screen = update_screen(grid_location)
screen = pew.Pix.from_iter(current_screen)

status = True
#initial state of player
x = 1
y = 1

'''End game (not working yet), 
shows the text GAME OVER! and the stats. 
Game ends when you press X'''
def end_game():
    print('you are out of ammo')
    text = pew.Pix.from_text('Game over!') #text will be shown when game ends also shwoing stat
    for a in range(-8, text.width):
        screen.blit(text, -a, 1)
    pew.show(screen)
    return False

def catch(s):
    s -= 1
    print('you tried to catch a ghost')
    screen.pixel(7 - s, 7, 2)
    return s
    #this should trigger the catching process ie creating the entangled photons

def update_pixels(dx, dy): #loop through the pixels and update them to show map
    
    if y > 5 and dy == 1:
        print('y bigger than five') 
        for i in range(8):
            for j in range(8):
                if i == 7:
                    pic_before = grid[i + world_y][j]
                    print(pic_before)
                    print(grid[i + world_y][j])
                else:
                    pic_before = screen.pixel(i, j + 1)
                
                screen.pixel(i,j,pic_before)
    
    elif y < 2 and dy == -1:
        print('y smaller than two')
        for i in range(8):
            for j in range(8):
                pic_before = screen.pixel(i, j - 1)
                screen.pixel(i,j,pic_before)
    
    elif x > 5 and dx == 1:
        print('x bigger than five')
        for i in range(8):
            for j in range(8):
                pic_before = screen.pixel(i + 1, j)
                screen.pixel(i,j,pic_before)
    
    elif x < 2 and dx == -1:
        print('x smaller than two')
        for i in range(8):
            for j in range(8):
                x_prev_pix = i - 1
                y_prev_pix = j
                if x_prev_pix < 0:
                    print('going offscreen')
                    pic_before = screen.pixel(x_prev_pix, y_prev_pix)
                    #look at coord
                else:
                    pic_before = screen.pixel(x_prev_pix, y_prev_pix)
                print('i:', i, 'j:', j)
                print('color', pic_before)
                #screen.pixel(i,j,pic_before)
    
    print('no update')
    # - dx or dy
 
    """
                    pic_before = screen.pixel(i - 1, j)
                print('i:', i, 'j:', j)
                print('color', pic_before)
                screen.pixel(i,j,pic_before)
    for i in range(8:
       for j in range(8):
           pic_before = 
           pic_after =
     for i in range(8):
        for j in range(8):
        if j < 7:
            screen.pixel(i,j,0)
        else:
            screen.pixel(i,j,3)
    """

while status:
    screen.pixel(x,y,0)
    keys = pew.keys()
    dx = 0
    dy = 0

    #arrow key controls
    if keys & pew.K_UP:
        dy = -1
    elif keys & pew.K_DOWN:
        dy = 1
    elif keys & pew.K_LEFT:
        dx = -1
    elif keys & pew.K_RIGHT:
        dx = 1
    elif keys & pew.K_X:
        status = False

    target = screen.pixel(x + dx ,y + dy)
    #criteria for the movement of the character
    if target == 0: #move to empty spot if character is in accepptable spot
        if dx == -1 and x > 1:
            x += dx
        elif dx == 1 and x < 6:
            x += dx
        if dy == -1 and y > 1:
            y += dy
        elif dy == 1 and y < 6:
            y += dy        
        if dx != 0 or dy != 0:
            print('x and y:', x , y)
            print('dx and dy', dx , dy)
            update_pixels(dx,dy)
        world_x += dx
        world_y += dy
        print('world coordinates', world_x, world_y)
    elif target == 3:
        print('door')#a door to a different floor TODO move to a different floor
    elif target == 2:
        print('you have ', ammo, 'shots left') #TODO catching the ghost
        ammo = catch(ammo)
    if ammo == 0:
        status = end_game()

    #if either the x or the y go <0 or 8< the map has to move 
    print('updating character location to ', x , y)
    screen.pixel(x,y,1)
    pew.show(screen)
    pew.tick(1/6)