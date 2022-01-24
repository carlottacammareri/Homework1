#HOMEWORK 1 CARLOTTA CAMMARERI 
#COLLECTIONS

#COLLECTIONS.COUNTER()

from collections import Counter

shoes_num = int(input())
shoe_sizes = Counter(map(int, input().split()))
customer_num = int(input())

cost = 0
for _ in range(customer_num):
    size, price = map(int, input().split())
    if shoe_sizes[size]:
        cost += price
        shoe_sizes[size] -= 1
print(cost)

#COLLECTIONS.ORDEREDDICT()

from collections import OrderedDict
s = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    s[item] = s.get(item, 0) + int(quantity)
for item, quantity in s.items():
    print(item, quantity)

#COMPANY LOGO

import math
import os
import random
import re
import sys
import collections


if __name__ == '__main__':
    S = sorted(input().strip())
    S_counter = collections.Counter(S).most_common()
    S_counter = sorted(S_counter, key = lambda x: (x[1] *-1, x[0]))
    for i in range(0,3):
        print(S_counter[i][0], S_counter[i][1])


#PILLING UP!

from collections import deque
T= int(input())
for _ in range(T):
    out = True
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
                out = False
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
                out = False
                break
    if out:
        print("Yes")
    else:
        print("No")
            
                