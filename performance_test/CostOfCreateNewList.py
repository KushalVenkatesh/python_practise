A = [x for x in range(100000)]
B = [x for x in range(100000)]

import time

def pop1(A):
    for i in xrange(len(A)):
        A.pop()
        i += 1

def pop2(B):
    length= len(B)
    point = length -1
    for i in xrange(length):
        point -= 1
        #this step cost a lot
        if i % 10 == 0:
            B = B[:point]

print("pop1 cost:")
start = time.clock()
pop1(A)
elapsed = (time.clock() - start)
print(elapsed)

print("pop2 cost:")
start = time.clock()
pop2(B)
elapsed = (time.clock() - start)
print(elapsed)

# pop1 cost:
# 0.027287
# pop2 cost:
# 3.46797
