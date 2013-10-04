
    # calc((plus,1,2))=3
    # calc((times,0,50=0
    # calc((time,(plus,1,2),5))=15
    # calc(5) = 5
    # calc(plus)= plus

def add(a):
    b=0
    for x in a:
        b+=x
    return b
        

def times(a):
    b=1
    for x in a:
        b=b*x
    return b

def divide(a):
    b=0
    for x in a:
        if b==0:
            b=x
        else: b=b/x
    return b
        

def minus(a):
    b=0
    for x in a:
        if b ==0:
            b = x
        else: b= b-x
    return b


def calc(a):
    b=[]
    if type(a)!= list and type(a)!= tuple:
        return a
    for i in range(len(a)):
        if type(a[i]) == tuple or type(a[i]) == list:
            b+=[calc(a[i])]
        else: b+= [a[i]]
        
    return mcalc(b)
           
     
def mcalc(a):
    a= map(a[0],[[a[1],a[2]]])
    return a[0]
    
