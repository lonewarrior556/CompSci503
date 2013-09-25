######################################################
# # useful functions within this file:

# # list2dic(list,dictionary)
# # histogram(string), 
# # print_hist(dictionary) prints a sorted dictionary
# # reverse_lookup(dictionary,value)
# # invert_dict(dictionary)
# # fibonacci(n) creates a fibonacci dictionary called known, 
# # fib(n) fibonacci number the hard way
# # has_dupli(list)
# # rotated_pairs(string,dictionary) returns all rotated words for string

######################################################################

# Exercise 11.1. Write a function that reads the words in words.txt and stores 
# them as keys in a dictionary.
def list2dic(a,b):
    for x in a:
        b[x]=1
    return b

import time

def test(a,b,n):
    c=time.time()
    for i in range (n):
        'zoo' in a
    d=time.time()
    print "done"
    print (d-c)
    c=time.time()
    for i in range (n):
        'zoo' in b
    d=time.time()
    print "done"
    print (d-c)
        
    
def histogram(s):
    d = dict()
    for c in s:
        d[c]=d.get(c,0)+1
    return d

def print_hist(a):
    c=a.keys()
    c.sort()
    for x in c:
        print x, a[x]



# Exercise 11.4. Modify reverse_lookup so that it builds and returns a list of 
# all keys that map to v, or an empty list if there are none.

def reverse_lookup(d, v):
    ls=[]
    for k in d:
        if d[k] == v:
            ls.append(k)
    return ls

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

known = {0:0, 1:1}
def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else: return fib(n-1)+fib(n-2)

# Exercise 11.9. Use a dictionary to write  a  faster, simpler version of has_duplicates. 
def has_dupli(a):
    b=dict()
    for x in a:
        b[x]=''
    if len(a)==len(b):
        print "no duplicates"
    else: print 'a has duplicates'

# Exercise 11.10. Two words are rotate pairs if you can rotate one of them and 
# get the other (see rotate_word in Exercise 8.12).
# Write a program that reads a wordlist and finds all the rotate pairs. 

def rotated_pairs(a,ls):
    a2n=dict()
    n2a=dict()
    alphabet='abcdefghijklmnopqrstuvwxyz'
    for i in range (len(alphabet)):
        a2n[alphabet[i]]=i
    for i in range (len(alphabet)):
        n2a[i]=alphabet[i]
    rotwords=[]
    for i in range (len(alphabet)-1): 
        rword=''
        for x in a:
           n= a2n[x]+i
           if n>25:
               n=n-25
           rword += n2a[n]
        if rword in ls and i!= 0:
            rotwords.append(rword)
    return rotwords

# Make a wordlist list, and a dictionary with that word list, 
# and and empty lin=dict()
# for x in wordlist:
#     var=ex11HW.rotated_pairs(x,dictionary)
#     if len(var)>0:
#         lib[x]=var
