from Crypto.Util import number

def getGoodPrime():

    while True:
        p = number.getStrongPrime(1024)
    
        if p % 4 == 3:
            return p

def encrypt(messge,n):
    return m**2 % n

def decryption(p,q,c):

    return 1

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


p = getGoodPrime()

q = getGoodPrime()
n = p*q


m = 19950417



print(p)
print("--")
print(q)
print("--")
print(n)
print("--")
print(encrypt(m,n))

print(ExtendedEuclideanAlgorithm(1434,112))
