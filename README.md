# WARMUP-ALGORITHMS
homework 1 pcs2021


1.SOLVE ME FIRST

        return a+b
    num1 = int(input())
    num2 = int(input())
    res = solveMeFirst(num1,num2)
    print(res)


2.SIMPLE ARRAY SUM

    x = 0
    for i in range(0,ar_count):
        x = x + ar[i]
    return x
    
    
3.COMPARE THE TRIPLETS


    Alice = 0
    Bob = 0
    for i in range(3):
        if a[i] > b[i]:
            Alice += 1
        elif b[i] > a[i]:
            Bob += 1
    li = (Alice,Bob)
    return li
    
4. A VERY BIG SUM

         sum = 0
         for i in range(ar_count):
             sum = sum + int(ar[i])
         return sum        
    
5.DIAGONAL DIFFERENCE

    d1 = sum([arr[x] [x] for x in range(len(arr))])
    d2 = sum([arr[x] [n-1-x] for x in range(len(arr))])
    return(abs(d1 - d2))
    
    
6. PLUS MINUS
       positiveCounter = 0
       negativeCounter = 0
       zeroCounter = 0
    
       for i in range (len(arr)):
           if arr[i] > 0:
               positiveCounter +=1
           elif arr[i] < 0:
               negativeCounter += 1
           else:
               zeroCounter += 1
       print("%f"%(positiveCounter / len(arr)))
       print("%f"%(negativeCounter / len(arr)))
       print("%f"%(zeroCounter / len(arr)))

7.STAIRCASE

                  for i in range(0,n):
                      for j in range(0,n):
                          if i+j >= n-1:
                              print("#",end='')
                          else:
                              print(" ",end ='')
                      print("\r")
        
8.MINI MAX SUM

    arr.sort()
    s = sum(arr)
    maxResults = s - arr[0]
    minResults = s - arr[len(arr)-1]
    print(minResults, maxResults)
    
9.BIRTHDAY CAKE CANDLES

         candles.sort()
         result = candles.count(candles[len(candles)-1])
         return result

10. TIME CONVERSION

          p = s.split(":")
          p[0] = int(p[0])%12
          if "PM" in p[-1] and [0]:
              p[0]+=12
          p[0] = '%02d'%p[0]
          return ":".join(p)[:-2]
            
