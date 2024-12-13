# How the Language Works

## Alphabet
- `{0, 1}`

## Semantics
- The minimal string our language accepts is `λ`.  
- Strings of length greater than 0 must have a length that is a multiple of 6 (`length % 6 = 0`).  
  - **Example**:  
    - `100000` is accepted.  
    - `100` is rejected.  
- Each segment of 6 must correlate to a letter in the English alphabet.  
  - **Example**:  
    - `100000` correlates to “a”.  
    - `111111` does not correlate to any letter and is rejected.  

To utilize our language, English letters must be converted into binary strings of length 6, and vice versa.

---

## Example: Translating the Letter “a” into a Binary String

1. Find the letter “a” in Figure 1, **BRAILLE Alphabet**.  
   - `a = ⠁`  
2. Translate each row of the 3x2 grid into a binary sequence by reading left to right:  
   - **First row**: dot, blank → `10`  
   - **Second row**: blank, blank → `00`  
   - **Third row**: blank, blank → `00`  
3. Concatenate all rows together, top to bottom, to achieve the binary representation of the letter:  
   - `100000`

---

## Example: Translating a Binary String (`100000101000`) into English Letters

1. Break the string into segments of length = 6:  
   - `100000101000` → `100000` `101000`
2. Break those segments into 3 parts of 2:  
   - `100000` → `10` `00` `00`  
   - `101000` → `10` `10` `00`  
3. Stack each of the 3 segments on top of each other (leftmost on top):  
   - `100000` →  
     ```
     10
     00
     00
     ```  
   - `101000` →  
     ```
     10
     10
     00
     ```  
4. Reference Figure 1, **BRAILLE Alphabet**, to find the corresponding letters:  
   - A `1` corresponds to a dot, and a `0` corresponds to blank space.  
   - `⠁` = “a”  
   - `⠃` = “b”  

**Result**:  
- `100000101000` → “ab”



**Figure 1**



![image](https://github.com/user-attachments/assets/31042701-243a-4432-b4be-baa7d5d8add4)


