import numpy as np
import matplotlib.pyplot as plt
from random import randrange

def test(set,iterations=100):
    h = []
    for j in range(iterations):
        temp = []
        for i in range(set):
            new_rand = randrange(set)
            if(new_rand in temp):
                h.append(i)
                break
            else: temp.append(new_rand)
    return h

plist = test(365,100000)
avg = sum(plist) / len(plist)
'''
print('avg: '+ str(avg))
plot of number of iterations of test x number of random samples taken until collision
'''

plt.hist(plist,bins=30)
plt.ylabel('number of iterations')
plt.xlabel('samples until collision');
plt.axvline(sum(plist) / len(plist), color='k', linestyle='dashed', linewidth=1)
min_ylim, max_ylim = plt.ylim()
plt.text(avg*1.1, max_ylim*0.9, 'Mean: {:.2f}'.format(avg))
