# Exercise 12.1. Many of the built-in functions use variable-length argument 
# tuples. Write a function called sum all that takes any number of arguments 
# and returns their sum.

def sum(*x):
    a=0
    for i in x:
        a+=i
    return a


# Exercise 12.2. In this example, ties are broken by comparing words, so words 
# with the same length appear in reverse alphabetical order. For other 
# applications you might want to break ties at random. Modify this example so 
# that words with the same length appear in random order.
def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)
    res = []
    for length, word in t:
        res.append(word)
    return res

def sort_by_just_length(words):
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(key=lambda x:x[0], reverse=True)
    res = []
    for length, word in t:
        res.append(word)
    return res

################
def sort_by_length_rest_random(words):
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)
    t=second_value_random(t)
    res = []
    for length, word in t:
        res.append(word)
    return res

def second_value_random(a):
    import random
    f=[]
    t=a+[(0,0)]
    temp=[]
    for i in range (len(t)-1):
        if t[i][0]==t[i+1][0]:
            temp+=[t[i]]
        else:
            temp+=[t[i]]
            random.shuffle(temp)
            f+=temp
            temp=[]
    return f
            

# Exercise 12.3. Write a function called most_frequent that takes a string and
# prints the letters in decreasing order of frequency. Find text samples from 
# several different languages and see how letter frequency varies between
# languages

def most_frequent(a):
    d=dict()
    for x in a:
        if x == ' ':
            x='space'
        else: x='  '+x+'  '
        if x in d:
            d[x]+=1
        else:
            d[x]=1
    f=d.items()
    f.sort(key=lambda x:x[1],reverse=True)
    for i in range (len(f)):
        print f[i][0],f[i][1]


# Exercise 12.4. More anagrams!
# 1. Write a program that reads a word list from a file (see Section 9.1) and 
# prints all the sets of words that are anagrams.
# Here is an example of what the output might look like:
# ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
# ['retainers', 'ternaries']
# ['generating', 'greatening']
# ['resmelts', 'smelters', 'termless']
# Hint: you might want to build a dictionary that maps from a set of letters to a# list of words that can be spelled with those letters. The question is, how can 
# you represent the set of letters in a way that can be used as a key?
def all_anagrams(wordlist):
    d=dict()
    for word in wordlist:
        a=list(word)
        a.sort()
        a=tuple(a)
        d[a]=d.get(a,[])+[word]
    for x in d:
        if len(d[x])>2:
            print d[x]


# 2. Modify the previous program so that it prints the largest set of anagrams 
# first, followed by the second largest set, and so on.
def anagrams_sorted(wordlist,d):
    '''make a clean d=dict() before running this prog'''
    t=[]
    for word in wordlist:
        a=list(word)
        a.sort()
        a=tuple(a)
        d[a]=d.get(a,[])+[word]
    for x in d:
        c= d.get(x)
        t.append(c)
    t.sort(key=len,reverse=True)
    for i in t:
        if len(i) >3:
            print i


# 3. In Scrabble a 'bingo' is when you play all seven tiles in your rack, along 
# with a letter on the board, to form an eight-letter word. What set of 8 
# letters  forms the most possible bingos?

def bingo(dic):
    ls=[]
    for x in dic:
        if len(x)>7 and len(dic[x])>2:
            ls+=[dic[x]]
    ls.sort(key=len,reverse=True)
    return ls[0]

    
    
# Exercise 12.5. Two words form a 'metathesis pair' if you can transform one into
# the other by swapping two letters; for example, 'converse' and 'conserve.' 
# Write a program that finds all of the metathesis pairs in the dictionary. 
def metathesis(d):
    d2=dict()
    for x in d:
        if len(d[x])>1:
            d2[x]=d[x]
    temp=[]
    for x in d2:
        ls=d2[x]
        for i in range(len(ls)):
            for j in range(i+1,len(ls)):
                if are_meta(ls[i],ls[j]):
                       temp.append((ls[i],ls[j]))
    return temp

def are_meta(a,b):
    n=0
    for i in range(len(a)):
        if  a[i]==b[i]:
            pass
        else:
            n+=1
            if n>2:
                return False
    return True
    
        
# Exercise 12.6. 
# What is the longest English word, that remains a valid English word, as you
# remove its letters one at a time? Now, letters can be removed from either end,
# or the middle, but you cant rearrange any of the letters. Every time you drop 
# a letter, you wind up with another English word.
# Write a program to find all words that can be reduced in this way, and then
# find the longest one.

def two_words(a,ls,c):
    twos=[]
    for x in ls:
        for y in a:
            if y in x and len(x)==c:
                twos.append(x)
    return twos

# temp=[]
# for i in range (2,10):      
#     temp=ex12HW.two_words(temp,a,i)
# longest words: relapsers,scrapings, sheathers

# Eureka! since the longest words built with the method above were 9 letters in 
# order to beat it i just need to test all 10 letter words so just 9,199 words


def check(tenlist,ninelist,a):
    b=[]
    for word in tenlist:
        shorten(word,a,ninelist,b)
    return b
def shorten(word, a,ninelist,b):
    for i in range (0,len(word)-1):
            if word[:i]+word[i+1:] in ninelist:
                a.append(word)
                b.append(word[:i]+word[i+1:])
                return True

# only 816 word! so only 816 9 letter words can be made into ten letter words by
# adding a character, after several runs, it turns out there are no ten words!

# some but possinbly not all 9 letter words are: relapsers,scrapings, sheathers

