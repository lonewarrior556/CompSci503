# Classes for creating facts and rules
# Matthew Stone
# CS 503 Fall 2013

# File organization -- two parts.
# *** FACTS ***
# *** RULES ***
# Find the part that you want by search.

import sys
import unify

# *** FACTS ***

class FACT(object) :

    # A fact just has a single term as its body
    def __init__(self, body) :
        self.term = body

    # Apply a method to the a fact
    # by operating on the term body
    def app(self, fn) :
        fn(self.term)

    # Transform the representation of a
    # fact by doing some operation to the body
    def xform(self, fn) :
        return FACT(fn(self.term))

    # Print out a fact to a terminal, 
    # in a form that can be read in again
    # by the parser

    def prettyprint(self, n) :
        sys.stdout.write(n * " ")
        sys.stdout.write(unify.prettyprintformulaterm(self.term))
        sys.stdout.write(".\n")

    # Give a one-line description of a fact as a string
    def __str__(self) :
        return ("FACT " + unify.prettyprintformulaterm(self.term))

    # Compare facts: requires exact identity
    # (that is, no renaming of variables)
    def __eq__(self, other) :
        return isinstance(other, FACT) and self.term == other.term

    def __ne__(self, other) :
        return not isinstance(other, FACT) or self.term != other.term

# *** RULES ***

class RULE(object) :

    # A fact has a term as an antecedent 
    # and either a fact or rule as its consequent.
    def __init__(self, antecedent, consequent) :
        self.cond = antecedent
        self.result = consequent

    # Apply a method to a rule
    # by operating on the term antecedent
    # and applying recursively to the consequent
    def app(self, fn) :
        fn(self.cond)
        self.result.app(fn)

    # Transform the representation of a
    # rule by doing some operation to the
    # antecedent and applying the transformation
    # recursively to the consequent
    def xform(self, fn) :
        return RULE(fn(self.cond), self.result.xform(fn))

    # Print out a fact to a terminal, 
    # in a form that can be read in again
    # by the parser
    def prettyprint(self, n) :
        sys.stdout.write(n * " ") 
        sys.stdout.write(unify.prettyprintformulaterm(self.cond))
        sys.stdout.write(" =>\n")
        self.result.prettyprint(n + 3)

    # Give a one-line description of a fact as a string
    def __str__(self) :
        return ("RULE " + unify.prettyprintformulaterm(self.cond) + " => " \
                    + str(self.result))

    # Compare facts: requires exact identity
    # (that is, no renaming of variables)
    def __eq__(self, other) :
        return isinstance(other, RULE) and \
            self.cond == other.cond and self.result == other.result

    def __ne__(self, other) :
        return not isinstance(other, RULE) or \
            self.cond != other.cond or self.result != other.result

# Takes the abstract syntax tree representing
# a knowledge-base program and prints it to
# the terminal, in a form that can be read
# in again by the parser.

def prettyprintkb(d) :
    for f in d :
        f.prettyprint(0)

