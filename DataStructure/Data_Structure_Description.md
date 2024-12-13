# Python Data Structure Description

## Class Variables
- `self.states`: A list of all states in the automaton (e.g., `q0`, `q1`, `q2`, etc.).  
- `self.inputs`: A list of valid input symbols (e.g., `0`, `1`).  
- `self.start`: The declared starting state for the automaton (e.g., `q0`).  
- `self.accepts`: A list of final accepting states.  
- `self.transitions`: A dictionary of dictionaries that represents the valid transitions between states.  
  - **Outer Dictionary**: Keys are the source states.  
  - **Inner Dictionary**: Keys are symbols, and values are the destination states.  

---

## Class Methods
- **`add_state`**: Adds a single possible state to the automaton with an option to mark it as an accepting state.  
- **`add_start`**: Sets the starting state of the automaton.  
- **`add_transition`**: Adds a single transition between two states with a single symbol.  
- **`add_all_transitions`**: Adds all transitions from a correctly formatted list.  
- **`display`**: Displays the possible states, symbols, starting state, accepting states, and transitions of the automaton.  

---

# Data Structure Text Representation Description

Our data structure can also be represented as a file (data_structure_text_representation.txt) containing **96 lines**, where each line serves a specific purpose:  

1. **Line 1**: A whitespace-separated list of the states.  
2. **Line 2**: A whitespace-separated list of input symbols.  
3. **Line 3**: The start state.  
4. **Line 4**: A whitespace-separated list of accept states.  
5. **Lines 5–96**: Each line represents one transition with exactly three whitespace-separated elements:  
   - **1st Element**: The state the transition leaves from.  
   - **2nd Element**: The symbol the transition reads.  
   - **3rd Element**: The state the transition goes to.  

**Note**:  
- Letter symbols designate the letter that the six-digit string produces but act as a lambda in the automaton.
