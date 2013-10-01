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
    for i in range (572):
        f.readline()
    while a != '':
        a=f.readline()
        b=clean_and_return(a)
        for x in b:
            d[x]=d.get(x,0)+1

    return d 

        
def find_biggest(d):
    biggest=''
    n=0
    for x in d:
        if d.get(x)>n:
            print biggest, n
            biggest=x
            n=d.get(x)
    print biggest, n
    
