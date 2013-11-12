# Finite State Automata
# CS 503, Fall 2011
# Matthew Stone
# Implementation of Deterministic Automata

class DFA(object) :

    # A DFA must have a complete set of transitions.
    # The initial state must be a state
    # The final states must be states
    def check_integrity(self) :
        for s in self.states :
            assert s in self.transitions, \
                "No rule for " + str(s)
            for i in self.symbols :
                assert i in self.transitions[s], \
                    "No rule for " + str(i) + " in " + str(s)
                assert self.transitions[s][i] in self.states, \
                    "Transition "  + str(i) + " in " + str(s) + \
                    " to bad state " + str(self.transitions[s][i])
        assert self.initial in self.states, \
            "Bad initial state " + str(self.initial)
        for s in self.final :
            assert s in self.states, \
                "Bad final state " + str(s)

    # Create a DFA with associated parameters:
    # states: the collection of states
    # symbols: the collection of possible input symbols
    # transitions: the double dictionary giving the function 
    #    from states and symbols to states
    # initial: the initial state
    # final: the collection of final states
    # Make sure that the resulting object is legal,
    # by calling the check_integrity method.

    def __init__(self, states, symbols, transitions, initial, final) :
        self.states = frozenset(states)
        self.symbols = frozenset(symbols)
        self.transitions = transitions.copy()
        self.initial = initial
        self.final = frozenset(final)
        self.check_integrity()

    # Determine whether a DFA accepts the passed sequence

    def accepts(self, sequence) :
        current_state = self.initial
        for i in sequence :
            assert i in self.symbols, \
                "Unrecognized input symbol " + str(i)
            current_state = self.transitions[current_state][i]
        return current_state in self.final

# Examples
parity =  DFA(['even', 'odd'],
              [0, 1],
              {'even': {0: 'even', 1: 'odd'},
               'odd': {0: 'odd', 1: 'even'}},
              'even',
              ['even'])


"""
compare two strings print out every string up to a limit where they do not agree
"""
