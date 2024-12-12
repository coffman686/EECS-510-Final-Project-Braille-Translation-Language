class A:
    def __init__(self):
        self.states = []
        self.inputs = []
        self.start = None
        self.accepts = []
        self.transitions = {}

    def add_state(self, state, isAccept = False):
        self.states.append(state)
        if isAccept:
            self.accepts.append(state)

    def add_start(self, state):
        self.start = state

    def add_transition(self, fromState, symbol, toState):
        if fromState not in self.transitions:
            self.transitions[fromState] = {}
        if symbol not in self.transitions[fromState]:
            self.transitions[fromState][symbol] = []
        if toState not in self.transitions[fromState][symbol]:
            self.transitions[fromState][symbol].append(toState)
    
    def add_all_transitions(self, transitions):
        for fromState, symbol, toState in transitions:
            self.add_transition(fromState, symbol, toState)

    def display(self):
        print("States:", self.states)
        print("Input Symbols:", self.inputs)
        print("Start State:", self.start)
        print("Accept States:", self.accepts)
        print("Transitions:")
        for fromState, transitions in self.transitions.items():
            for symbol, toState in transitions.items():
                print(f"{fromState} --{symbol}--> {toState}")