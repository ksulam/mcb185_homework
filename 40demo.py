import random
for i in range(50):
    r = random.random()
    if r < 0.7: print(random.choice('AT'), end='')
    else: 
            print(random.choice('CG'), end='')

import sys
print('logging', file=sys.stderr)

