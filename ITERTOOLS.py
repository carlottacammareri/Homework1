#HOMEWORK1 CARLOTTA CAMMARERI
#ITERTOOLS

#ITERTOOLS.PRODUCT()

from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*product(A,B))

#ITERTOOLS.PERMUTATIONS()

from itertools import permutations
S,n = input().split()
print(*[''.join(i) for i in permutations(sorted(S),int(n))],sep='\n')

#ITERABLES AND ITERATORS

from itertools import combinations
N= int(input())
let = input().split()
K = int(input())
count = 0;
total = 0;
for i in combinations(let,K):
    count += 'a' in i
    total += 1
print(count/total)

#MAXIMIZE IT!

from itertools import *

K,M = map(int,input().split())
N = (list(map(int,input().split()))[1:]for _ in range(K))
res = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print (max(res))

