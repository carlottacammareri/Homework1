# COLLECTIONS
homework 1 pcs2021

1.COLLECTIONS.COUNTER()

from collections import Counter

num_shoes = int(input())
shoe_sizes = Counter(map(int, input().split()))
num_customers = int(input())

cost = 0
for _ in range(num_customers):
    size, price = map(int, input().split())
    if shoe_sizes[size]:
        cost += price
        shoe_sizes[size] -= 1
print(cost)


2.COLLECTIONS.ORDEREDDICT()


from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)
    
3.COMPANY LOGO

import math
import os
import random
import re
import sys
import collections


if __name__ == '__main__':
    s = sorted(input().strip())
    s_counter = collections.Counter(s).most_common()
    s_counter = sorted(s_counter, key = lambda x: (x[1] *-1, x[0]))
    for i in range(0,3):
        print(s_counter[i][0], s_counter[i][1])


4.PILLING UP!

from collections import deque
N= int(input())
for _ in range(N):
    flag = True
    input()
    d= deque(map(int, input().strip().split()))
    if(d[0] >= d[-1]):
        max = d.popleft()
    else:
        max = d.pop()
    while d:
        if(len(d)==1):
            if(d[0] <= max):
                break
            else:
                flag = False
                break
        else:
            if(d[0] <= max and d[-1]<=max):
                if(d[0]>= d[-1]):
                    max = d.popleft()
                else:
                    max = d.pop()
            elif(d[0]<= max):
                    max = d.popleft()
            elif(d[-1]<= max):
                max = d.pop()
            else:
                flag = False
                break
    if flag:
        print("Yes")
    else:
        print("No")
            
                


