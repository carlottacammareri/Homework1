#HOMEWORK1 CARLOTTA CAMMARERI
#SETS


#INTRODUCTION TO SETS

def average(array):
    
    size_array = sum(set(array))
    len_array = len(set(array))
    output = size_array/len_array
    return output

#SYMMETRIC DIFFERENCE

M= int(input())
M_set = set(map(int,input().split()))
N= int(input())
N_set = set(map(int,input().split()))

M_def= M_set.difference(N_set)
N_def= N_set.difference(M_set)

out = M_def.union(N_def)
for i in sorted(list(out)):
    print(i)

#SET.ADD()

N= int(input())
country_name = set()
for i in range(N):
    country_name.add(input())
print(len(country_name))

#CHECK SUBSET

T= int(input())
for _ in range(T):
    a= input()
    A= set(input().split())
    b= int(input())
    B= set(input().split())
    print(A.issubset(B))