from microqiskit import QuantumCircuit, simulate
import numpy as np

def make_line ( length ):
    # determine the number of bits required for at least `length` bit strings
    n = int(np.ceil(np.log(length)/np.log(2)))
    # start with the basic list of bit values
    line = ['0','1']
    # each application of the following process double the length of the list,
    # and of the bit strings it contains
    for j in range(n-1):
        # this is done in each step by first appending a reverse-ordered version of the current list
        line = line + line[::-1]
        # then adding a '0' onto the end of all bit strings in the first half
        for j in range(int(len(line)/2)):
            line[j] += '0'
        # and a '1' onto the end of all bit strings in the second half
        for j in range(int(len(line)/2),int(len(line))):
            line[j] += '1'
    return line

def height_to_circuit( height ):
    
    line = make_line( len(height) )

    n = int(np.ceil(np.log(len(line))/np.log(2)))

    renorm = np.sqrt(sum(height))

    real_vec = [0]*(2**n)
    for j,h in enumerate(height):
        real_vec[int(line[j],2)] = np.sqrt(h)/renorm

    qc = QuantumCircuit(n)
    qc.initialize( real_vec )

    return qc

def circuit_to_height( qc ):
    
    n = qc._n
    
    line = make_line( 2**n )

    real_vec = simulate(qc,get='statevector')
    
    height = [0]*(2**n)
    for j,amp in enumerate(real_vec):
        string = "{0:b}".format(j)
        string = '0'*(n-len(string)) + string
        k = line.index(string)
        height[k] = amp[0]**2
        
    max_prob = max(height)
    for j,h in enumerate(height):
        height[j] = h/max_prob
  
    return height