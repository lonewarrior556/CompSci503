
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

d={'pi':3.141592,'e':2.7183}
def calc(a):
    global d
    dic =d
    b=[]
    if type(a)!= list and type(a)!= tuple or len(a)<3:
        return a
    for i in range(len(a)):
        if type(a[i]) == tuple or type(a[i]) == list:
            b+=[calc(a[i])]
        else:
            if type(a[i]) != int and not callable(a[i]):
                if a[i] in dic:
                    b+=[d[a[i]]]
                else:
                    return 'variable not defined',a[i]
            else:b+= [a[i]]
        
    return mcalc(b)
           
     
def mcalc(a):
    a= map(a[0],[[a[1],a[2]]])
    return a[0]


