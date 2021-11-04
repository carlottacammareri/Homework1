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


