# Template code for dealing with
# abstract syntax trees for symbolic structures.
# revised with occurs check.
# Matthew Stone
# CS 503 Fall 2013
#
# File organization -- three parts
# *** DEFINITIONS ***
# *** OUTPUT ***
# *** UNIFICATION ***
# *** TEST CASES ***
# Find the part you want by search.

import re
import sys
import test

##########################################
# *** DEFINITIONS ***

# variables are strings
# that begin with an upper case letter
# or with the symbol _

def isvariable(t) :
    return isinstance(t, str) and \
        (t[0].isupper() or t[0] == "_")

# constants are strings that being with
# lower case letters
# or integers

def isconstant(t) :
    return (isinstance(t, str) and t[0].islower() or 
            isinstance(t, int))

# complex terms are tuples
#  we don't bother to check that the tuples
#  themselves really have the right constituency
#  really the tuples should have at least two
#  elements, and the first element 
#  should be a symbol and the remaining
#  elements should be terms
#  this means that the operations we define here
#  will actually be more general than the
#  abstract syntax trees that the parser builds.
#  this should not cause any problems.

def iscomplexterm(t) :
    return isinstance(t, tuple)

##########################################
# *** OUTPUT ***

# On the input side, arbitrary string constants
# can be recognized by surrounding them with ' quotes
# and escaping any 's or \s with a preceding \.
# Escape checks whether an expression can be
# read in as is (using the re.match statement)
# and if not transforms the string so it can be.

def escape(s) :
    if re.match(r'(\d+$)|([a-zA-Z_][A-Za-z0-9_]*$)', s) :
        return s
    else :
        return "'" + re.sub(r"([\\'])", r"\\\1", s) + "'"

# Takes an abstract syntax tree representing
# a term and prints it to the terminal,
# in a form that can be read in again by the parser

def prettyprintformulaterm(ft) :
    l = []
    def traverse(f) :
        if isvariable(f) :
            l.append(escape(f)),
        elif isconstant(f) :
            l.append(escape(str(f))),
        elif iscomplexterm(f) :
            l.append(escape(f[0]) + "("),
            for i in range(1,len(f)) :
                traverse(f[i])
                if i < len(f) - 1 :
                    l.append(", ")
            l.append(")")
    traverse(ft)
    return ''.join(l)

##########################################
# *** UNIFICATION ***

# Check whether the variable v
# occurs free in the interpretation of term t
# under substitution d.

def occursin(v, t, d) :
    if isvariable(t) :
        if v == t :
            return True
        if t in d :
            return occursin(v, d[t], d)
        return False
    if isconstant(t) :
        return False
    if iscomplexterm(t) :
        for subterm in t :
            if occursin(v, subterm, d) :
                return True
    return False

# Basic unification operation:
# Extend bindings d destructively 
# to impose the minimal constraints necessary
# to ensure that t1 and t2 must be equal.
# Returns true if the operation is possible,
# returns false otherwise. 
# Bindings d are updated in either case,
# so in general it will be necessary to 
# copy a dictionary used elsewhere
# before providing it as an argument 
# to this function.
#
# The algorithm has three cases:
# - look up the values of variables,
#   and assign the value of free
#   variables to match the other term
# - make sure atoms are equal
# - for complex terms, make sure
#   there are corresponding subterms
#   and call unification on each pair
#   recursively, requiring success
#   for a shared binding in all cases 

def unify(t1, t2, d) :
    if isvariable(t1) and t1 in d:
        return unify(d[t1], t2, d)
    if isvariable(t2) and t2 in d :
        return unify(t1, d[t2], d)
    if isvariable(t1) :
        if t1 != t2 :
            if occursin(t1, t2, d) :
                return False
            d[t1] = t2
        return True
    if isvariable(t2) :
        if occursin(t2, t1, d) :
            return False
        d[t2] = t1
        return True
    if isconstant(t1) or isconstant(t2) :
        return t1 == t2
    if not iscomplexterm(t1) or not iscomplexterm(t2) :
        return False
    if len(t1) != len(t2) :
        return False
    for i in range(len(t1)) :
        if not unify(t1[i], t2[i], d) :
            return False
    return True

##########################################
# *** TEST CASES ***

def tu(t1, t2, v) :
    test.test("unify", lambda (x, y): unify(x, y, dict()), (t1, t2), v, str)

test_unify = False
if test_unify :
    # Check first case - do we follow variables in t1?
    tu(("f", "a", "X"), ("f", "X", "b"), False)
    tu(("f", "a", "X"), ("f", "X", "a"), True)

    # Check second case - do we follow variables in t2?
    tu(("f", "a", "b"), ("f", "X", "X"), False)
    tu(("f", "a", "a"), ("f", "X", "X"), True)

    # Check variables in t1
    tu(("f", "X"), ("f", "X"), True)
    tu(("f", "X"), ("f", "Y"), True)
    tu(("f", "X"), ("f", "a"), True)
    tu(("f", "X"), ("f", ("g", "X")), False)

    # Check variables in t2
    tu(("f", "a"), ("f", "X"), True)
    tu(("f", ("g", "X")), ("f", "X"), False)

    # Check constant matching
    tu("a", ("f", "a"), False)
    tu(("f", "a"), "a", False)

    # Unification of constants
    tu(("f", "a"), ("f", "b"), False)
    tu(("f", "a", "b"), ("f", "b"), False)
    tu(("f", "a"), ("f", "a"), True)

    # Unification of variables
    # Matching structure
    tu(("f", "X"), ("f", "b"), True)
    tu(("f", "X"), ("f", "Y"), True)
    tu(("f", "X"), ("f", "b", "b"), False)
    tu(("f", "X", "b"), ("f", "b"), False)
    tu(("f", "X", "X"), ("f", "a", "a"), True)
    tu(("f", "X", "X"), ("f", "Y", "a"), True)

    # Occurs check
    tu(("f", "X", "X"), ("f", "Y", ("g", "Y")), False)
