from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob
bob.delay=0


def draw(t, length, n):
    if n == 0:
        return
    angle = 45
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

def order(n):
    if n%3 == 0:
        return 3
    elif n%2==0:
        return 2
    else:
        return 1

def fractaln(l,n):
    if n == 10:
        return
    fd(bob, l)
    lt(bob,60)
    fd(bob,l)
    rt(bob,120)
    fd(bob,l)
    lt(bob,60)
    fd(bob,l)
    if order(n) == 1:
        lt(bob,60)
        n=n+1
    elif order(n) == 2:
        rt(bob,120)
        n=n+1
    elif order(n) == 3:
        lt(bob,60)
        n=1
    fractaln(l,n)
    

fractaln(10,1)

def Koch(length):
    fd(bob,length)
    lt(bob,60)
    fd(bob,length)
    rt(bob,120)
    fd(bob,length)
    lt(bob,60)
    fd(bob,length)

def fractal(l):
    Koch(l/3)
    lt(bob,60)
    Koch(l/3)
    rt(bob,120)
    Koch(l/3)
    lt(bob,60)
    Koch(l/3)

def fractal2(l):
    fractal(l/3)
    lt(bob,60)
    fractal(l/3)
    rt(bob,120)
    fractal(l/3)
    lt(bob,60)
    fractal(l/3)

def fractal3(l):
    fractal2(l/3)
    lt(bob,60)
    fractal2(l/3)
    rt(bob,120)
    fractal2(l/3)
    lt(bob,60)
    fractal2(l/3)

def fractal4(l):
    fractal3(l/3)
    lt(bob,60)
    fractal3(l/3)
    rt(bob,120)
    fractal3(l/3)
    lt(bob,60)
    fractal3(l/3)


def snowflake(l):
    fractal4(l)
    rt(bob,120)
    fractal4(l)
    rt(bob,120)
    fractal4(l)
    rt(bob,120)


wait_for_user()

