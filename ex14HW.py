# Exercise 14.1. The os module provides a function called walk that is similar
# to this one but more versatile. Read the documentation and use it to print
# the names of the files in a given directory and its subdirectories

def run():
    import os
    import time
    directory=raw_input('name of dir ')
    flist=[]
    for x,y,z in os.walk(directory):
        if len(z)>0:
            flist.extend(z)
    print directory
    for x in flist:
        print x
        time.sleep(1)
    
        

# Exercise 14.2. Write a function called sed that takes as arguments a pattern 
# string, a replacement string, and two filenames; it should read the first 
# file and write the contents into the second file (creating it if necessary). 
# If the pattern string appears anywhere in the file, it should be replaced
# with the replacement string. If an error occurs while opening, reading, 
# writing or closing files, your program should catch the exception, 
# print an error message, and exit.

def sed(pattern,replacement,readfile,writefile):
    try:
        r=open(readfile)
        w=open(writefile,'w')
        a='a'
        text=''
        while a != '':
            a=r.readline()
            text+=a
        while pattern in text:
            p=text.find(pattern)
            text=text[:p]+replacement+text[p+len(pattern):]
        w.write(text)
        r.close()
        w.close()
    except:
        return 'does not fempute'


# Exercise 14.3.  Write a module that 
# imports anagram_sets and provides two new functions: store_anagrams should 
# store the anagram dictionary in a 'shelf' read_anagrams should look up a 
# word and return a list of its anagrams.
def all_anagrams(wordlist):
    d=dict()
    for word in wordlist:
        a=list(word)
        a.sort()
        a=tuple(a)
        d[a]=d.get(a,[])+[word]
    return d

def stored_anagrams(d):
    a=raw_input('read or write? ')
    import pickle
    if a == 'write':
        f=open('anagram.db','w')
        f.write(pickle.dumps(d))
    elif a=='read':
        f=open('anagram.db')
        s=''.join(f.readlines())
        s=pickle.loads(s)
        for x in s:
            d[x]=s[x]
    f.close()


def read_anagrams(word,d='a'):
    import pickle
    if type(word)!=str:
        return 'only strings please'
    if d=='a':
        f=open('anagram.db')
        s=''.join(f.readlines())
        d=pickle.loads(s)
    letters=list(word)
    letters.sort()
    try:
        anagrams=d[tuple(letters)][:]
        anagrams.remove(word)
    except:
        return "sorry %s not a word" % word
    return anagrams


# Exercise 14.4. In a large collection of MP3 files, there may be more than 
# one copy of the same song, stored in different directories or with different 
# file names. The goal of this exercise is to search for duplicates.

# 1. Write a program that searches a directory and all of its subdirectories, 
# recursively, and returns a list of complete paths for all files with a given 
# suffix (like .mp3). Hint: os.path provides several useful functions for 
# manipulating file and path names.

def allfiles(dirf):
    import os 
    masterlist=[]
    for x,y,z in os.walk(dirf):
        if len(z)>0:
            for i in z:
                if i[-1]=='3':
                    masterlist.append(x+'/'+i)
    return masterlist

# 2. To recognize duplicates, you can use md5sum to compute a 'checksum' for 
# each files. If two files have the same checksum, they probably have the 
# same contents.
def find_dups(masterlist):
    import os
    d=dict()
    for x in masterlist:
        import string
        x=x.replace(' ','\ ')
        for i in "(){}[]&,';":
            x=x.replace(i,"\\"+i)
        f=os.popen('md5sum '+x)
        hashed=f.read()
        d[hashed[:32]]=d.get(hashed[:32],[])+[x]
        f.close()
        print x
    return d

# 3. To double-check, you can use the Unix command diff.
# nah.



# Programs that will be imported as modules often use the following idiom:
# if __name__ == '__main__':
#     print linecount('wc.py')
# __name__ is a built-in variable that is set when the program starts. 
# If the program is running as a script, __name__ has the value __main__; in 
# that case, the test code is executed. Otherwise, if the module is being 
# imported, the test code is skipped.
# Exercise 14.5. Type this example into a file named wc.py and run it as a 
# script. Then run the Python interpreter and import wc. What is the value 
# of __name__ when the module is being imported? 

# 'wc', The name of the module




# Exercise 14.6. The urllib module provides methods for manipulating URLs 
# and downloading information from the web. The following example downloads 
# and prints a secret message from thinkpython.com:

# import urllib
# conn = urllib.urlopen('http://thinkpython.com/secret.html')
# for line in conn:
# print line.strip()
# Run this code and follow the instructions you see there.


# Write a program that prompts the user for a zip code and prints the
# name and population of the corresponding town.

def townandpop():
    a= raw_input('zip code please.. ')
    import urllib
    import string
    f= urllib.urlopen('http://www.uszip.com/zip/'+a)
    a=f.read()
    f.close()
    townchar=a.find('<title>')+7
    popchar=a.find('Total population')
    population=''
    for x in a[popchar:popchar+40]:
        if x in string.digits+',':
            population+=x
    end=a[townchar:].find(',')+4
    town=a[townchar:townchar+end]
    print town,population
    
#doesnt work for zipcodes that are assigned to just states such a 04970
                   

