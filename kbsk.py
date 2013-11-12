# CS 503 Fall 2013
# Skeleton code for an interpreter for a
# "deductive database" or "production rule"
# programming language.
#
# There are four things that you have to write
# to complete this file:
# *** RENEW ***
#   a set of functions to replace all the 
#   variables in an expression with fresh copies
#   needed to enforce the meanings of
#   logic variables as universally quantified
#   and make inference generic
# *** INFER ***
#   the basic function to implement a step of
#   modus ponens and yield the conclusion if
#   any
# *** RUN ***
#   a process to figure out all the conclusions
#   that follow from a program; implemented
#   with a queue.
# *** QUERY ***
#   a user-level process to figure out what 
#   instances of a passed formula are true 
#   in the result of running a program.
# Search in the file to find these sections

import unify
import rules
import st
import collections
import test

test.verbose = True

########################################
# *** RENEW ***

# function gensym
#   make a new name that has never
#   appeared before that begins with
#   the passed prefix

_gensym_count = 0

def gensym(prefix) :
    global _gensym_count
    _gensym_count = _gensym_count + 1
    return prefix + str(_gensym_count)

# function copy
#   take a collection of variables as input
#   return a dictionary that associates
#   each of these old variables with a
#   fresh variable that has never been
#   considered before in running the
#   program.  

def copy(variables) :
    d = dict()
    for v in variables:
        d[v] = gensym(v)
    return d

# function index
#   take a collection of variables as input
#   return a dictionary that associates
#   each of these old variables with
#   consecutive integers.  

def index(variables) :
    count = 0
    d = dict()
    for v in variables :
        d[v] = "X" + str(count)
        count += 1
    return d

# function substitute
#   given a term and a binding dictionary d
#   construct a corresponding term
#   where each occurrence of a variable
#   has been replaced by whatever value
#   it has in d.
#   note: you should also substitute inside the
#   value given by d!  
#   hint: works by structural recursion 
#   on terms.
#   caveat: be sure to return complex results
#   as tuples.  you can always convert a list fred
#   to a tuple by saying tuple(fred).

# def substitute(t, d)
#   your code here

# tests for subsitute
# always use the same substitution
# { "X": ("f", "a"), "Y" : ("g", "X") }

def ts(term, answer) :
    test.test("substitute", 
              lambda t : substitute(t, { "X": ("f", "a"), "Y" : ("g", "X") }),
              term, 
              answer,
              str)

test_substitute = False
if test_substitute :
    # Base cases
    ts("f", "f")
    ts(1, 1)
    ts("X", ("f", "a"))
    # Recursive cases
    ts(("g", "X"), ("g", ("f", "a")))
    ts(("g", ("f", "X")), ("g", ("f", ("f", "a"))))
    # Substitution requires recursive passes
    # (substitute recursively into own output)
    ts(("g", "Y"), ("g", ("g", ("f", "a"))))

# function addvariables
#   given a term t and a list vrs,
#   update l by appending to vrs
#   each of the variables that occurs in t
#   that is not yet a member of vrs
#   hint: uses structural recursion
#   heads up: the otherwise more natural 'vars'
#      is reserved keyword in python
#
#   additional note: it would be more efficient
#   to use a set structure in addvariables,
#   other things being equal.
#   But set structures in python are ordered
#   by the hash value of their elements.
#   It is important for the way addvariables
#   is used throughout the program that
#   the variables be listed in the order 
#   that they occur in the term.

# def addvariables(t, vrs) :
#   your code here

# tests for add variables
def tav(term, answer) :
    x = []
    addvariables(term, x)
    test.test("addvariables", lambda v : x, (), answer, str)

test_addvariables = False
if test_addvariables :
    # Base cases
    tav("a", [])
    tav(1, [])
    tav("X", ["X"])
    # Recursive cases
    tav(("f", "X", "Y"), ["X", "Y"])
    tav(("f", "X", ("g", "Y")), ["X", "Y"])
    tav(("f", "X", "X"), ["X"])

# function renew(fr)
#   make a copy of fact or rule FR in which 
#   all the variables in FR are
#   replaced by new values.
#   pseudocode:
#   - find the variables that
#     occur in FR
#   - create a substitution that
#     maps the variables to unique
#     new variables
#   - infer the substitution to FR
#   - return the result

def renew(fr) :
    vrs = []
    fr.app(lambda t:addvariables(t, vrs))
    subs = copy(vrs)
    return fr.xform(lambda t:substitute(t, subs))

########################################
# *** INFER ***

# function infer
#   implement modus ponens with unification
#   given:
#     FACT fact
#     RULE rule
#   make a new copy of the fact and the rule
#   to handle the universally quantified
#   variables in the two expressions.
#   try to unify the fact body (copy_of_fact.body)
#   and antecedent of the rule (copy_of_rule.cond)
#   if this succeeds, you'll get a substitution out.
#   use this substitution to return an
#   instance of the result expression
#   (copy_of_rule.result)
#   incorporating the constraints 
#   discovered from unification.
#   otherwise, return None

# def infer(premise, antecedent, result)
#   your code here

# test inference
# these tests depend on a correct implementation
# of addvariables and substitute, 
# so get those working first,
# before enabling these tests.

# deal with the fact that terms will have
# different variables because of the
# renaming of variables involved in
# inference.

def normalize(t) :
    if t == None :
        return t
    vs = []
    t.app(lambda p:addvariables(p,vs))
    subs = index(vs)
    return t.xform(lambda p:substitute(p, subs))

def ti(factstr, rulestr, resultstr) :
    try :
        fact = st.parse_program(factstr)[0]
        rule = st.parse_program(rulestr)[0]
        if resultstr != None :
            result = st.parse_program(resultstr)[0]
            canonical = normalize(result)
        else :
            canonical = None
        test.test("infer",
                  lambda (f,r) : normalize(infer(f, r)),
                  (fact, rule),
                  canonical,
                  str)
    except Exception as e :
        print "Infer test badly specified:", str(e)

test_infer = False
if test_infer :
    # Propositional inference
    ti("a.", "a => b.", "b.")
    ti("c.", "a => b.", None)
    ti("a.", "a => b => c.", "b => c.")

    # Instantiating variables
    ti("a(k).", "a(X) => b(X).", "b(k).")
    ti("a(k).", "a(l) => b(l).", None)
    ti("a(k).", "a(X) => b(X) => c(X).", "b(k) => c(k).")
    ti("a(X).", "a(k) => b(k).", "b(k).")
    ti("a(X).", "a(k) => b(k) => c(k).", "b(k) => c(k).")

    # Free variables
    ti("a(k).", "a(X) => b(X,Y).", "b(k,Y).")
    ti("a(k).", "a(X) => b(X,Y) => c(X,Y).", "b(k,Y) => c(k,Y).")

########################################
# *** RUN ***
#
# For running a program,
# it's convenient to keep two lists 
# storing the formulas you've processed so far:
# - one list of the atomic facts (facts)
# - and one list of the implications (rules)
# You also need a queue of 
# information that you still have to process
# create a queue with
#   collections.deque(initial_items)
# add something to the queue with
#   queue.appendleft(x)
# remove something from the queue with
#   queue.pop()

# Propagate
#   called when a new fact is discovered
#   to find all the consequences of the fact
# arguments:
#   new fact
#   list of rules
#   queue
# for each rule, use infer to check whether
# the fact leads to a new inference, and 
# if so, enqueue it.

# def propagate(fact, rules, queue) :
#   your code here

# Fire
#   called when a new rule is discovered
#   to find all the results of using the
#   rule on existing data
# arguments:
#   new rule
#   list of facts
#   queue
# for each fact, use infer to check whether
# the rule leads to a new inference, and 
# if so, enqueue it.

# def fire(rule, facts, queue) :
#   your code here

# testing code for propagate and fire

def tx(itemstr, programstr, resultstr, name, op) :
    try :
        item = st.parse_program(itemstr)[0]
        program = st.parse_program(programstr)
        if resultstr != None :
            result = st.parse_program(resultstr)
            canonical = map(normalize, result)
        else :
            canonical = []
        queue = collections.deque()
        def process (pr) :
            (i, l) = pr
            op(i, l, queue)
            return map(normalize, list(reversed(queue)))
        test.test(name, process, (item, program), canonical, lambda x:map(str,x))
    except Exception as e :
        print name, "test badly specified:", str(e)

test_propagate = False
if test_propagate :
    # Propositional cases
    tx("a.", "a => b.", "b.", 
       "propagate", propagate)
    tx("b.", "a => b.", None, 
       "propagate", propagate)
    tx("a.", "a => b. a => c.", "b. c.", 
       "propagate", propagate)

    # First-order cases
    tx("a(k).", "a(X) => b(X).", "b(k).", 
       "propagate", propagate)
    tx("b(k).", "a(X) => b(X).", None, 
       "propagate", propagate)
    tx("a(k).", "a(X) => b(X).  a(X) => c(X).", "b(k).  c(k).", 
       "propagate", propagate)

    # Fancy
    tx("a(k).", 
       "a(X) => b(X,Y) => d(Y).", 
       "b(k,Y) => d(Y).", 
       "propagate", propagate)
    tx("a(k).", 
       "a(X) => b(X,Y) => d(Y).  a(X) => c(X,Y) => e(Y).", 
       "b(k,Y) => d(Y).  c(k,Y) => e(Y).", 
       "propagate", propagate)

test_fire = False
if test_fire :
    # Propositional cases
    tx("a => b.", "a.", "b.", 
       "fire", fire)
    tx("a => b.", "b.", None, 
       "fire", fire)

    # First-order cases
    tx("a(X) => b(X).", "a(k).", "b(k).", 
       "fire", fire)
    tx("a(X) => b(X).", "b(k).", None, 
       "fire", fire)
    tx("a(X) => b(X).", "a(k).  a(l).",  "b(k).  b(l).", 
       "fire", fire)

    # Fancy
    tx("a(X) => b(X,Y) => c(Y).", 
       "a(k).",
       "b(k,Y) => c(Y).",
       "fire", fire)
    tx("a(X) => b(X,Y) => c(Y).", 
       "a(k). a(l).",
       "b(k,Y) => c(Y). b(l,Y) => c(Y).",
       "fire", fire)

# Process
#   called when new information is discovered
# arguments:
#   item just inferred
#   list of facts
#   list of rules
#   queue
# check whether you have a fact or a rule,
# using isinstance
# if it's a fact,
#   check if it occurs in facts
#   if not, propagate it and add it to facts
# if it's a rule
#   check if it occurs in rules
#   if not, fire it and add it to rules
#
# it's easy to see that testing for 
# a formula that you already have by equality
# is a shortcut around what logic would
# dictate in general, but it's enough for 
# this assignment.  if you want to be 
# fancier, you can normalize facts and rules
# before putting them into the lists,
# and before comparing them.

# def process(item, factlist, rulelist, queue) :
#   your code here.

# Run
#   puts everything together
# input
#   a list of formulas
# output
#   all the consequences of the rules
#
# put all the items on the queue
# then process items while items remain on the queue
# return a pair
#   (facts, rules)
# showing what you have inferred

def run(items) :
    queue = collections.deque(items)
    factlist = []
    rulelist = []
    while len(queue) != 0 :
        process(queue.pop(), factlist, rulelist, queue)
    return (factlist, rulelist)

########################################
# *** QUERY ***

# query
# arguments:
#    a fact with variables
#    a list of facts
# return
#    the substitution instances that can be obtained
#    by successfully unifying pattern with 
#    a fact in the passed list.

def query(pat, factlist) :
    results = []
    for f in factlist :
        b = dict()
        if unify.unify(pat.term, f.term, b) :
            results.append(pat.xform(lambda t:substitute(t, b)))
    return results

# qt
#   short for query text
#   user-level query function
# given a string representing a program
# and the facts resulting from running a program
# print out all the instances of the string
# in the facts.

def qt(string, factlist) :
    pat = ast.parse_program(string)
    assert isinstance(pat, rules.FACT), \
        "Error: Can only query facts"
    rules.prettyprintkb(query(pat, factlist))

# Print out overall status
test.test_report()
