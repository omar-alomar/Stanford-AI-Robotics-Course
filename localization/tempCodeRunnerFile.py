

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2


def sense(p, Z):
    psum = 0 
    pdf = [0] * 5

    nsum = 0
    for el in p:
       nsum += el

    for j in range(len(p)):
        if world[j] == Z:
          pdf[j] = (p[j] * pHit) / nsum
        else:
          pdf[j] = (p[j] * pMiss) / nsum
        psum += j
    return pdf

print (sense(p,Z))
