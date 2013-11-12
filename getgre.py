import urllib






def wordsfrompage(webp,d):
    f=urllib.urlopen(webp)
    a=f.read()
    f.close
    b='<tr><th>'
    c='</th>'
    while b in a:
        startw=a.find(b)+len(b)
        endw=a.find(c,startw)
        startd=endw+9
        endd=a.find('</td>',startd)
        d[a[startw:endw]]=a[startd:endd]
        a=a[endd:]

        
