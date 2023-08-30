# Modify the empty list, p, so that it becomes a UNIFORM probability
# distribution over five grid cells, as expressed in a list of 
# five probabilities.

p = [0,1,2,3,4]

for i in p:
    p[i] = 1/float(len(p))

print(p)
