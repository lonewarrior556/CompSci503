import collections

def plus(t) :
    result = 0
    for a in t :
        result += a
    return result

def times(t) :
    result = 1
    for a in t :
        result *= a
    return result

def minus(t) :
    if t == [] :
        return 0
    result = t[0]
    for a in t[1:] :
        result -= a
    return result

def div(t) :
    if len(t) != 2 :
        return 0
    return t[0] / t[1]

def calc(expr) :
    if isinstance(expr, int) :
        return expr
    if callable(expr) :
        return expr
    if isinstance(expr, collections.Sequence) :
        l = map(calc, expr)
        return l[0](l[1:])

p1 = (plus, 1, (times, 2, 3))
p2 = [plus, 1, [times, 2, 3]]
# map(lambda x: x[1,2,3], [1,2,3])
# [[1,2,3],[1,2,3,1,2,3],[1,2,3,1,2,3,1,2,3]]
                 
