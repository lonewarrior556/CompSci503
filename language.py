# Automata and search
# CS 503, Fall 2013
# Matthew Stone
# Search methods for exploring the languages of automata
# Slightly revised from class to work for both DFAs and NFAs

import dfa
import nfa
from nfa import *
from dfa import *



# PART I
# SEARCH

# Helper for iterative deepening search
# Print out all the strings that machine accepts
# that begin with prefix and contain depth further symbols

def search_strings1(machine, prefix, depth) :
    if depth <= 0 :
        if machine.accepts(prefix) :
            print prefix
    else :
        for i in machine.symbols :
            next = list(prefix)
            next.append(i)
            search_strings(machine, next, depth - 1)

# Iterative deepening search
# Print out all the strings of length less than limit
# which machine accepts

def print_language(machine, limit) :
    for length in range(limit) :
        search_strings(machine, [], length)

# Exercise
# Adapt the code above to solve the following problem.
# Suppose you are given two machines m1 and m2,
# such that m1.symbols is the same set as m2.symbols.
# Suppose you are also given a length limit.
# The task is as follows:
# Print out a description of all the strings 
# composed of the symbols of the machines
# of length shorter than limit
# where the machines have different behavior 
# (that is, m1 accepts the string and m2 rejects it,
#  or m2 accepts the string and m1 rejects it)

# Your code here
# def mismatches(m1, m2, limit) : ...

def search_strings(m1,m2, prefix, depth) :
    if depth <= 0 :
        if m1.accepts(prefix)and not m2.accepts(prefix):
            print prefix, str(m2)+ 'rejects'
        if not m1.accepts(prefix) and m2.accepts(prefix):
            print prefix, str(m1)+ 'rejects'
    else:
        for i in m1.symbols :
            next = list(prefix)
            next.append(i)
            search_strings(m1,m2, next, depth - 1)


def mismatches(m1,m2, limit) :
    for length in range(limit) :
        search_strings(m1,m2, [], length)


# PART II
# AUTOMATA

# Exercise
# Explore the correspondence between NFAs and DFAs.
# Construct some NFAs, drawing on the examples in Rosen's book.
# Write testing code that will create corresponding DFAs,
# and make sure that the languages of the DFAs and the NFAs 
# are the same.

def nfa2dfa(nfa):
    import itertools
    keys=[]
    for i in range(1,len(nfa.states)+1):
        keys.extend(list(itertools.combinations(tuple(sorted(list(nfa.states))),i)))
    d=dict()
    for x in keys:
        if len(x)==1:
            d[x]=dict()
            temp=nfa.transitions[x[0]]
            for z in nfa.symbols:
                d[x][z]=tuple(sorted((temp.get(z))))
        else:
            d[x]=dict()
            for z in nfa.symbols:
                d[x][z]=tuple(sorted(list(set(d[x[:-1]].get(z)+(d[x[-1:]].get(z))))))
    ls=[]
    for x in nfa.final:
        for y in keys:
            if x in y:
                ls.append(y)
    return DFA(keys,nfa.symbols,d,(nfa.initial,),ls)




# PART III
# Manipulating Automata

# Exercise
# Write a function complement as described below.
# Given a DFA m, complement(m) returns another DFA.
# If S is a list of symbols in the input alphabet of m,
# complement(m).accepts(S) is true
# exactly when
# m.accepts(S) is false

def complement(dfa):
    ls=list(dfa.states)
    for x in dfa.final:
        ls.remove(x)
    return DFA(dfa.states,dfa.symbols,dfa.transitions,dfa.initial,frozenset(ls))

# Write a function intersection as described below.
# Given two DFAs, m1 and m2, intersection(m1,m2)
# returns another DFA.
# If S is a list of symbols in the input alphabet of m1 and m2,
# intersection(m1,m2).accepts(S) is true
# exactly when
# m1.accepts(S) is true and m2.accepts(S) is true


def intersection(m1,m2):
    import itertools
    states=list(itertools.product(m1.states,m2.states))
    d=dict()
    for x in states:
        d[x]=dict()
        for y in m1.symbols:
            d[x][y]=(m1.transitions[x[0]][y],m2.transitions[x[1]][y])
    final=list(itertools.product(m1.final,m2.final))

    return DFA(states,m1.symbols,d,(m1.initial,m2.initial),final)
