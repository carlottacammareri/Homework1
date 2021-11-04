# STRINGS-ALGORITHMS
homework 1 pcs2021


1.CAMEL CASE

       res = 1
       for let in s:
           if let.isupper():
               res += 1
       if not s:
           res = 0
       return res
       
2.CAESAR CIPHER


       e = []
       for char in s:
           e.append(ord(char))
       for i in range(n):
           if 65<= e[i] <= 90:
               e[i] = (65 + (e[i]-65+k)%26)
           elif 97 <= e[i] <= 122:
               e[i] = (97 + (e[i]-97+k)%26)
       return "".join(map(chr,e))
       
 
 3.PANGRAMS
 
 
 
       temp = set(s.lower())-set(' ')
       if len(temp) == 26:
           return "pangram"
       else: 
           return "not pangram"
           
4. GAME OF THRONES 1


             from collections import Counter
                 s = Counter(s)
                 total = 0
                 for key, value in s.items():
                     total += value % 2
                 if total > 1:
                     return "NO"
                 else: 
                     return "YES"
               
5.TWO STRINGS

       m1 = set(s1)
       m2 = set(s2)
       if set.intersection(m1,m2):
           return "YES"
       return "NO"
   
