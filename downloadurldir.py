import urllib
import os

def pullallhref(a):
    ls=[]
    while 'href=' in a:
        n=a.find('href')+6
        end=a.find("\"",n)
        if len(a[n:end])>1 and a[n:end][0] != '?':
            ls.append(a[n:end])
        a=a[end:]
    return ls



def getfiles(suffix):
    os.makedirs('./'+suffix)
    parenturl='http://people.duke.edu/~'+suffix
    f=urllib.urlopen(parenturl)
    a=f.read()
    ls=pullallhref(a)
    for x in ls:
        if x[-3:]=='htm':
            rf=urllib.urlopen(parenturl+'/'+x)
            wf=open('./'+suffix+'/'+x,'w')
            wf.write(rf.read())
            rf.close()
            wf.close()
        if x[-1]=='/':
            getfiles(suffix+'/'+x)

# afterward you need to run " find ./ -type d -name ~kd32 -exec rm -rf {} \; " to remove all ~kd32 directories
        
        
