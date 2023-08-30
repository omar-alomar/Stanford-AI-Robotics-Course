#Modify the code so that it updates the probability twice
#and gives the posterior distribution after both 
#measurements are incorporated. Make sure that your code 
#allows for any sequence of measurement of any length.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    psum = 0 
    pdf = [0] * 5

    nsum = 0
    for el in pdf:
       nsum += el

    for j in range(len(p)):
        if world[j] == Z:
          pdf[j] = (p[j] * pHit)
        else:
          pdf[j] = (p[j] * pMiss)
        psum += j
    
    nsum = 0
    for el in pdf:
       nsum += el
    for i in range(len(p)):
       pdf[i] /= nsum
    return pdf

for i in range(len(measurements)):
    p = sense(p,measurements[i])
print(p)
