'''
* Controls:
    - Click on the Pygame window to ensure your inputs are captured
    - Use the arrow keys for ▲ ▼ ◀︎ and ►
    - Use the 'x' key for X and the 'd' key for O
'''

import pew
'''from microqiskit import QuantumCircuit, simulate
from math import pi
from random import random'''

pew.init()
screen = pew.Pix()

for X in range(8):
        for Y in range(8):
            screen.pixel(X,Y,2)

B = 3

pressing = False
while True:

    keys= pew.keys()
    if not pressing:
        if keys&pew.K_X:
            break
        if keys&pew.K_UP:
            B = min(B+1,3)
        if keys&pew.K_DOWN:
            B = max(B-1,0)
        if keys:
            pressing = True
    else:
        if not keys:
            pressing = False

screen.pixel(6,6,B)

pew.show(screen)

pew.tick(1/6)

'''# initialize circuit
qc = QuantumCircuit(1,1)

# set a random seed, composed of four numbers
seed = [(2*(random()<0.5)-1)*(1+random())/2 for _ in range(4)]

# coordinate of the current screen
X,Y = 0,0
    
# loop to allow player to move half a screen
while True:
    
    # arrow keys move to neighbouring screens
    keys = pew.keys()
    if keys!=0:
        if keys&pew.K_UP:
            Y -= 4
        if keys&pew.K_DOWN:
            Y += 4
        if keys&pew.K_LEFT:
            X -= 4
        if keys&pew.K_RIGHT:
            X += 4
    
    # loop over all points on the screen, and display the brightness
    for x in range(8):
        for y in range(8):
            B = get_brightness(x+X,y+Y) # coordinate of the player is accounted for also
            screen.pixel(x,y,B)
    pew.show(screen)

    pew.tick(1/6)'''