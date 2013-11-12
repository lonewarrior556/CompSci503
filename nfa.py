# Finite State Automata
# CS 503, Fall 2013
# Matthew Stone
# Initial Implementation of Nondeterministic Automata

import dfa

class NFA(object) :

    # Make sure the NFA is legal
    # The dictionary should enable lookup of each state
    # Everything found there must be a valid state
    # The initial state must be a valid state
    # Each final state must be a valid state
    def check_integrity(self) :
        for s in self.states :
            assert s in self.transitions, \
                "No rule for " + str(s)
            for i in self.symbols :
                assert i in self.transitions[s], \
                    "No rule for " + str(i) + " in " + str(s)
                out = self.transitions[s][i]
                try:
                    for n in out:
                        assert n in self.states, \
                            "Transition "  + str(i) + " in " + str(s) + \
                            " to bad state " + str(n)
                    self.transitions[s][i] = frozenset(out)
                except TypeError:
                    raise AssertionError("Transition " + str(i) + " in " + 
                                         str(s) + " to bad set " + str(out))
        assert self.initial in self.states, \
            "Bad initial state " + str(self.initial)
        for s in self.final :
            assert s in self.states, \
                "Bad final state " + str(s)

    # Create an NFA with associated parameters:
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

    # Simulate the recognition of a string by an NFA
    # using depth-first search.
    # 
    # try_to_recognize(NFA, sequence, state, pos)
    #   Helper function:
    #   Returns true if you can reach an accepting state
    #   by starting from the specified state and 
    #   analyzing the remainder of the input, as
    #   given by sequence[pos:]

    def try_to_recognize(self, sequence, state, pos) :
        if pos == len(sequence) :
            return state in self.final
        options = self.transitions[state][sequence[pos]]
        for s in options :
            if self.try_to_recognize(sequence, s, pos + 1) :
                return True
        return False

    # Main method:
    # Returns true if you can reach an accepting state
    # starting in the initial state of the machine and
    # analyzing the complete input specified by sequence.

    def accepts(self, sequence) :
        return self.try_to_recognize(sequence, self.initial, 0)

    # NFA to DFA construction
    # give the set of states that the NFA could transition to
    # if it starts in any of the states in states and sees
    # input symbol

    def dfa_transition(self, states, symbol) :
        n = set()
        for s in states:
            n.update(self.transitions[s][symbol])
        return frozenset(n)

    # NFA to DFA construction
    # return an index corresponding to a state set
    # maintaining the queue of states to consider
    # so that you can track the progress in constructing
    # the DFA

    def get_dfa_state(self, state_set) :
        if not state_set in self.dfa_states :
            v = len(self.dfa_states)
            self.dfa_states[state_set] = v
            self.unmarked_dfa_states.add(state_set)
        return self.dfa_states[state_set]

    # NFA to DFA construction
    # Consider all the possible transitions you need 
    # in the dfa, starting from the passed state_set

    def make_dfa_transitions(self, state_set) :
        fro = self.get_dfa_state(state_set)
        self.dfa_transitions[fro] = dict()
        for i in self.symbols :
            self.dfa_transitions[fro][i] = \
                self.get_dfa_state(self.dfa_transition(state_set, i))

    # NFA to DFA construction
    # Organize the bookkeeping to create a DFA from an NFA
    # Uses five auxiliary data structures
    # dfa_states: dictionary mapping sets of nfa states to 
    #    states in dfa (numbers)
    # unmarked_dfa_states: sets of nfa states whose 
    #    dfa transitions have not yet been created
    # dfa_start: initial state in dfa
    # dfa_transitions: table of transitions for dfa
    # dfa_final: sets of dfa states that count as accepting states
    # Basic operation is a loop,
    # starting with the initial state,
    # create transitions for new dfa states you have encountered
    # until all the dfa states are spoken for
    # figure out which are final states
    # create a dfa with the resulting structures

    def to_dfa(self) :
        self.dfa_states = dict()
        self.unmarked_dfa_states = set()
        start = frozenset([self.initial])
        self.dfa_start = self.get_dfa_state(start)
        self.dfa_transitions = dict()
        while (len(self.unmarked_dfa_states) != 0) :
            todo = self.unmarked_dfa_states.pop()
            self.make_dfa_transitions(todo)
        self.dfa_final = []
        for (k,v) in self.dfa_states.items() :
            if len(k.intersection(self.final)) != 0 :
                self.dfa_final.append(v)
        return dfa.DFA(self.dfa_states.values(),
                   self.symbols,
                   self.dfa_transitions,
                   self.dfa_start,
                   self.dfa_final)


# This machine is actually deterministic but uses the NFA representation
parity =  NFA(['even', 'odd'],
              [0, 1],
              {'even': {0: ['even'], 1: ['odd']},
               'odd': {0: ['odd'], 1: ['even']}},
              'even',
              ['even'])

# This machine accepts any string except those with a single 1

hilarity = NFA(['even', 'odd'],
               [0, 1],
               {'even': {0: ['even'], 1: ['odd']},
                'odd': {0: ['odd'], 1: ['odd', 'even']}},
               'even',
               ['even'])

# just a test machine with same language as hilarity but different transitions

hilarity2 =NFA(['even', 'odd'],
               [0, 1],
               {'even': {0: ['even'], 1: ['odd']},
                'odd': {0: ['odd','even'], 1: ['even']}},
               'even',
               ['even'])

messy = NFA(['s1', 's2', 's3', 's4'],
            ['a', 'b'],
            {'s1': {'a' : ['s2'], 'b' : ['s1', 's3']},
             's2': {'a' : ['s4'], 'b' : ['s4', 's3']},
             's3': {'a' : ['s1'], 'b' : ['s2']},
             's4': {'a' : ['s3'], 'b' : ['s4']}},
            's1',
            ['s1', 's3'])
