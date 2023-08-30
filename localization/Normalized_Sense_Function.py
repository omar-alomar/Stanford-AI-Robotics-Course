#Modify your code so that it normalizes the output for 
#the function sense. This means that the entries in q 
#should sum to one.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
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


print (sense(p,Z))
