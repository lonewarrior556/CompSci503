# PLY-LEX and -YACC parser 
# for a simple logic programming language.
# revised to use fact and rule structures.
# Matthew Stone
# CS 503 Fall 2013

########################################
# Overview.
# This file contains three parts
# *** LEXER ***
#   specifications for lexical analysis
# *** PARSER ***
#   specifications for the parser
# *** UTILTIES ***
#   convenience and testing functions
# Search in the file to find the different sections.

import re
import rules

########################################
# *** LEXER ***
#  the lexer consists of a specification
#  of the tokens of the language,
#  and the rules for matching tokens
#  in the input string and constructing
#  token data.

tokens = (
    'LPAREN', 'RPAREN',
    'COMMA', 'DOT', 'IMP',
    'CONSTANT', 'NUMBER', 'STRING', 'VARIABLE',
    )

# Tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_DOT = r'\.'
t_IMP = r'=>'
t_CONSTANT = r'[a-z][a-zA-Z0-9_]*'
t_VARIABLE = r'[A-Z_][a-zA-Z0-9_]*'
t_ignore_COMMENT = r'\#.*'

# String constants are enclosed in 's
# and can contain any characters
# backslashes escape 's and backslashes

def t_STRING(t) :
    r"'([^\\']|\\.)*'"
    t.value = re.sub(r"\\([\\'])", r"\1", t.value[1:-1])
    return t

# Integer constants are possible
# they are converted internally into integer values

def t_NUMBER(t) :
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignore white space
t_ignore = ' \t\n\r'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

########################################
# *** PARSER ***

# flatten list
#   takes a recursive list structure and removes
#   creates a list containing all and only the
#   non-list elements of any component list
#   flattening a nested structure into a single level.
#   this is needed for cases where the abstract 
#   syntax tree considerably simplifies from the
#   actual grammar parse tree: e.g., the parse
#   structure
#     (args: term comma (args: term comma (args: term)))
#   really should just be
#     (args term term term)
#   in terms of the underlying abstract data.
#   this implementation of flatten is very efficient
#   and does not place large demands on the python
#   recursive stack.  you can find details about it
#   where i found it on the web:
#      http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html

def flatten(l) :
    i = 0
    while i < len(l):
        while isinstance(l[i], list):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return l

# Specifications of context free productions.
# the grammar and corresponding abstract syntax
# is given below
#
# program : statement
#         | statement program
#   abstract program: a list of abstract statements
#
# statement : term DOT
#           | term IMP statement
#   abstract statement: a fact or rule structure
# 
# term : NUMBER 
#      | STRING
#      | CONSTANT
#      | VARIABLE
#      | CONSTANT LPAREN args RPAREN
#   abstract atoms are either ints or strings
#   complex terms are tuples 
#      with function and args as elements
#
# args : term
#      | term COMMA args
#    args are stored abstractly and provisionally
#    as two-element lists.
#    the term clause flattens the arg structure.

def p_simple_program(p) :
    'program : statement'
    p[0] = [p[1]]

def p_complex_program(p) :
    'program : statement program'
    p[0] = p[2]
    p[0].append(p[1])

def p_simple_statement(p) :
    'statement : term DOT'
    p[0] = rules.FACT(p[1])

def p_complex_statement(p) :
    'statement : term IMP statement'
    p[0] = rules.RULE(p[1], p[3])

def p_atomic_term(p) :
    '''term : NUMBER 
            | STRING 
            | CONSTANT 
            | VARIABLE'''
    p[0] = p[1]

def p_function_term(p) :
    'term : CONSTANT LPAREN args RPAREN'
    p[0] = tuple(flatten([p[1], p[3]]))

def p_atomic_arg(p) :
    'args : term'
    p[0] = p[1]

def p_complex_arg(p) :
    'args : term COMMA args'
    p[0] = [ p[1], p[3] ]

def p_error(p) :
    print "Syntax error in input!"

import ply.yacc as yacc
parser = yacc.yacc()

########################################
# *** UTILTIES ***

# parse_program
#   convenience function
#   given string
#   returns abstract syntax for knowledge base

def parse_program(s) :
    result = parser.parse(s)
    result.reverse()
    return result

# parse_file
#   convenience function
#   given string filename
#   opens file
#   parses the definitions into a program
#   returns the program

def parse_file(s) :
    file = open(s, 'r')
    text = file.read()
    result = parse_program(text)
    file.close()
    return result

# Data to test the program.
# we define five strings that you can parse
# into programs of various kinds:
# r1, r2, m1, m2 and mkbs.

r1 = r'''
# base case
relevant(f(a,f(b,f(c,f(d,nil))))).
'''
r2 = r'''
# recursive case
relevant(f(X,Y)) =>
  relevant(Y).
'''
m1 = r'''
# base case
relevant(f(X,Y)) =>
  member(X, f(X,Y)).
'''
m2 = r'''
# recursive case
relevant(f(Z,Y)) =>
  member(X, Y) => 
    member(X, f(Z,Y)).
'''
mkbs = r'''
relevant(f(X,Y)) =>
  member(X, f(X,Y)).
relevant(f(Z,Y)) =>
  member(X, Y) => 
    member(X, f(Z,Y)).
relevant(f(X,Y)) =>
  relevant(Y).
relevant(f(a,f(b,f(c,f(d,nil))))).
'''
