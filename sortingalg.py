#HOMEWORK 1 CARLOTTA CAMMARERI
#SORTING ALGORITHMS

#BIGSORTING

def bigSorting(unsorted):
  
    unsorted.sort(key = lambda x: (len(x), x))
  
    return unsorted

#INTRO TO TUTORIAL

def introTutorial(V, arr):
     return arr.index(V)
    
#INSERTION SORT 1

def insertionSort1(n, arr):
   
    pr = arr[-1]
    for ind in range(len(arr)-2, -1, -1):
        if arr[ind] > pr:
            arr[ind + 1 ] = arr[ind]
            print(" ".join(map(str, arr)))
        else:
            arr[ind + 1] = pr
            print(" ".join(map(str, arr)))
            break
    if arr[0] > pr:
        arr[0] = pr
        print(" ".join(map(str, arr)))

#INSERTION SORT 2

def insertionSort1(n, arr):
    # Write your code here
    pr = arr[n]
    for ind in range(n-1, -1, -1):
        if arr[ind] > pr:
            arr[ind + 1 ] = arr[ind]
        else:
            arr[ind + 1] = pr
            break
    if arr[0] > pr:
        arr[0] = pr
    

def insertionSort2(n, arr):
    # Write your code here
    for ind in range(1, len(arr)):
        insertionSort1(ind, arr)
        print(" ".join(map(str, arr)))

#CORRECTNESS AND THE LOOP INVARIANT

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

M = int(input().strip())
arr = [int(i) for i in input().strip().split()]
insertion_sort(arr)
print(" ".join(map(str,arr)))

#RUNNING TIME

def runningTime(arr):
    # Write your code here
    shifts = 0
    for j in range(1, len(arr)):
        key = arr[j]
        i = j 
        while i > 0 and arr[i-1]>key:
            arr[i] = arr[i-1]
            shifts += 1
            i -= 1
        arr[i] = key
    return shifts

#QUICKSORT 1

def quickSort(arr):
    
    left = []
    right = []
    pivot = arr[0]
    i = 0 
    j = len(arr) -1
    while i < j:
        while i < j and arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    arr[0], arr[j] = arr[j], arr[0]
    
    return arr 

#THE FULL COUNTING SORT

def countSort(arr):
    # Write your code here
    res= [[] for i in range(100)]
    for i in range(n//2):
        res[int(arr[i][0])].append('-')
    for i in range(n//2, n):
        res[int(arr[i][0])].append(arr[i][1])
    for string in res:
        if string:
            print(*string, end=' ')

#CLOSEST NUMBERS

def closestNumbers(arr):
    
    pairs = []
    mindiff = 999999999999
    arr.sort()
    for i in range(1, len(arr)):
        d = abs(arr[i-1] - arr[i])
        if d < mindiff:
            mindiff = d 
            pairs = [arr[i-1], arr[i]]
        elif d == mindiff:
            pairs.extend([arr[i-1], arr[i]])
            
    return pairs

#FIND THE MEDIAN

def findMedian(arr):

    arr = sorted(arr)
    return arr[len(arr)//2]
    