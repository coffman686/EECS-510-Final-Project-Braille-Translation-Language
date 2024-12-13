# Testing Grammar

## Generating the Word “test” with Our Grammar

To generate the word “test” with our grammar, we must follow these steps:

### 1. Translate Each Letter into Braille Represented as a Binary String of Length 6

- **“t”** = `0111101` &rarr; <span style="color:red">011110</span>
- **“e”** = `100100` &rarr; <span style="color:green">100100</span>
- **“s”** = `011010` &rarr; <span style="color:blue">011010</span>
- **“t”** = `011110` &rarr; <span style="color:red">011110</span>

### 2. Combine the Binary Strings into One Continuous String
<span style="color:red">011110</span><span style="color:green">100100</span><span style="color:blue">011010</span><span style="color:red">011110</span>
### 3. Generate the String with Our Grammar
**S**

<span style="color:red">0</span>**Q32**

<span style="color:red">01</span>**Q33**

<span style="color:red">011</span>**Q34**

<span style="color:red">0111</span>**Q38**

<span style="color:red">01111</span>**Q59**

<span style="color:red">011110</span>**S**

<span style="color:red">011110</span><span style="color:green">1</span>**Q1**

<span style="color:red">011110</span><span style="color:green">10</span>**Q2**

<span style="color:red">011110</span><span style="color:green">100</span>**Q3**

<span style="color:red">011110</span><span style="color:green">1001</span>**Q19**

<span style="color:red">011110</span><span style="color:green">10010</span>**Q20**

<span style="color:red">011110</span><span style="color:green">100100</span>**S**

<span style="color:red">011110</span><span style="color:green">100100</span><span style="color:blue">0</span>**Q32**

<span style="color:red">011110</span><span style="color:green">100100</span><span style="color:blue">01</span>**Q33**

<span style="color:red">011110</span><span style="color:green">100100</span><span style="color:blue">011</span>**Q34**

<span style="color:red">011110</span><span style="color:green">100100</span><span style="color:blue">0110</span>**Q35**

<span style="color:red">011110</span><span style="color:green">100100</span><span style="color:blue">01101</span>**Q57**

<span style="color:red">011110</span><span style="color:green">100100</span><span style="color:blue">011010</span>**S**

<span style="color:red">011110</span><span style="color:green">100100</span><span style="color:blue">011010</span><span style="color:red">0</span>**Q32**

<span style="color:red">011110</span><span style="color:green">100100</span><span style="color:blue">011010</span><span style="color:red">01</span>**Q33**

<span style="color:red">011110</span><span style="color:green">100100</span><span style="color:blue">011010</span><span style="color:red">011</span>**Q34**

<span style="color:red">011110</span><span style="color:green">100100</span><span style="color:blue">011010</span><span style="color:red">0111</span>**Q38**

<span style="color:red">011110</span><span style="color:green">100100</span><span style="color:blue">011010</span><span style="color:red">01111</span>**Q59**

<span style="color:red">011110</span><span style="color:green">100100</span><span style="color:blue">011010</span><span style="color:red">011110</span>**S**

<span style="color:red">011110</span><span style="color:green">100100</span><span style="color:blue">011010</span><span style="color:red">011110</span>**&lambda;**