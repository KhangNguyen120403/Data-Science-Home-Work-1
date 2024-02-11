import numpy as np
#a
#print(np.random.random())

#b
def Flip(p):
    if (p > 1 or p <= 0):
        raise ValueError
    random = np.random.random()
    print (random)
    if (random <= p):
        return True
    #if True is return, it means the result is Head
    else:
        return False
    #if False is return, it means the result is Tail
i = 0
for i in range (5):
    {
        print(Flip(0.21))
    }
#I would expect 1 head out of 5 flips.