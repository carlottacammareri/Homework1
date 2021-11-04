# SETS
homework 1 pcs2021

1.INTRODUCTION TO SETS

def average(array):
    # your code goes here
    sum_array = sum(set(array))
    len_array = len(set(array))
    output = sum_array/len_array
    return output
    
2.SYMMETRIC DIFFERENCE
 
 M= int(input())
mset = set(map(int,input().split()))
N= int(input())
nset = set(map(int,input().split()))

mdef= mset.difference(nset)
ndef= nset.difference(mset)

output = mdef.union(ndef)
for i in sorted(list(output)):
    print(i)
    

3.SET.ADD()

N= int(input())
countries = set()
for i in range(N):
    countries.add(input())
print(len(countries))


4.CHECK SUBSET

T= int(input())
for _ in range(T):
    a= input()
    A= set(input().split())
    b= int(input())
    B= set(input().split())
    print(A.issubset(B))
    
