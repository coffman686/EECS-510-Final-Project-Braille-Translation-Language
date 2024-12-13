# Grammar for the Language
## The following is the formal grammar written for our langauge:
S     ->  0Q32 | 1Q1 | λ

Q1   ->  0Q2 | 1Q11

Q2   ->  0Q3 | 1Q7

Q3   ->  0Q4 | 1Q19

Q4   ->  0Q5 | 1Q41

Q5   ->  0S

Q7   ->  0Q8 | 1Q29

Q8   ->  0Q9 | 1Q43

Q9   ->  0S

Q11  ->  0Q12 | 1Q22

Q12  ->  0Q13 | 1Q16

Q13  ->  0Q14 | 1Q45

Q14  ->  0S

Q16  ->  0Q17 | 1Q47

Q17  ->  0S

Q19  ->  0Q20 | 1Q49

Q20  ->  0S

Q22  ->  0Q23 | 1Q26

Q23  ->  0Q24 | 1Q51

Q24  ->  0S

Q26  ->  0Q27 | 1Q53

Q27  ->  0S

Q29  ->  0Q30 | 1Q55

Q30  ->  0S

Q32  ->  1Q33

Q33  ->  1Q34

Q34  ->  0Q35 | 1Q38

Q35  ->  0Q36 | 1Q57

Q36  ->  0S

Q38  ->  0Q39 | 1Q59

Q39  ->  0S | 1S

Q41  ->  0S | 1S

Q43  ->  0S | 1S

Q45  ->  0S | 1S

Q47  ->  0S | 1S

Q49  ->  0S | 1S

Q51  ->  0S

Q53  ->  0S

Q55  ->  0S

Q57  ->  0S

Q59  ->  0S


Testing Grammar: 

To generate the word “test” with our grammar we must do the following:
Translate each letter in the word into braille represented as a binary string of length 6.
“t” =  011110
“e” =  100100
“s” =  011010
“t” =  011110

Combine each of the binary strings into one continuous string.
011110100100011010011110

Generate this string with the grammar.

S
0Q32
01Q33
011Q34
0111Q38
01111Q59
011110S
0111101Q1
01111010Q2
011110100Q3
0111101001Q19
01111010010Q20
011110100100S
0111101001000Q32
01111010010001Q33
011110100100011Q34
0111101001000110Q35
01111010010001101Q57
011110100100011010S
0111101001000110100Q32
01111010010001101001Q33
011110100100011010011Q34
0111101001000110100111Q38
01111010010001101001111Q59
011110100100011010011110S
011110100100011010011110λ
