import pew


pew.init()
screen = pew.Pix()

for i in range(8):
    for j in range(8):
        screen.pixel(i,j,0)

screen.pixel(5,5,3)
x = 0
y = 0

while True:
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

    target = screen.pixel(x + dx ,y + dy)
    #constrains the movement of the character
    if target == 0: #move to empty spot
        x += dx
        y += dy
    elif target == 3:
        print('door')
        #a door to a different floor
    screen.pixel(x,y,3)
    pew.show(screen)
    pew.tick(1/6)