# ITERTOOLS
homework 1 pcs2021


1.ITERTOOLS.PRODUCT()

from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*product(a,b))


2.ITERTOOLS.PERMUTATIONS()

from itertools import permutations
s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')


3.ITERABLES AND ITERATORS

from itertools import combinations
N= int(input())
char = input().split()
K = int(input())
count = 0;
total = 0;
for i in combinations(char,K):
    count += 'a' in i
    total += 1
print(count/total)

4.MAXIMIZE IT!


from itertools import *

K,M = map(int,input().split())
N = (list(map(int,input().split()))[1:]for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print (max(results))
