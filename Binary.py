def value(n):
	if len(n) == 0:
		return 0
	elif n[0] == 0 or n[0] ==1 :
		return n[0] + 2 * value(n[1:])
	else :
		print "Bad Value", n[0], "is not binary!"



def add1(n):
    if len(n) ==0:
        return [1]
    elif n[0] == 0:
        return [1] + n[1:]
    elif n[0] ==1 :
        return [0] + add1(n[1:])
    else :
        raise Exception("bad value was entered")
