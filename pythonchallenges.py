
def translate(a):
    a2n=dict()
    n2a=dict()
    alphabet='abcdefghijklmnopqrstuvwxyz'
    for i in range (len(alphabet)):
        a2n[alphabet[i]]=i
    for i in range (len(alphabet)):
        n2a[i]=alphabet[i]
    b=''
    for x in a:
        if x in alphabet:
            var= a2n[x]+2
            if var > 25:
                var=var-26
            b += n2a[var]
        else: b+= x
    return b
        

def find(a):
    b=''
    test=''
    for i in range (len(a)-8):
        if a[i]>'Z' and a[i+1]<'a' and a[i+2]<'a' and a[i+3]<'a'and a[i+4]>'Z' and a[i+5]<'a' and a[i+6]<'a' and a[i+7]<'a'and a[i+8]>'Z':
           test=a[i]+a[i+1]+a[i+2]+a[i+3]+a[i+4]+a[i+5]+a[i+6]+a[i+7]+a[i+8]
           if '\n' not in test:
               b+=a[i+4]
               
    return b

def runprog(x):
    import urllib
    import time
    a=''
    link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + x
    f=urllib.urlopen(link)
    for i in range (10):
        a+=f.readline()
    print a

    if len(a)>35:
        print ''
        print ''
        print a
        time.sleep(10)
    n=''
    for x in a:
        if x > '/'and x<'<':
            n+=x
    f.close()
    print 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    print n
    runprog(n)
    
        
def formnextline(x,a):
     string=''
     for i in range (len(a[x])):
         string+=a[x][i][0]*a[x][i][1]
     return string
