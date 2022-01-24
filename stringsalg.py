#HOMEWORK1 CARLOTTA CAMMARERI
#STRINGSALG

#CAMEL CASE

def camelcase(s):
    res = 1
    for let in s:
        if let.isupper():
            res += 1
    if not s:
        res = 0
    return res

#CAESAR CIPHER

def caesarCipher(s, k):
    e = []
    for char in s:
        e.append(ord(char))
    for i in range(n):
        if 65<= e[i] <= 90:
            e[i] = (65 + (e[i]-65+k)%26)
        elif 97 <= e[i] <= 122:
            e[i] = (97 + (e[i]-97+k)%26)
    return "".join(map(chr,e))

#PANGRAMS

def pangrams(s):
    tem = set(s.lower())-set(' ')
    if len(tem) == 26:
        return "pangram"
    else: 
        return "not pangram"

#GAME OF THRONES 1

def gameOfThrones(s):
    
    s = Counter(s)
    tot = 0
    for key, value in s.items():
        tot += value % 2
    if tot > 1:
        return "NO"
    else: 
        return "YES"

#TWO STRINGS

def twoStrings(s1, s2):
    
       m1 = set(s1)
       m2 = set(s2)
       if set.intersection(m1,m2):
           return "YES"
       return "NO"
