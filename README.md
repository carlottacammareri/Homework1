# SORTING ALGORITHMS
homework 1 pcs2021

1.BIG SORTING

       unsorted.sort(key = lambda x: (len(x), x))
  
       return unsorted
       
 2.INTRO TO TUTORIAL 
 
             return arr.index(V)
             
             
 3.INSERTION SORT 1
             
             probe = arr[-1]
    for ind in range(len(arr)-2, -1, -1):
        if arr[ind] > probe:
            arr[ind + 1 ] = arr[ind]
            print(" ".join(map(str, arr)))
        else:
            arr[ind + 1] = probe
            print(" ".join(map(str, arr)))
            break
    if arr[0] > probe:
        arr[0] = probe
        print(" ".join(map(str, arr)))
        
 4.INSERTION SORT 2
 
       def insertionSort1(n, arr):
    # Write your code here
    probe = arr[n]
    for ind in range(n-1, -1, -1):
        if arr[ind] > probe:
            arr[ind + 1 ] = arr[ind]
        else:
            arr[ind + 1] = probe
            break
    if arr[0] > probe:
        arr[0] = probe
    

      def insertionSort2(n, arr):
          # Write your code here
          for ind in range(1, len(arr)):
              insertionSort1(ind, arr)
              print(" ".join(map(str, arr)))


5.CORRECTNESS AND THE LOOP INVARIANT

           for i in range(1, len(l)):
               j = i-1
               key = l[i]
               while (j >= 0) and (l[j] > key):
                  l[j+1] = l[j]
                  j -= 1
               l[j+1] = key

       m = int(input().strip())
       ar = [int(i) for i in input().strip().split()]
       insertion_sort(ar)
       print(" ".join(map(str,ar)))
       
       
       
6.RUNNING TIME

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
    
    
    
7.QUICKSORT 1


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
    
    
    
    
8.THE FULL COUNTING SORT


        result = [[] for i in range(100)]
    for i in range(n//2):
        result[int(arr[i][0])].append('-')
    for i in range(n//2, n):
        result[int(arr[i][0])].append(arr[i][1])
    for string in result:
        if string:
            print(*string, end=' ')

9.CLOSEST NUMBERS
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
