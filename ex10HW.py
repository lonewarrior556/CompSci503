###################################################
# # Usefull functions within this file:

# # Cumsum(list)
# # is_sorted(list)
# # anagram(a,b)
# # has_duplicates(list)
# # guess(numberofkids, numberoftrials)birthday problem
# # remove_duplicate(list)
# # methodtest2(list) imports word.txt
# # isinlist(word,list)
# # reverse_pairs(a)

###############################################





def cumsum(a):
    if a==[] or a==[0]:
        return 0
    n=[a[0]]
    for i in range (len(a)-1):
        n=n+[0]
        n[i+1]= a[i+1]+n[i]
    return n

def chop(t):
    del t[0], t[-1]

def middle(t):
    return t[1:-1]

# Exercise 10.6. Write a function called is_sorted that takes a list as a
#  parameter and returns True
# if the list is sorted in ascending order and False otherwise.
def is_sorted(a):
    b=a+[0]
    b.sort()
    b=b[1:]
    if a==b:
        return True

# Exercise 10.7. Two words are anagrams if you can rearrange the letters from
#  one to spell the other.
# Write a function called is_anagram that takes two strings and returns True if
#  they are anagrams.
def anagram(a,b):
    c = list(a)
    d = list(b)
    c.sort()
    d.sort()
    if c == d:
        return True

# Exercise 10.8. The (so-called) Birthday Paradox:
# 1. Write a function called has_duplicates that takes a list and returns True if
#  there is any element that appears more than once. It should not modify the 
#  original list.
def has_duplicates(a):
    t=0
    for x in a:
        for y in a:
            if x == y:
                t = t+1
    if t > len(a):
        return True




# 2. If there are 23 students in your class, what are the chances that two of you
# have the same birthday? You can estimate this probability by generating random
#  samples of 23 birthdays and checking for matches. Hint: you can generate
# random birthdays with the randint function in the random module.
from random import *
def guess(n,t):
    a=[0]*n
    b=0
    for j in range(t):
        for i in range (n):
            a[i] = randint(1,365) 
        if has_duplicates(a):
            b=b+1

    print "out of "+str(t)+" classrooms with "+ str(n)+" kids, "+ str(b)+" had at least 2 kids with the same birthday, or " +str(b/float(t))

# Exercise 10.9. Write a function called remove_duplicates that takes a list and 
# returns a new  list with only the unique elements from the original.



def remove_duplicate(a):
    b=[]
    for i in range(len(a)):
        if a[i] in b:
            True
        else: b.append(a[i])
    return b
    

# Exercise 10.10. Write a function that reads the file words.txt and builds a 
# list with one element per word. Write two versions of this function, one using
#  the append method and the other using the idiom t = t + [x]. Which one takes
#  longer to run? Why? Hint: use the time module to measure elapsed time.
#  Solution: http: // thinkpython. com/ code/ wordlist. py
import time
def methodtest1(listone):
    print "here comes the first run"
    f=open('./words.txt','r')

    a=time.time()
    listone=[]
    for i in range (113809):
        word=f.readline()
        listone=listone+[word]
    b=time.time()
    print b-a
    f.close()
    print "not bad"
    print "\n"
    
def methodtest2(listtwo):
    print "here comes the 2nd run"
    fb=open('./words.txt','r')
    a=time.time()
    for i in range (113809):
        word=fb.readline()
        listtwo.append(word[:-2])
    b=time.time()
    print b-a
    fb.close()
    print "done"


# Exercise 10.11. To check whether a word is in the word list, you could use the 
# in operator, but it would be slow because it searches through the words in 
# order.Because the words are in alphabetical order, we can speed things up with 
# a bisection search (also known as binary search), which is similar to what you 
# do when you look a word up in the dictionary.
# You start in the middle and check to see whether the word you are looking for 
# comes before the word in the middle of the list. If so, then you search the 
# first half of the list the same way. Otherwise you search the second half.
# Either way, you cut the remaining search space in half. If the word list has 
# 113,809 words

def isinlist(a,ls):
    b = ls[len(ls)/2]
    while len(ls)>1:
#        print len(ls)
#        print b
        if a>b:
            ls = ls[(len(ls)/2):]
            b = ls[len(ls)/2]
        elif a<b:
            ls = ls[:(len(ls)/2)]
            b = ls[len(ls)/2]
        elif a==b:
            ls=[a]
    if ls[0] == a:
        return True
    else: 
        return False
                       
     
# Exercise 10.12 Two words are a reverse pair if each is the reverse of
# the other. Write a program that finds all the reverse pairs in the word list. 


def reverse_pairs(a):
    b=[]
    k=a+['konrad']
    for x in a:
        c=''
        for i in range(len(x)):
            c=x[i]+c
        if isinlist(c,k):
            b.append(x)
            k.remove(x)
            print x
        else: k.remove(x)
    return b

