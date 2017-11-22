from Crypto.Util import number
import sys

def getGoodPrime():

    while True:
        p = number.getStrongPrime(1024)
    
        if p % 4 == 3:
            return p

# TODO Need to be in the group so it need to fit
# TODO Add some randomes salt, read in the book
def encrypt(message,publicKey):
    
    postfix = message & 0xFFFFFFFFFFFFFFFF #Get the 64 first bits
    message = (message << 64) | postfix
     
    return message**2 % publicKey

def decrypt(cryptogram,p,q):
    
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


    assert a*p+b*q == 1, "extendedEuclideanAlgorithm don't work" 
    assert p % 4 == 3 , "p mod 4 != 3"
    assert q % 4 == 3 , "1 mod 4 != 3"

    r = powerMod(cryptogram,(p+1)//4,p)

    s = powerMod(cryptogram,(q+1)//4,q)
    
    x = (a*p*s + b*q*r) % n
    y = (a*p*s - b*q*r) % n
    
    for message in (x, -x % n,y,-y % n):
        postfix = message & 0xFFFFFFFFFFFFFFFF #Get the postfix 
        message = message >> 64 # Remove postfix
        if ((postfix ^ message) & 0xFFFFFFFFFFFFFFFF) == 0:
            return message
    
    print("No postfix matched the expected postfix")
    return -1
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
    length = exponent.bit_length()
    a = base
    if exponent & 1 == 1: 
        b = base
    exponent = exponent >> 1

    for x in range(1,length): #length if exlusive
        
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
print(powerMod(69,2,77)) #=64
print(powerMod(69,4,77)) #=15
print(powerMod(47874897438974839,859043859042385098494890584209839058243905432534,859043859042385098494890584209839058243905432534859043859042385098494890584209839058243905432534)) #=741409898527092967581108125001817633038884962666623420677168281613882656173807423395032534913531
print(powerMod(69,2,77)) #=64
print(powerMod(69,4,77)) #=15


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
n= p*q
m = 19950417
m = 123456789987654321123456789
c = encrypt(m,n)

print("p=",p,"OK? =3?",p % 4)
print("q=",q,"OK? =3?",p % 4)
print("n=",n)
print("m=",m)
print("c=",c)
mm  = decrypt(c,p,q)
print("m'=", mm)
print(mm == m)




p = 7
q = 11

n = p*q


print(p)
print("--")
print(q)
print("--")
print(n)
print("--")


for m in range(1000887647363000000000,1000887647363000000100):
    p = getGoodPrime()
    q = getGoodPrime()
    n= p*q
    c = encrypt(m,n)
    mm  = decrypt(c,p,q)
    print(mm,"\n")
    print(m,"\n")
    assert mm == m, "Not equal"
