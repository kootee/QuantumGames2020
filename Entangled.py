import pew # setting up tools for the pewpew
import random
from microqiskit import QuantumCircuit, simulate # setting up tools for quantum

pew.init() # initialize the game engine...
screen = pew.Pix() # ...and the screen

qc = QuantumCircuit(2,2) # create an empty circuit with two qubits and two output bits
qc.h(0)
qc.cx(0,1)

# create circuits with the required measurements, so we can add them in easily
meas = QuantumCircuit(2,2)
meas.measure(0,0)
meas.measure(1,1)
    
    


# loop over the squares centered on (1,2), (6,2) (1,4) and (6,4) and make all dim
for (X,Y) in [(1,4),(6,4)]:
    for dX in [+1,0,-1]:
        for dY in [+1,0,-1]:
            screen.pixel(X+dX,Y+dY,2)
pew.show(screen)
        
for (X,Y) in [(1,4),(6,4)]:
    screen.pixel(X,Y,0) # turn off the center pixels of the squares  

old_keys = 0
while True: # loop which checks for user input and responds

    # look for and act upon key presses
    keys = pew.keys() # get current key presses
    if keys!=0 and keys!=old_keys:
        if keys&pew.K_O:
            qc.cx(1,0)
            
        
    old_keys = keys 
    
    # execute the circuit and get a single sample of memory for the given measurement bases
    m = simulate(qc+meas,shots=1,get='memory')
    
    # turn the pixels (1,2) and (1,4) (depending on basis[1]) on or off (depending on m[0][0])
    if m[0][0]=='1':
        
            screen.pixel(6,4,3)
        
    else:
        
            screen.pixel(6,4,0)
       
    # do the same for pixels (6,2) and (6,4)
    if m[0][1]=='1':
        
            screen.pixel(1,4,3)
        
    else:
        
            screen.pixel(1,4,0)
       
    # turn the pixels not used to display m[0] to dim
    
        
    
    
       
    
    pew.show(screen) 
    pew.tick(1/6) # pause for a sixth of a second