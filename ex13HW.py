# Exercise 13.1. Write a program that reads a file, breaks each line into words,
# strips whitespace and punctuation from the words, and converts them to 
# lowercase.
import string
def clean_and_return(a):
    a=string.strip(a)
    a=string.lower(a)
    for x in string.whitespace[:-1]:
        a=a.replace(x,'')
    for x in string.punctuation[:-1]:
        a=a.replace(x,'')
    for x in a:
        if x>'z':
            a=a.replace(x,'')
    for x in string.digits:
        a=a.replace(x,'')
    b=a.split()
    return b

# Exercise 13.2. Go to Project Gutenberg (gutenberg. org ) and download your 
# favorite out-of-copyright book in plain text format.
# Modify your program from the previous exercise to read the book you downloaded
# skip over the header information at the beginning of the file, and process the 
# rest of the words as before. 
# Then modify the program to count the total number of words in the book, and 
# the number of times each word is used.
# Print the number of different words used in the book. 
# Compare different books by different authors, written in different eras. 
# Which author uses the most extensive vocabulary?

def analyzefile(a):
    f=open('./'+a,'r')
    d=dict()
    a='word'
### just to get passed the header
    for i in range (572):   
        f.readline()
######
    while a != '':
        a=f.readline()
        b=clean_and_return(a)
        for x in b:
            d[x]=d.get(x,0)+1
    f.close()
    return d 

        
def find_biggest(d):
    biggest=''
    n=0
    for x in d:
        if d.get(x)>n:
            biggest=x
            n=d.get(x)
    print biggest, n
    return biggest
    
# Exercise 13.3. Modify the program from the previous exercise to print the 20 
# most frequently-used words in the book

def top20(a):
    b=''
    d=dict(a.items()+{'madebykonrad':0}.items())
    for i in range(20):
        b=find_biggest(d)
        d[b]=1
        
# Exercise 13.4. Modify the previous program to read a word list  and then 
# print all the words in the book that are not in the word list. How many of 
# them are typos? How many of them are common words that should be in the word 
# list, and how many of them are really obscure?

def not_english(bookdic,englishdic):
    import time
    b=bookdic.keys()
    for x in b:
        if x not in englishdic:
            print x
            time.sleep(1)

# Exercise 13.5. Write a function named choose_from_hist that takes a histogram 
# and returns a random value from the histogram, chosen with probability in 
# proportion to frequency. 

#this assumes you have a dict of the histogram of 't' other wise it's simply 
# random.choice(t)
def choose_from_hist(d):
    import random
    word=''
    for x in d.keys():
        word+=x*d.get(x)
    return random.choice(word)

# Exercise 13.7. This algorithm works, but it is not very efficient; each time 
# you choose a random word, it rebuilds the list, which is as big as the original
# book. An obvious improvement is to build the list once and then make multiple 
# selections, but the list is still big.
# Write a program that uses this algorithm to choose a random word from the book.

def random_word(d):
    if type(d)==list:
        dic=dict()
        for x in d:
            dic[x]=dic.get(x,1)+1
    d=dic
    import random 
    b=sum(d.values())
    a=random.randint(1,b)
    word=''
    for x in d:
        a=a-d[x]
        word=x
        if a<=0:
            return x
            
# Exercise 13.8. Markov analysis:
# 1. Write a program to read a text from a file and perform Markov analysis
def markov(a):
    f=open('./'+a,'r')
    d=dict()
    a='word'
    b=''
    while a != '':
        a=f.readline()
        b+=a
    a=clean_and_return(b)
    for i in range(len(a)-3):
        if d.get((a[i],a[i+1]),[])==[]:
            d[(a[i],a[i+1])]=[]
        d[(a[i],a[i+1])].append([a[i+2],a[i+3]])
    f.close()
    return d

#2. Add a function to the previous program to generate random text based on 
# the Markov analysis.

def write(tup,d):
    import random
    import time
    rand=random.randint(0,len(d.get(tup))-1)
    tup= d.get(tup)[rand]
    print tup
    time.sleep(1)
    tup=tuple(tup)
    write(tup,d)
    
