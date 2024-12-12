# The Intent, Structure, and Purpose of Our Language

Our group created a language to help the visually unimpaired learn Braille using a simple machine. The goal is to translate Braille into a 3x2 grid of 6 dots (1s and 0s), which can then 
be read by our machine to identify the corresponding character.

This is simply a brief synopsis of our language and a lesson in how to use our machine and language at a technical level. For a more in-depth description of our language's intent, purpose, 
and structure, please see the [Language Summary](Documentation/language_summary.md).

The requirements of the EECS 510 final project are fulfilled in this repository, and you can access them through the various folders. For part 1, refer to the above summary. For parts 2 and 3, refer to [AutomataAndTesting](AutomataAndTesting/). For parts 4 and 5, check out [DataStructure](DataStructure/). These are linked below with instructions on when you might want to use them, but this is for those not grading. These links are only provided for the convenience of the grader/professor. Thanks for grading!

## Purpose and Intent

We aim to:
- Enable visually unimpaired users to learn Braille using a mobile app or other devices.
- Translate Braille into a binary grid (6 dots: 1s and 0s) for machine input.
- Create a formal grammar that can be used in future projects, like an augmented reality (AR) app to scan and read Braille via a phone camera.

Our broader goal is to promote empathy and communication with the visually impaired and encourage learning Braille as a valuable skill.

## Language Structure

- **Alphabet:** Covers the 26 letters of the English alphabet (no symbols or numbers for this version).
- **Machine Process:** The machine reads 6-bit binary input and matches it to a dictionary of characters. If the input is invalid or doesn’t match, the machine rejects it.
- **Smallest Valid Input:** The empty string (`λ`) doesn’t trigger the machine’s processing.
- **Visualization:** To visualize the language, visit the [AutomataAndTesting](AutomataAndTesting/) directory and check out our diagram. A comprehensive DFA diagram of our machine is available.

### Key Features:
- **Input Format:** Braille as 6-bit binary strings (1s and 0s).
- **State Machine:** A deterministic finite automaton (DFA) matches input to characters in a dictionary.
- **Invalid Input:** The machine rejects invalid input that doesn't match a character.

## Purpose Beyond the Project

- **Global Impact:** Over 250 million blind people worldwide (National Library of Medicine), yet few resources exist to help the sighted understand them.
- **Empathy & Communication:** The machine is a tool to help the sighted empathize with the blind by learning Braille and understanding their experiences.
  
### Vision:
- We aim to build an app that not only scans Braille but also teaches users how to read it through a progression-based learning system.
- While similar ideas exist, our focus is on making learning Braille accessible and engaging for the sighted, rather than just providing a tool.

## Overall:
Our project is more than a machine—it’s a step toward fostering empathy, understanding, and communication between the sighted and the visually impaired. This language can lay the foundation for future 
applications that improve accessibility.

## Using the Machine's Code
- The program requires three files to operate.
- **driver.py:** The main file that imports the other two files, creates and defines the DFA, and tests input strings on the machine. The output of the machine comes from the print(accept(a, w)) statement.
- **test.py:** Holds the accept() function which is used to test the DFA by validating inputs, breaking the input into 6-bit chunks, and traversing the DFA until it is found to be invalid (rejects) or valid (accepts with a list of transitions).
- **data_structure.py:** Holds the data structure, A, as a Python class for our DFA.

## Running the Test Cases
- The DFA can be tested by printing the output of the accept function in driver.py.
- There is an example in line 109 of driver.py that can be altered to test different inputs.
- Outputting line example: print(accept(a, "100000"))
- To run the test cases yourself, ensure that you have all files from the [DataStructure](DataStructure/) folder downloaded, and are in a Python environment.

Examples:    
```
Input: "100000101000110000" (a=100000, b=101000, c=110000)    
Output:    
accept    
q0 1 q1    
q1 0 q2    
q2 0 q3    
q3 0 q4    
q4 0 q5    
q5 0 q6    
q6 a q0    
q0 1 q1    
q1 0 q2    
q2 1 q7    
q7 0 q8    
q8 0 q9    
q9 0 q10    
q10 b q0    
q0 1 q1    
q1 1 q11    
q11 0 q12    
q12 0 q13    
q13 0 q14    
q14 0 q15    
q15 c q0    

Input: "011101" (w=011101)    
Output:    
accept    
q0 0 q32    
q32 1 q33    
q33 1 q34    
q34 1 q38    
q38 0 q39    
q39 1 q63    
q63 w q0    

Input: "1100" (Invalid, too short)    
Output:    
reject    

Input: "100000111111" (a=100000, 111111 is invalid) (Invalid, 111111 not reachable through DFA and therefore not a letter)    
Output:    
reject    
```
