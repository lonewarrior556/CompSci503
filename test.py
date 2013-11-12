# Class for defining test cases for programs
# Matthew Stone
# CS 503 Fall 2013

global count
global verbose

count = 1
err_ct = 0
verbose = False

def test(label, fn, args, result, viz) :
    global count
    global verbose
    global err_ct
    try :
        guy = fn(args)
        if guy == result :
            if verbose :
                print "Test", str(count), \
                    "(" + label + "): correctly gives", \
                    viz(result)
        else :
            print "Test", str(count), "(" + label + "): failed"
            print "     Should give:", viz(result)
            print "  Actually gives:", viz(guy)
            err_ct += 1
    except Exception as e :
        print "Test", str(count), "(" + label + "): failed"
        print "Raised exception", type(e).__name__, ":", e
        err_ct += 1
    count = count + 1

def test_report() :
    if err_ct == 0 :
        if verbose :
            print "(All tests run have succeeded.)"
    else :
        print "Testing failure:", str(err_ct), "tests have failed."

