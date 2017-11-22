from Crypto.Util import number
import math

def getGoodPrime():

    while True:
        p = number.getStrongPrime(1024)
    
        if p % 4 == 3:
            return p

def encrypt(messge,n):
    return m**2 % n

def decrypt(c,p,q):
    
    n = p*q
    a = 0
    b = 0

    if p > q:
        t = extendedEuclideanAlgorithm(p,q)
        a = t[1]
        b = t[2]
    else:
        t = extendedEuclideanAlgorithm(q,p)
        a = t[2]
        b = t[1]

    print("#1")
    r = c**(int((p+1)/4)) % p
    print("#1")
    s = c**(int((q+1)/4)) % q 
    print("#1")
    x = (a*p*s + b*q*r) % n
    y = (a*p*s - b*q*r) % n
    
    return (x, -x % n,y,-y % n)

def extendedEuclideanAlgorithm(a,b):
    
    d = 0
    x = 0
    y = 0

    if a < 0:
        print("A need to be non-negtive")
        return -1 
    if b < 0:
        print("B need to be non-negtive")
        return -1

    if a < b: 
        #TODO fix this, call it with revers parameter
        print("The condition a >= b is not fulfilled")
        return -1

    if b == 0:
        d = a
        x = 1
        y = 0
        return (d,x,y)

    x2 = 1 
    x1 = 0
    y2 = 0
    y1 = 1

    while b > 0:
        q = int(a/b)
        r = a-q*b
        x = x2 - q*x1
        y = y2 - q*y1

        a = b
        b = r
        x2 = x1 
        x1 = x
        y2 = y1
        y1 = y
    d = a
    x = x2
    y = y2

    return (d,x,y)

def powerMod(base,exponent,modulo):
    if 0 > exponent:
        print("Exponent need to be non-negative.")
        # TODO Better error (the funciton can return -1)
        return -1
    if exponent >= modulo:
        print("The condition exponent < modulo is not fulfilled.")
        # TODO Better error (the funciton can return -1)
        return -1
    b = 1
    if exponent == 0:
        return b
    length= math.ceil(math.log2(exponent))
    a = base
    if exponent & 1 == 1: 
        b = base
    exponent = exponent >> 1
    for _ in range(1,length): #length if exlusive
        a = a**2 % modulo
        if exponent & 1 == 1:
            b = a*b % modulo
        exponent = exponent >> 1
    return b
    



def gcd(a,b):
    if b == 0:
        return (a,1,0) #(D,X,Y) a = a * 1 - 0*0
    t = gcd(b,a%b)
    

    return t

def gcd1(a,b):
    while b > 0:
        q = int(a/b)
        r = a-q*b
        a = b
        b = r
    d = a
    return d

print(powerMod(2,-10000,34))    #=-1 Error
print(powerMod(2,-1,34))        #=-1 Error
print(powerMod(7,45,5))         #=-1 Error 
print(powerMod(3,67,80))        #=27
print(powerMod(7,195,12454))    #=6973
print(powerMod(3,255,321))      #=57
print(powerMod(3,0,321))        #=1
print(powerMod(3,320,321))      #=9
print(powerMod(5,596,1234))     #=1013
print(powerMod(47874897438974839,859043859042385098494890584209839058243905432534,859043859042385098494890584209839058243905432534859043859042385098494890584209839058243905432534)) #=741409898527092967581108125001817633038884962666623420677168281613882656173807423395032534913531




print(gcd(12,5)) #=1
print(gcd(45,2)) #=1
print(gcd(12,5)) #=1
print(gcd(30,7)) #=1
print(gcd(31,8)) #=1
print(gcd(20,6)) #=2
print(gcd(28,20))#=4
print(gcd(20,8)) #=4
print(gcd(8,4))  #=4
print("---")
print(gcd1(12,5)) #=1
print(gcd1(45,2)) #=1
print(gcd1(12,5)) #=1
print(gcd1(30,7)) #=1
print(gcd1(31,8)) #=1
print(gcd1(20,6)) #=2
print(gcd1(28,20))#=4
print(gcd1(20,8)) #=4
print(gcd1(8,4))  #=4


print(extendedEuclideanAlgorithm(4864,3458))

"""Crypto"""


p = getGoodPrime()
# TODO Can't be the same fix it later
q = getGoodPrime()
n = p*q


m = 19950417


print(p)
print("--")
print(q)
print("--")
print(n)
print("--")

c = encrypt(m,n)
print(c)
print("---")
print(decrypt(c,p,q))



