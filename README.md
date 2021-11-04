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
