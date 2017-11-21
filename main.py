from Crypto.Util import number

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
        t = ExtendedEuclideanAlgorithm(p,q)
        a = t[1]
        b = t[2]
    else:
        t = ExtendedEuclideanAlgorithm(q,p)
        a = t[2]
        b = t[1]

    print("#1")
    r = c**(int((p+1)/4)) % p
    print("#1")
    s = c**(int((q+1)/4)) % q 
    print("#1")
    x = (a*p*s + b*q*r) % n
    x = (a*p*s - b*q*r) % n
    
    return (x, -x % n,y,-y % n)

def ExtendedEuclideanAlgorithm(a,b):
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


print(ExtendedEuclideanAlgorithm(4864,3458))

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



