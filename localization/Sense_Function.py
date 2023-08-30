#Modify the code below so that the function sense, which 
#takes p and Z as inputs, will output the NON-normalized 
#probability distribution, q, after multiplying the entries 
#in p by pHit or pMiss according to the color in the 
#corresponding cell in world.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2


def sense(p, Z):
    psum = 0 
    for j in p:
        if j == Z:
          j *= pHit
        else:
          j *= pMiss
        psum += j
    return psum

print sense(p,Z)
