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
    
# Exercise 13.9. 
# The 'rank' of a word is its position in a list of words sorted by frequency: the most common word has rank 1, the second most common has rank 2, etc.
# Zipf's law describes a relationship between the ranks and frequencies of words in natural languages
# (http: // en. wikipedia. org/ wiki/ Zipf's_ law ). 
# Specifically, it predicts that the frequency, f , of the word with rank r is:

#                             f = cr -s

# where s and c are parameters that depend on the language and the text. 
# If you take the logarithm of both sides of this equation, you get:

# log f = log c - s log r

# So if you plot log f versus log r, you should get a straight line with slope -s and intercept log c.
# Write a program that reads a text from a file, counts word frequencies, and prints one line for each
# word, in descending order of frequency, with log f and log r. Use the graphing program of your
# choice to plot the results and check whether they form a straight line. Can you estimate the value of
# s?
    
def sortdic(d):
    import math
    ls=d.items()
    logf=[]
    logr=[]
    ls.sort(key=lambda x:x[1],reverse=True)
    for i in range(len(ls)-1):
        logf.append( math.log(ls[i][1]))
        logr.append( math.log(i+1))
    return (logr,logf)



    #     if i%2==0:
    #         logf+=math.log(ls[i][1])
    #         logr-=math.log(i+1)
    #     else: 
    #         logf-=math.log(ls[i][1])
    #         logr+=math.log(i+1)
    # return (logf,logr) #given this s=0.8071824484324789

def findk(d):
    import math
    ls=d.items()
    s=0.8071824484324789
    k=0
    ls.sort(key=lambda x:x[1],reverse=True)
    for i in range(len(ls)-1):
        k+=math.log(ls[i][1])+s*math.log(i+1)
    return k/(len(ls)-1) #k=7.268894074998243

#equation = log f = 7.268894074998243 -0.8071824484324789(log r)
    
    
