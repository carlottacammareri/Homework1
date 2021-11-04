# Homework1
homework 1 pcs2021


##list comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print ([[a,b,c] for a in range (0, x+1)for b in range (0, y+1)for c in range(0,z+1)if a + b + c != n])
    
##find the runner-up score

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print (sorted(set(arr))[-2])


