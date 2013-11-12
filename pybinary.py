from math import *
#################################################
"""
COMMANDS IN THIS FILE TO MANIPULATE BINARIES:

makebinary(n)

makenumber(n)

add(a,b)

multiply(a,b)

"""
#############################################
"""
baller way to do it
def mb(x):
    return [x%2]+2*mb(x/2)
"""
def add1(l,c=0):
    if l==[] or type(l)!=list:
        return l
    if c+1 > len(l):
        l=l+[0]
    if l[c]==0:
        l[c]=1
        return l
    else: 
        l[c]=0
        c+=1
        return add1(l,c)


def machineadd(a,b):
    if type(a)!=type(b)!=list:
        print "does not fempute"
        return a,b
    a=a+(len(b)+1)*[0]
    b=b+(len(a)-len(b))*[0]
    d={0:{1:1,0:0,2:0},1:{1:0,2:1,0:1}}
    cb=0
    ls=[]
    for x,y in zip(a,b):
        ls.append(d[cb][x+y])
        if cb==0 and x+y == 2:
            cb=1
        elif cb==1 and x+y == 0:
            cb=0
    while ls[-1]==0 and len(ls)>1:
        ls=ls[:-1]
    return ls
    
        
def makebinary(n):
    if n==0:
        return [0]
    elif n==[]:
        return []
    c=[]
    b =int(log(n)/log(2))
    d= divideby2s (n,b,c)
    return d
    
def divideby2s (n,b,c):
    if b == -1:
        return c
    else:
        d = n/2**b
        n = n%2**b
        c= [d] + c
        b = b-1
        return divideby2s(n,b,c)
    
def add(a,b):
    c = []
    if a==[] and b==[]:
        return []
    if len(a)!=len(b):
        k = abs(len(a)-len(b))
        if len(a)> len(b):
            for j in range (k):
                b = b + [0]
        else:
            for j in range (k):
                a = a + [0]
    a+=[0]
    b+=[0]
    for i in range(len(b)):
        if a[i] + b[i]== 0:
            c = c + [0]
        elif a[i] + b[i]== 1:
            c = c + [1]
        elif a[i] + b[i]== 2:
            c = c + [0]
            a[i+1] = a[i+1]+1
        elif a[i] + b[i]== 3:
            c = c + [1]
            a[i+1] = a[i+1]+1
    while c[-1]==0 and len(c)>1:
        c = c[:-1]
    return c
            
def makenumber(n):
    a=0
    for i in range(len(n)):
            a= a + n[i]*(2**i)
    return a
            

def multiply(a,b):
    csum=[] 
    for i in range(len(b)):
       csum= add(csum,([0]*i)+(a*b[i]))
    return csum

